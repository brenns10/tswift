#!/usr/bin/env python3
"""
Download all the song lyrics for a particular artist, store in a file.
"""

from __future__ import print_function
from tswift import Artist


def download_all_songs(artist, outfn):
    artist_object = Artist(artist)
    artist_object.load(verbose=True)
    nsongs = len(artist_object.songs)
    outfile = open(outfn, 'w')

    for i, song in enumerate(artist_object.songs):
        print("%03d/%03d - %s - %s" % (i, nsongs, song._title, song._artist))
        song.load()
        print(song.lyrics, file=outfile)
        print("\n\n", file=outfile)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Need to pass artist and output file.')
        sys.exit(1)
    download_all_songs(*sys.argv[1:])
