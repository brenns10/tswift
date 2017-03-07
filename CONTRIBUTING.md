How to Contribute
=================

Bug Reports
-----------

Bug reports are welcome, as are feature requests. Keep in mind that this project
is not my main one, and so not everything (especially feature requests) can be
done by me. If you want to be certain, try implementing it yourself and
submitting a pull request!

Pull Requests
-------------

Some guidelines:

- Use [PEP8](https://www.python.org/dev/peps/pep-0008/) style. Try running
  `flake8` before committing to be sure.
- This module is Python 2/3 compatible. Make sure to test your changes on Python
  2.7 as well as a sufficiently recent version of Python 3 (i.e. 3.3).
- If your changes involve a bug fix, an API change, an addition, or a deletion,
  chances are it belongs in [`CHANGELOG.md`][changelog]. Please make sure your
  pull request includes an addition under the `[Unreleased]` header, using the
  proper subsection header (e.g. `Fixed`, `Added`, `Deprecated`, `Removed`,
  etc). See [Keep A Changelog][keepa] for more information.
- Updates to master are not immediately reflected on PyPI. If you would like
  your changes to be reflected quickly, make a note of it in your PR and I will
  try to make a version bump as soon as possible on PyPI.

[changelog]: CHANGELOG.md
[keepa]: http://keepachangelog.com
