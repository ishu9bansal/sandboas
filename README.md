# Python Project Template (sandboas)

A lightweight, collaboration-ready Python template for:

- simulations
- standalone scripts
- small apps / backend services

It includes a clean `src/` layout, a runnable entry point, test setup, linting,
and simple dependency management so you can start coding logic immediately.

## Quick start

### 1) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Install project + dev tools

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

### 3) Run the sample app

```bash
python -m sandboas
```

### 4) Run tests and lint

```bash
pytest
ruff check .
```

## Dependency management

### Runtime dependencies
Add to `[project.dependencies]` in `pyproject.toml`, then reinstall:

```bash
pip install -e ".[dev]"
```

### Dev dependencies
Add to `[project.optional-dependencies].dev` in `pyproject.toml`, then reinstall:

```bash
pip install -e ".[dev]"
```

## Regular maintenance tasks

- Run tests: `pytest`
- Run lint checks: `ruff check .`
- Auto-fix safe lint issues: `ruff check . --fix`
- Keep tooling current in your venv:
  - `python -m pip install --upgrade pip`
  - reinstall editable package: `pip install -e ".[dev]"`

## Recommended structure

```text
.
├── pyproject.toml
├── README.md
├── src/
│   └── sandboas/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── test_main.py
```

## Conventions

- Keep business logic in modules under `src/sandboas/`.
- Keep scripts thin and call reusable functions from modules.
- Add tests under `tests/` for every feature module.
- Use type hints for public functions.
- Keep dependencies minimal and explicit in `pyproject.toml`.

## Start extending

1. Add modules under `src/sandboas/`.
2. Import them in `main.py` (or create new entry modules).
3. Add tests in `tests/`.
4. Commit frequently and collaborate through pull requests.
