# tswift

This repo is actually not directly related to Taylor Swift.  It's just a simple
Python API for getting lyrics from MetroLyrics.  Here is how easy it is:

```python
from tswift import Artist
import random

tswift = Artist('taylor-swift')
tswift.load()
song = random.choice(tswift.songs)
song.load()
print(song.lyrics)
```

## Setup

This package needs `lxml` and `requests`, which you can probably get off of pip.
It was intended for Python 3, but it seems to run on Python 2 as well, so hooray
for that.  Once you have the dependencies, you can just clone this and put
`tswift.py` in your Python Path, or maybe one day I'll make a `setup.py` and put
it on pip.
