#!/usr/bin/env python3
"""
Download all the song lyrics for a particular artist, store in a file.
"""
import argparse
import json
from multiprocessing.pool import ThreadPool

from tswift import Artist, Song


def download_all_songs(artist, outfn, as_json=False):
    artist_object = Artist(artist)
    artist_object.load(verbose=True)
    outfile = open(outfn, 'w')

    pool = ThreadPool()
    songs = artist_object.songs
    print('loading %d songs in parallel!' % len(artist_object.songs))
    pool.map(Song.load, songs)
    if json:
        objs = []
        for song in songs:
            objs.append({
                "title": song.title,
                "artist": song.artist,
                "url": song._url,
                "lyrics": song.lyrics,
            })
        json.dump(objs, outfile)
    else:
        for song in songs:
            print(song.lyrics, file=outfile)
            print("\n\n", file=outfile)

    outfile.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="lyric downloader")
    parser.add_argument("artist", help="Artist to download")
    parser.add_argument("outfn", help="Output filename")
    parser.add_argument("--json", action="store_true", help="Use JSON output")
    args = parser.parse_args()
    download_all_songs(args.artist, args.outfn, args.json)
