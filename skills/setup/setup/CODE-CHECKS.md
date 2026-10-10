# Code checks

A pre-commit hook in a committed `.githooks/` directory runs the project's formatter and linter on staged files, then its typecheck. Reuse the tools the repository already has, and add a dependency only for a job nothing covers. No lint-staged: each tool below reads staged files itself or takes them as arguments.

## Contents

- Catalogue
- Steps: choose the tools, install and configure, write the hook, verify and commit
- Notes

## Catalogue

`<add-dev>` and `<run>` stand for the package manager's commands: `npm install -D` and `npx --no-install`, `pnpm add -D` and `pnpm exec`, `yarn add -D` and `yarn`, `bun add -d` and `bunx`.

JavaScript and TypeScript, verified 2026-10-10 against each tool's documentation:

| Job | Tool | Present when | Install | Staged check |
| --- | --- | --- | --- | --- |
| Format and lint | Biome | `biome.json` or `biome.jsonc`, or the `@biomejs/biome` package | `<add-dev> @biomejs/biome`, then `<run> biome init` | `<run> biome check --staged --no-errors-on-unmatched --files-ignore-unknown=true` |
| Lint | oxlint | `.oxlintrc.json` or `oxlint.config.ts`, or the `oxlint` package | `<add-dev> oxlint` | `<run> oxlint --no-error-on-unmatched-pattern <files>` |
| Format | oxfmt | `.oxfmtrc.json`, `.oxfmtrc.jsonc`, or `oxfmt.config.ts`, or the `oxfmt` package | `<add-dev> oxfmt` | `<run> oxfmt --check --no-error-on-unmatched-pattern <files>` |
| Typecheck | `bun check` | A Bun lockfile, `tsconfig.json`, and a Bun that has `bun check` (documented for 1.4.3) | Comes with Bun | `bun check` |
| Typecheck | TypeScript | `tsconfig.json` | `<add-dev> typescript` | `<run> tsc --noEmit` |

`bun check` reads `tsconfig.json`, reports TypeScript 7's errors, and writes nothing. A `check` script in `package.json` takes precedence over it; see [Bun's page](https://bun.com/docs/runtime/check) for that case. Keep `tsc` where the project emits declaration files.

Python, not checked on 2026-10-10: Ruff formats and lints (`ruff.toml`, `.ruff.toml`, or `[tool.ruff]` in `pyproject.toml`; staged check `ruff format --check <files>` and `ruff check <files>`). Keep a configured type checker (mypy, pyright) as it is.

Other languages: use the toolchain's own commands (`gofmt -l`, `go vet`, `cargo fmt --check`, `cargo clippy`), with no catalogue entry.

Migrations from older tooling, verified 2026-10-10. Run each without its write flag first where it has one, to preview:

| From | To | Command |
| --- | --- | --- |
| Prettier | Biome | `<run> biome migrate prettier --write` |
| ESLint | Biome | `<run> biome migrate eslint --write`; `--include-inspired` adds rules Biome only approximates |
| Prettier | oxfmt | `<run> oxfmt --migrate=prettier` |
| ESLint (flat configuration) | oxlint | `npx @oxlint/migrate [config path]`; `--type-aware` carries typed rules |

## Steps

### 1. Choose the tools

Work from the inspection's `configs`, `packages`, and `package_scripts` lines, and from the conventions' tool rules:

- **A catalogue tool is present**: use it and install nothing.
- **Older tooling (ESLint, Prettier)**: offer a move, never make it unasked. Recommend Biome when one tool for both jobs fits; recommend oxlint and oxfmt when Prettier-identical output matters or ESLint plugins must keep running (oxlint runs ESLint JavaScript plugins, an alpha feature). Name what the move would drop, from the migration preview. When the user declines, wire the existing tools into the hook.
- **Nothing present**: recommend Biome for JavaScript and TypeScript, Ruff for Python.
- **A hook manager is present (Husky, lefthook, the pre-commit framework, lint-staged)**: ask whether to replace it with `.githooks/` or to add the checks to it. When kept, add the commands there and skip step 3.
- **Typecheck**: an existing `typecheck` script first, then `bun check` on a Bun project, then `tsc --noEmit`.
- **Style**: carry each conventions rule a tool can hold (indentation, line width, quotes, import order, banned constructs) into its configuration. When a documented rule disagrees with an existing configuration, ask which wins. With neither, ask for indentation (default 2 spaces), line width (default 160), and for JavaScript, quotes (default double), semicolons (default always), and trailing commas (default none).
- **Build**: offer to run the build in the hook as well; recommend against it, since it slows every commit.

Completion: each staged language has one formatter and one linter, or none by the user's choice, and the typecheck command is chosen.

### 2. Install and configure

Install only the missing packages, as quiet commands. Write a tool's configuration only when none exists, from its own init command where it has one, then apply the style choices. Run an accepted migration, run the new check on the whole repository, and remove the old packages and configuration only after that check passes and the user agrees.

When the conventions document names a tool this area replaced, update that line; when there is no conventions document, say so in the report and create none.

Completion: each chosen tool runs once on the whole repository with exit 0, or its findings are reported to the user.

### 3. Write the hook

Write `.githooks/pre-commit` with one line per chosen tool and make it executable. For example, Biome with `tsc`, and oxlint on staged TypeScript:

```sh
#!/bin/sh
# Checks staged files, then typechecks. Written by setup; edit freely.
set -eu
has_staged() { ! git diff --cached --quiet --diff-filter=ACMR -- "$@"; }
staged() { git diff --cached --name-only -z --diff-filter=ACMR -- "$@"; }

npx --no-install biome check --staged --no-errors-on-unmatched --files-ignore-unknown=true
if has_staged '*.ts' '*.tsx'; then staged '*.ts' '*.tsx' | xargs -0 npx --no-install oxlint --no-error-on-unmatched-pattern; fi
npx --no-install tsc --noEmit
```

The hook checks and never writes, so a partly staged file is never rewritten behind the committer's back; they run the formatter and stage again.

Move any hook already in `.git/hooks/` into `.githooks/`, then run `git config core.hooksPath .githooks`. So that clones get it too, add a `prepare` script to `package.json` (`git config core.hooksPath .githooks`, appended with `&&` to an existing one; a published package guards it with `git rev-parse --git-dir >/dev/null 2>&1 &&` and `|| true`). Without `package.json`, add the command to the project's setup instructions.

Completion: `git config core.hooksPath` prints `.githooks`, and the hook is executable.

### 4. Verify and commit

Run `.githooks/pre-commit` with nothing staged and expect exit 0. Then stage a deliberately misformatted scratch file in a checked language, run the hook and expect a failure naming it, and unstage and delete the file.

Commit only the files this area wrote: `.githooks/`, tool configuration, `package.json`, and the lockfile. Ask first when the branch is the default branch and other changes are uncommitted. The commit runs through the new hook.

Completion: the hook passed clean, failed on the scratch file, and the commit went through it.

## Notes

- `core.hooksPath` replaces `.git/hooks/` entirely; hooks left there stop running.
- For parallel steps or per-file-type runners, lefthook is the next step up.
