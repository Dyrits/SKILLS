# Code checks: JavaScript and TypeScript

Verified: 2026-10-10, against each tool's documentation.

`<add-dev>` and `<run>` stand for the package manager's commands: `npm install -D` and `npx --no-install`, `pnpm add -D` and `pnpm exec`, `yarn add -D` and `yarn`, `bun add -d` and `bunx`.

| Job | Tool | Present when | Install | Staged check |
| --- | --- | --- | --- | --- |
| Format and lint | Biome | `biome.json` or `biome.jsonc`, or the `@biomejs/biome` package | `<add-dev> @biomejs/biome`, then `<run> biome init` | `<run> biome check --staged --no-errors-on-unmatched --files-ignore-unknown=true` |
| Lint | oxlint | `.oxlintrc.json` or `oxlint.config.ts`, or the `oxlint` package | `<add-dev> oxlint` | `<run> oxlint --no-error-on-unmatched-pattern <files>` |
| Format | oxfmt | `.oxfmtrc.json`, `.oxfmtrc.jsonc`, or `oxfmt.config.ts`, or the `oxfmt` package | `<add-dev> oxfmt` | `<run> oxfmt --check --no-error-on-unmatched-pattern <files>` |
| Typecheck | `bun check` | A Bun lockfile, `tsconfig.json`, and a Bun that has `bun check` (documented for 1.4.3) | Comes with Bun | `bun check` |
| Typecheck | TypeScript | `tsconfig.json` | `<add-dev> typescript` | `<run> tsc --noEmit` |

`bun check` reads `tsconfig.json`, reports TypeScript 7's errors, and writes nothing. A `check` script in `package.json` takes precedence over it; see [Bun's page](https://bun.com/docs/runtime/check) for that case. Keep `tsc` where the project emits declaration files.

## Choosing

- **Nothing present**: Biome, one dependency for both jobs.
- **ESLint or Prettier present**: offer Biome when one tool for both jobs fits; offer oxlint and oxfmt when Prettier-identical output matters or ESLint plugins must keep running (oxlint runs ESLint JavaScript plugins, an alpha feature).
- **Typecheck**: an existing `typecheck` script, then `bun check` on a Bun project, then `tsc --noEmit`.
- **Style defaults** when neither conventions nor configuration decide: 2-space indentation, line width 160, double quotes, semicolons always, no trailing commas.

## Migrations

Run each without its write flag first where it has one, to preview what it drops.

| From | To | Command |
| --- | --- | --- |
| Prettier | Biome | `<run> biome migrate prettier --write` |
| ESLint | Biome | `<run> biome migrate eslint --write`; `--include-inspired` adds rules Biome only approximates |
| Prettier | oxfmt | `<run> oxfmt --migrate=prettier` |
| ESLint (flat configuration) | oxlint | `npx @oxlint/migrate [config path]`; `--type-aware` carries typed rules |

## Hook lines

```sh
npx --no-install biome check --staged --no-errors-on-unmatched --files-ignore-unknown=true
if has_staged '*.ts' '*.tsx'; then staged '*.ts' '*.tsx' | xargs -0 npx --no-install oxlint --no-error-on-unmatched-pattern; fi
npx --no-install tsc --noEmit
```

So that clones get the hooks path, add a `prepare` script to `package.json`: `git config core.hooksPath .githooks`, appended with `&&` to an existing one. A published package guards it: `git rev-parse --git-dir >/dev/null 2>&1 && git config core.hooksPath .githooks || true`.
