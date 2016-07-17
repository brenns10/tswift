#!/usr/bin/env python3
"""
Get Taylor Swift Lyrics!

Actually, this module is more general than just Taylor Swift.  It is a
MetroLyrics API of sorts, that allows you to get song lyrics and find all songs
by an artist.  My use case for this API was rather simple, and thus the API
doesn't have much.  It is mainly useful if you want to get the lyrics of all
songs written by a certain artist (for example, Taylor Swift).
"""

from lxml import html
import requests
import re
import random

ARTIST_URL = "http://www.metrolyrics.com/{artist}-alpage-{n}.html"
SONG_URL = "http://www.metrolyrics.com/{title}-lyrics-{artist}.html"
SONG_RE = r'http://www\.metrolyrics\.com/(.*)-lyrics-(.*)\.html'


class Song(object):
    """An object that represents a song, whose lyrics can be retrieved."""

    def __init__(self, title=None, artist=None, url=None):
        """
        Create a song.

        You can EITHER provide a URL for the song lyrics, OR provide the
        lower-case hyphenated song title and artist.  If both are provided, the
        URL is preferred.
        """
        self._lyrics = None
        if url is not None:
            self._url = url
            self._title, self._artist = re.match(SONG_RE, url).groups()
        elif title is not None and artist is not None:
            self._title = title
            self._artist = artist
            self._url = SONG_URL.format(title=title, artist=artist)
        else:
            raise ValueError('Must provide either title & artist or URL.')

    def load(self):
        """Load the lyrics from MetroLyrics."""
        page = requests.get(self._url)
        # Forces utf-8 to prevent character mangling
        page.encoding = 'utf-8'

        tree = html.fromstring(page.text)
        lyric_div = tree.get_element_by_id('lyrics-body-text')
        verses = [c.text_content() for c in lyric_div]
        self._lyrics = '\n\n'.join(verses)
        return self

    @property
    def lyrics(self):
        if self._lyrics is None:
            self.load()
        return self._lyrics

    def __str__(self):
        return 'Song(title=%r, artist=%r)' % (self._title, self._artist)

    def __repr__(self):
        return self.__str__()


class Artist(object):
    """
    An object that represents an artist, and can get you their songs.

    Pass into the constructor the "name" of the artist.  Generally, this is the
    lower case name with spaces replaced by hyphens, and punctuation removed.
    I don't really provide any utilities for searching for this name.  If you
    just Google the artist + " lyrics", you'll probably get their MetroLyrics
    page, and so you can get the artist's "name" from that.
    """

    def __init__(self, name):
        self._songs = None
        self._name = name

    def load(self, verbose=False):
        """
        Load the list of songs.

        Note that this only loads a list of songs that this artist was the main
        artist of.  If they were only featured in the song, that song won't be
        listed here.  There is a list on the artist page for that, I just
        haven't added any parsing code for that, since I don't need it.
        """
        self._songs = []
        page_num = 1
        total_pages = 1

        while page_num <= total_pages:
            if verbose:
                print('retrieving page %d' % page_num)
            page = requests.get(ARTIST_URL.format(artist=self._name,
                                                  n=page_num))
            tree = html.fromstring(page.text)
            song_rows_xp = r'//*[@id="popular"]/div/table/tbody/tr'
            songlist_pagination_xp = r'//*[@id="main-content"]/div[1]/'\
                                     'div[2]/p/span/a'

            rows = tree.xpath(song_rows_xp)
            for row in rows:
                song_link = row.xpath(r'./td/a[contains(@class,"title")]')
                assert len(song_link) == 1
                self._songs.append(Song(url=song_link[0].attrib['href']))

            total_pages = len(tree.xpath(songlist_pagination_xp))
            page_num += 1
        return self

    @property
    def songs(self):
        if self._songs is None:
            self.load()
        return self._songs

    def __str__(self):
        return 'Artist(%r)' % self._name

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    tswift = Artist('taylor-swift')
    song = random.choice(tswift.songs)
    print(song.lyrics)
