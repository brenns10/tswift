tswift
======

This repo is actually not directly related to Taylor Swift.  It's just a simple
Python API for getting lyrics from MetroLyrics.  Here is how easy it is:

.. code:: python

    from tswift import Artist
    import random

    tswift = Artist('taylor-swift')
    tswift.load()
    song = random.choice(tswift.songs)
    song.load()
    print(song.lyrics)

Setup
-----

This package depends on ``lxml`` and ``requests``.  These should be installed
when you install this package from pip:

.. code::

    pip install tswift


