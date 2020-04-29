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
from googlesearch import search
import argparse
import requests
import re
import random
import sys


ARTIST_URL = "https://www.metrolyrics.com/{artist}-alpage-{n}.html"
SONG_URL = "https://www.metrolyrics.com/{title}-lyrics-{artist}.html"
SONG_RE = r'https?://www\.metrolyrics\.com/(.*)-lyrics-(.*)\.html'


def slugify(string):
    return string.replace(' ', '-').lower()


def deslugify(string):
    return string.replace('-', ' ').title()


class TswiftError(Exception):
    """Base exception for errors raised in tswift."""


class Song(object):
    """An object that represents a song, whose lyrics can be retrieved."""

    def __init__(self, title=None, artist=None, url=None):
        """
        Create a song.

        You can EITHER provide a URL for the song lyrics, OR provide the song
        title and artist (which will be slugified). If both are provided, the
        URL is preferred.
        """
        self._lyrics = None
        if url is not None:
            self._url = url
            self.title, self.artist = re.match(SONG_RE, url).groups()
        elif title is not None and artist is not None:
            self.title = title
            self.artist = artist
            self._url = SONG_URL.format(
                title=slugify(title),
                artist=slugify(artist),
            )
        else:
            raise ValueError('Must provide either title & artist or URL.')

        self.title = deslugify(self.title)
        self.artist = deslugify(self.artist)

    def load(self):
        """Load the lyrics from MetroLyrics."""
        page = requests.get(self._url)

        if page.status_code > 200:
            raise TswiftError("No lyrics available for requested song")

        # Forces utf-8 to prevent character mangling
        page.encoding = 'utf-8'

        tree = html.fromstring(page.text)
        try:
            lyric_div = tree.get_element_by_id('lyrics-body-text')
            verses = [c.text_content() for c in lyric_div.find_class('verse')]
        except KeyError:
            raise TswiftError("No lyrics available for requested song")
        else:
            self._lyrics = '\n\n'.join(verses)

        return self

    @property
    def lyrics(self):
        if self._lyrics is None:
            self.load()
        return self._lyrics

    def format(self):
        return '%s\n%s\n%s\n\n%s' % (
            self.title,
            self.artist,
            '-' * max(len(self.title), len(self.artist)),
            self.lyrics,
        )

    def __repr__(self):
        return 'Song(title=%r, artist=%r)' % (self.title, self.artist)

    @staticmethod
    def find_song(lyrics):
        for url in search('site:www.metrolyrics.com ' + lyrics, stop=20):
            if re.match(SONG_RE, url):
                return Song(url=url)
        return None


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
        self.name = slugify(name)

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
            page = requests.get(ARTIST_URL.format(artist=self.name,
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

    def __repr__(self):
        return 'Artist(%r)' % self.name


def main():
    """
    Run the CLI.
    """
    parser = argparse.ArgumentParser(
        description='Search artists, lyrics, and songs!'
    )
    parser.add_argument(
        'artist',
        help='Specify an artist name (Default: Taylor Swift)',
        default='Taylor Swift',
        nargs='?',
    )
    parser.add_argument(
        '-s', '--song',
        help='Given artist name, specify a song name',
        required=False,
    )
    parser.add_argument(
        '-l', '--lyrics',
        help='Search for song by lyrics',
        required=False,
    )
    args = parser.parse_args()

    if args.lyrics:
        song = Song.find_song(args.lyrics)
    else:
        if args.song:
            song = Song(
                title=args.song,
                artist=args.artist,
            )
        else:
            artist = Artist(args.artist)
            if artist.songs:
                song = random.choice(artist.songs)
            else:
                print('Couldn\'t find any songs by artist {}!'
                      .format(args.artist))
                sys.exit(1)

    print(song.format())


if __name__ == '__main__':
    main()
