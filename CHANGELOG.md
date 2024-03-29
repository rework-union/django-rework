# Change Log
# All notable changes to this project will be documented in this file.
# This project adheres to [Semantic Versioning](http://semver.org/).
# includes Added / Changed / Fixed

Release Notes for versions 0.5 or later
https://github.com/rework-union/django-rework/releases

## [0.5.2] 2023-03-03
### Added
- 400 bad request response format
### Changed
- Upgraded all dependency packages
- Drop Python 3.7 support

## [0.5.1] 2023-02-11
### Fixed
- Fixed the old configuration path is wrong
- Fixed ALLOWED_HOSTS settings read env

## [0.5.0] 2023-02-10
### Added
- Added `django-environ` to manage environments
- Restored the settings file from settings package
- Agile API development support Pydantic and FastAPI style with `django-ninja`
### Changed
- Optimized CLI UI
- Started MySQL/Redis/Supervisor as installed
- `devops` docs
- Upgraded all dependency packages

## [0.4.0] 2021-11-07
### Added
- Converted `uWSGI` to `Gunicorn`.

### Changed
- Refactor the deploy command templates.
- Liberalized mysqlclient version.
- Changed yapf COLUMN_LIMIT from 100 to 99.
- Updated to `Python 3.7.9`.
- Updated to `Redis 4.0.14`.

## [0.3.0] 2021-07-05
### Added
- Combined nginx & supervisor to `infrastructure`.

## [0.2.0] 2021-07-05
### Added
- Added code formatter `yapf`.
- Added contrib app `users`

## [0.1.0] 2020-03-05
### Added
- Added `django-rework init` command. It used to create a new project.
- Added `django-rework add` command.
- Added Deploy
