# Code checks: Python

Verified: 2026-10-10, against each tool's documentation.

`<run>` is `uv run` in a uv project (a `uv.lock`), and the virtual environment's own command otherwise.

| Job | Tool | Present when | Install | Staged check |
| --- | --- | --- | --- | --- |
| Format and lint | Ruff | `ruff.toml`, `.ruff.toml`, or `[tool.ruff]` in `pyproject.toml` | `uv add --dev ruff`, or `pip install ruff` | `<run> ruff format --check --force-exclude <files>` and `<run> ruff check --force-exclude <files>` |
| Typecheck | mypy or pyright | Their configuration or package | Keep as configured | Their configured command |
| Typecheck | ty | `[tool.ty]` in `pyproject.toml`, `ty.toml`, or the `ty` package | `uv add --dev ty`, or `pip install ty` | `<run> ty check` |

`--force-exclude` makes Ruff honour its exclusions for files passed by name, as the hook does. `ruff format --check` writes nothing and exits non-zero when a file would change.

## Choosing

- **Nothing present**: Ruff for both jobs.
- **Black, isort, or Flake8 present**: offer Ruff, which replaces all three. There is no migration command: carry their settings (line length, import sections, enabled rules) into Ruff's configuration by hand, and name any Flake8 plugin with no Ruff rule.
- **Typecheck**: keep a configured mypy or pyright. With none, offer ty; its documentation states no stability level, so say so when offering it.
- **Style defaults** when neither conventions nor configuration decide: Ruff's own.

## Hook lines

```sh
if has_staged '*.py' '*.pyi'; then
  staged '*.py' '*.pyi' | xargs -0 uv run ruff format --check --force-exclude
  staged '*.py' '*.pyi' | xargs -0 uv run ruff check --force-exclude
fi
uv run ty check
```

Without `package.json`, add `git config core.hooksPath .githooks` to the project's setup instructions so clones get the hooks.
