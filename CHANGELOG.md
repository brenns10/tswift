Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/), and we
don't really adhere to Semantic Versioning. But that's mostly because we don't
make many changes to this project.

## [Unreleased]

## [0.4.0] - 2017-08-16
### Fixed
- Fix error caused by HTML comments within song div. Thanks [@nizzit][]!

## [0.3.0] - 2017-03-07
Thanks [@a-johnston][]!

### Fixed
- Variable names prefixed with underscore when they should convey publicness
- Removed unnecessary `__str__` definitions due to `__repr__` implementations

### Added
- Slugify and deslugify
- Song formatting for pretty printing
- Entry point for CLI, `tswift`
- Search for lyrics via the `google` package
- Artist name and song name CLI arguments

## [0.2.0] - 2016-07-16
### Fixed
- Forced UTF-8 encoding to prevent character mangling, thanks
  [@EsotericAlgorithm][]!

### Added
- Simplified API: `Artist.songs` and `Song.lyrics` are now properties that are
  loaded on first access, so calling `load()` is no longer necessary.
- Simplified API: `Artist.load()` and `Song.load()` return `self` so that you
  can perform further operations.
- Added `repr()` for `Artist`.
- Explicitly added Revised BSD license.

## [0.1.0] - 2015-08-19

Initial release!

[@nizzit]: https://github.com/nizzit
[@a-johnston]: https://github.com/a-johnston
[@EsotericAlgorithm]: https://github.com/EsotericAlgorithm
