# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

django-rework is a rapid development framework built on Django and Django-Ninja, providing a non-verbose Django development experience. It bundles a CLI, project scaffolding, simplified model definitions, and Fabric-based deployment into a single package.

## Commands

### Setup
```bash
pip install -r requirements_dev.txt
```

### Run tests
```bash
pytest
# Run a single test file
pytest tests/core/test_custom_exceptions.py
```

### Format
```bash
black .
```

### Manual project creation test
```bash
cd examples && rm -rf * && rm -rf .* && rework init pony
```

### Build and publish (on v* tag push)
```bash
python setup.py sdist bdist_wheel && twine upload dist/*
```

## Architecture

### CLI Entry Point

The CLI is exposed as three console scripts (`rework`, `re`, `ro`) all pointing to `rework.core.management:execute_from_command_line`. Commands are dispatched via a `COMMANDS` dict in `rework/core/management/__init__.py`:

- `init` → `project.init` — scaffolds a new Django project in the current directory (hacks `argv` to append `'.'` for `startproject`)
- `add` → `app.add` — adds built-in contrib apps (e.g., `users`)
- `deploy` → `deploy.DeployCommand()` — Fabric-based deployment
- `migrate` → `migrate.migrate` — runs Django migrations

### Core Package (`rework/core/`)

- **quickmodel** — Simplified field types (`Str`, `LongStr`, `Int`, `Float`, `Decimal`, `Bool`, `DateTime`, `Date`, `Time`, `UUID`, `JSON`) that wrap Django model fields with sensible defaults. Inspired by SQLModel/PonyORM.
- **exceptions** — `ServiceUnavailable` (503) and `ValidateError` (400, with optional `errors` list) extending DRF's `APIException`.
- **views** — Custom DRF exception handler that adds `code`, `detail`, and `errors` keys to error responses. Configured via `REST_FRAMEWORK['EXCEPTION_HANDLER']`.
- **devops** — Fabric-based deployment with host loading (`hosts.py`), task definitions (`fabric_tasks.py`), and environment support (dev/test/prod).
- **templates** — `.tpl` files for project scaffolding (fabfile, requirements).
- **utils** — `say()` (CLI output helper) and `copy_template_to_file()`.

### Contrib Apps (`rework/contrib/`)

- **users** — `EnhancedAbstractUser` model extending Django's `AbstractUser` with `mobile`, `nickname`, `avatar` fields and a custom `UserManager`. Added to projects via `rework add users`.

### Key Design Decisions

- The `init` command always creates the project in the current directory (`.`), not as a subdirectory.
- QuickModel fields provide opinionated defaults (e.g., `Str` uses `TextField` with `max_length=150` and `default=""`).
- Deployment uses Fabric 3.x with host configs loaded via `rework.core.devops.hosts.loads()`.
- The framework targets MySQL (via `django-mysql` and `mysqlclient`).

## Code Style

- Black formatter with target versions py310/py311/py312
- Max line length: 99 (from .editorconfig)
- Python >=3.10 required
