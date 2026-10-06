---
name: setup-git-hooks
description: Set up versioned git hooks via core.hooksPath (no Husky) with lint-staged (Biome, plus Prettier only for languages Biome leaves uncovered and only if the user wants it), plus typecheck and build. Use when user wants to add pre-commit hooks, commit-time formatting/linting/typechecking, or to replace Husky with git's built-in hooks path.
metadata:
  forks: "mattpocock/skills/skills/misc/setup-pre-commit"
---

# Setup Git Hooks

## What This Sets Up

- **`core.hooksPath`** pointing at a committed `.githooks/` dir (git built-in, no Husky needed)
- **lint-staged** running Biome on the languages it supports
- **Biome** config (if missing)
- **Prettier** for the languages Biome leaves uncovered, only when the user opts in
- **typecheck** and **build** scripts in the pre-commit hook

Why not Husky: Husky's only job is copying runners into `.git/hooks/`. `git config core.hooksPath .githooks` does the same with zero dependencies. A `prepare` script sets the config on every `npm install`, so teammates are covered on clone.

## Steps

### 1. Detect package manager and existing hook tooling

Check for `package-lock.json` (npm), `pnpm-lock.yaml` (pnpm), `yarn.lock` (yarn), `bun.lockb` (bun). Use whichever is present. Default to npm if unclear.

If the repository already uses Husky (a `.husky/` directory or `prepare: husky`), ask the user now, before anything is installed or written, whether to migrate off it or keep Husky and stop here.

### 2. Map formatter coverage

List the languages the repository contains, then check which ones the Biome version you will install formats and lints (its documentation or `biome --help`). Some languages, HTML among them in Biome 2.x, are covered only once enabled in `biome.json`; count them as covered and enable them in step 7. Keep a formatter the project already uses (oxfmt, dprint, Prettier) and route its languages to it.

When languages remain uncovered, offer Prettier for them, naming each language, and let the user decline.

Completion: every language in the repository is assigned to Biome, an existing formatter, Prettier (accepted), or no formatter (declined).

### 3. Install dependencies

Install `lint-staged` and `@biomejs/biome` as devDependencies, plus `prettier` only when the user accepted it. Skip any tool the repository already has.

### 4. Create `.githooks/pre-commit`

Write this file and make it executable (`chmod +x .githooks/pre-commit`):

```bash
#!/bin/sh
npx lint-staged
npm run typecheck --if-present
npm run build --if-present
```

**Adapt**: Replace `npm` with detected package manager (`pnpm --if-present` is not supported, so check package.json for the script first and omit the line if missing). Omit `typecheck` or `build` if the repository has no such script in package.json, and tell the user.

### 5. Point git at the hooks dir

```bash
git config core.hooksPath .githooks
```

This is local config; new clones need it too. Add a `prepare` script to package.json so it runs on every install:

```json
{
  "scripts": {
    "prepare": "git config core.hooksPath .githooks"
  }
}
```

Merge into existing scripts; if `prepare` already exists, append the `git config` call (e.g. `&&`).

### 6. Create `.lintstagedrc`

Biome handles format and lint (`check`) for the languages assigned to it in step 2. Add a Prettier entry only for languages the user assigned to Prettier:

```json
{
  "*.{js,jsx,ts,tsx,json,jsonc,css,graphql}": "biome check --write --no-errors-on-unmatched",
  "*.{html,md,mdx,yaml,yml,scss,vue,svelte,astro}": "prettier --write"
}
```

Give each glob exactly one tool, and list only the extensions the repository contains.

### 7. Create `biome.json` and `.prettierrc` (if missing)

Only create a config if none exists (check for `biome.json`, `biome.jsonc`, `.prettierrc`, `.prettierrc.json`, `prettier.config.*`). Enable the opt-in languages step 2 assigned to Biome. Write `.prettierrc` only when Prettier was accepted.

Biome defaults (`biome.json`). Ask the user for base formatter preferences before writing (see questions below), then write the file:

```json
{
  "$schema": "https://biomejs.dev/schemas/latest/schema.json",
  "formatter": {
    "enabled": true,
    "indentWidth": 2,
    "lineWidth": 160,
    "trailingComma": "none"
  },
  "javascript": {
    "formatter": {
      "quoteStyle": "double",
      "semicolons": "always",
      "arrowParentheses": "always"
    }
  },
  "json": {
    "formatter": { "enabled": true }
  },
  "css": {
    "formatter": { "enabled": true }
  },
  "linter": { "enabled": true },
  "organizeImports": { "enabled": true },
  "assist": {
    "actions": {
      "source": {
        "useSortedAttributes": "on",
        "useSortedKeys": "on",
        "useSortedProperties": "on"
      }
    }
  }
}
```

Ask the user for base parameters before writing `biome.json` (skip any already answered or fixed above):
- Tabs or spaces (default: spaces, width 2)?
- Line width (default: 160)?
- Quote style for JS/TS (default: double)?
- Semicolons and arrow parens (defaults: always / always)?

Prettier defaults (`.prettierrc`, when accepted, mirrors Biome base):

```json
{
  "useTabs": false,
  "tabWidth": 2,
  "printWidth": 160,
  "singleQuote": false,
  "trailingComma": "none",
  "semi": true,
  "arrowParens": "always"
}
```

### 8. Verify

- [ ] `.githooks/pre-commit` exists and is executable
- [ ] `git config core.hooksPath` prints `.githooks`
- [ ] `prepare` script in package.json sets `core.hooksPath`
- [ ] `.lintstagedrc` exists
- [ ] `biome.json` exists (or pre-existing Biome config found)
- [ ] `prettier` config exists, when Prettier was accepted
- [ ] Run `npx lint-staged` to verify it works

### 9. Commit

Stage only the files this setup created or changed: `.githooks/`, `.lintstagedrc`, the formatter configs, `package.json`, and the lockfile. When other uncommitted changes are present and the branch is the default branch, ask before committing. Commit with a message naming the tools installed, for example `Add git hooks via core.hooksPath (lint-staged + biome)`.

The commit runs through the new pre-commit hook: a good smoke test that everything works.

## Notes

- `core.hooksPath` overrides `.git/hooks/` entirely; hooks in `.git/hooks/` stop running
- The `prepare` script needs a git repository present; `npm install` in a non-git context fails unless guarded (e.g. `prepare": "git rev-parse && git config core.hooksPath .githooks || true"` in published packages)
- Biome `check` runs both format and lint in one pass; `--no-errors-on-unmatched` keeps lint-staged quiet when no supported files are staged
- Prettier handles only what Biome does not, so the two never fight over the same file
- The pre-commit runs lint-staged first (fast, staged-only), then full typecheck and build
- If the team needs more than pre-commit (parallel steps, per-glob runners without lint-staged), suggest lefthook as the next step up; Husky only adds convenience wrappers over what core.hooksPath already does
