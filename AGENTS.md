# Repository Guidelines

## Project Structure & Module Organization

`rework/` is the distributable Python package. `rework/core/management/` implements the `rework` (also `re` and `ro`) CLI; `rework/core/quickmodel/`, `devops/`, and `templates/` contain model helpers, Fabric tasks, and generated project files. `rework/contrib/users/` is the bundled Django app. Put package tests in the matching area of `tests/` (`tests/core/`, `tests/clis/`, or `tests/contrib/`). User documentation lives in `docs/`; packaging and dependencies are defined in `setup.py`, `pyproject.toml`, and the requirements files.

## Build, Test, and Development Commands

- `python -m pip install -r requirements_dev.txt` installs runtime and test dependencies for local work.
- `pytest` runs the full test suite; `pytest tests/core/test_custom_exceptions.py` runs one file.
- `black --check rework tests` checks formatting when Black is installed. Run `black rework tests` to format changed Python files.
- `python setup.py sdist bdist_wheel` builds the source and wheel distributions used by the release workflow.

For a manual CLI check, run `rework init pony` from a **new temporary directory**: initialization writes the project into the current directory.

## Coding Style & Naming Conventions

Use four-space indentation in Python, LF line endings, and a final newline (`.editorconfig`). Format Python with Black; `pyproject.toml` targets Python 3.10–3.12. Use `snake_case` for modules, functions, and tests, and `PascalCase` for classes. Keep new CLI behavior in `rework/core/management/` and reusable app behavior in `rework/contrib/`.

## Testing Guidelines

Tests use pytest, including discovery of `unittest.TestCase` classes. Name files `test_*.py` and test functions `test_*`; add focused regression tests beside the related tests when behavior changes. There is no configured coverage threshold. Run `pytest` before submitting a change.

## Commit & Pull Request Guidelines

Recent commits use short, descriptive subjects such as `Add django-nx dependency` and `Update to fabric 3.1.0 and drop Python 3.8`; follow that style and keep each commit focused. In pull requests, describe the behavior changed, note the test command and result, and link a relevant issue when one exists. Include screenshots only for visible UI or documentation rendering changes. Releases are published by the workflow on `v*` tags; do not upload packages as part of a routine PR.
