# Unused-code tools

Verified: 2026-11-19, against each tool's documentation, except where a row says otherwise.

Run a tool without adding it to the project: `npx`, `pnpm dlx`, `bunx`, `uvx`, or `go run` with a version. Installing one on the machine (`cargo install`, `brew install`, a global `pip install`) changes more than the repository, so ask the user first. When the project already configures one of these tools, run it through the project's script with its configuration.

| Ecosystem | Finds | Run | Notes |
| --- | --- | --- | --- |
| JavaScript, TypeScript | Unused files, exports, types, enum and namespace members, dependencies | `npx knip` (or `pnpm dlx knip`, `bunx knip`) | `--production` checks only shipped code: `dependencies`, production entries, and the `start` script. `--fix` edits files; leave it off and remove by hand, so each removal gets a verdict |
| Python | Unused functions, classes, variables, imports, unreachable code | `uvx vulture <paths>` | Confidence 100 means certain within the analysed files; 60 (functions, classes, attributes) is a rough estimate. `--make-whitelist` writes the false positives to a file the next run reads |
| Python | Unused dependencies (rule `DEP002`) | `deptry .` inside the project's environment, for example `uv run --with deptry deptry .` | A global install does not see the project's packages. `uv run --with` is from uv's documentation, not deptry's |
| Go | Functions unreachable from any `main` | `go run golang.org/x/tools/cmd/deadcode@latest -test ./...` | `-test` adds the `go test` mains, so a library is analysed through its tests. `-whylive=<function>` prints the call chain that keeps a function alive. Blind to calls from assembly and `go:linkname` |
| Rust | Unused private items | `cargo check`, then read the `dead_code` and `unused_imports` warnings | The compiler does not flag a `pub` item of a library crate. Not checked against documentation: compiler lints are standard |
| Rust | Unused dependencies | `cargo machete` | Needs `cargo install cargo-machete`. Exit 1 means it found some. `--with-metadata` cuts false positives but can modify `Cargo.lock` |

`depcheck` is archived (2025) and points to knip; do not use it.

## Elsewhere

For a language without a row, use the compiler's or the linter's unused warnings when the project's build already produces them, then [find-unreferenced.py](../scripts/find-unreferenced.py) on the source folders with `--stem`. The script is also the only check for assets, styles, fixtures, and scripts in every ecosystem.
