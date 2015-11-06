#!/usr/bin/env python3
"""
Download all the song lyrics for a particular artist, store in a file.
"""

from __future__ import print_function
from multiprocessing.pool import ThreadPool

from tswift import Artist, Song


def download_all_songs(artist, outfn):
    artist_object = Artist(artist)
    artist_object.load(verbose=True)
    outfile = open(outfn, 'w')

    pool = ThreadPool()
    songs = artist_object.songs
    print('loading %d songs in parallel!' % len(artist_object.songs))
    pool.map(Song.load, songs)
    for song in songs:
        print(song.lyrics, file=outfile)
        print("\n\n", file=outfile)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Need to pass artist and output file.')
        sys.exit(1)
    download_all_songs(*sys.argv[1:])
