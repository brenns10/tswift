import re
import sys

from google import search
from tswift import Song
from tswift import SONG_RE


def find_song(lyrics):
    for url in search('site:www.metrolyrics.com ' + lyrics, stop=20):
        if re.match(SONG_RE, url):
            return Song(url=url)
    return None


if __name__ == '__main__':
    if len(sys.argv) > 1:
        song = find_song(sys.argv[1])
        print(song.format() if song else 'No song found :(')
