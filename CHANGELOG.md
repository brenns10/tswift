Changelog
=========

## [Unreleased]
### Fixed
- Variable names prefixed with underscore when they should convey publicness
- Unnecessary ```__str__``` definitions due to ```__repr__``` implementations

### Added
- Artist name and song name arguments
- Naive slug and deslug
- Song formatting for pretty printing

## [0.2.0] - 2016-07-16
### Fixed
- Forced UTF-8 encoding to prevent character mangling, thanks
  @EsotericAlgorithm!

### Added
- Simplified API: `Artist.songs` and `Song.lyrics` are now properties that are
  loaded on first access, so calling `load()` is no longer necessary.
- Simplified API: `Artist.load()` and `Song.load()` return `self` so that you
  can perform further operations.
- Added `repr()` for `Artist`.
- Explicitly added Revised BSD license.

## [0.1.0] - 2015-08-19

Initial release!
