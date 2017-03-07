tswift
======

This repo is actually not directly related to Taylor Swift.  It's just a simple
Python API for getting lyrics from MetroLyrics.  Here is how easy it is:

.. code:: python

    from tswift import Artist
    import random

    tswift = Artist('Taylor Swift')
    song = random.choice(tswift.songs)
    print(song.format())

Setup
-----

This package depends on ``lxml``, ``requests``, and ``google``. These should be
installed when you install this package from pip:

.. code::

    pip install tswift

After installing, you can also print a random Taylor Swift song lyric with the
command:

.. code::

    tswift

CLI
---

The module comes with a simple command line interface. By default, it will
display a random song by Taylor Swift. You can specify an artist like this:

.. code::

    tswift 'Lynyrd Skynyrd'

You can choose a particular song:

.. code::

    tswift 'Lynyrd Skynyrd' -s Freebird

There is also a "lyric search mode", which allows you to search for a song by
lyrics, e.g.:

.. code::

    tswift -l 'I would walk 500 miles'

    Im Gonna Be 500 Miles
    Proclaimers
    ---------------------

    When I wake up, well I know I'm gonna be,
    I'm gonna be the man who wakes up next you
    ...

API
---

Artist class
************

The constructor takes a single argument, the artist name. This name will be
"slugified" in order to use it within URLs. This process involves replacing
spaces with hyphens, and making everything lowercase. If this is not sufficient
for your particular artist, you'll need to provide a pre-slugified version of
their name.

- ``songs`` - a list of Song instances by this artist. This will call ``load()``
  if it hasn't been called yet
- ``name`` - the artist's slugified name
- ``load()`` - populates the ``songs`` list

Song class
**********

The constructor can be called in two ways. In the first, you provide a
Metrolyrics URL, and the class will infer the artist and song title:

.. code:: python

    s = Song(url='url here')

In the second way, you provide a title and artist, which will be slugified.

.. code:: python

    s = Song('Taylor Swift', 'Love Story')

The attributes are:

- ``lyrics`` - a string. Accessing this will call ``load()`` if not yet loaded
- ``title`` - de-slugified title of song
- ``artist`` - de-slugified artist name
- ``load()`` - loads the lyrics
- ``format()`` - returns the lyrics, with a header that includes the title and
  artist.

The static method ``Song.find_song(lyrics)`` takes a string with a search term,
and performs a Google search. It returns a Song instance corresponding to the
first Metrolyrics link it finds, stopping after 20 results. If nothing is found,
returns ``None``.
