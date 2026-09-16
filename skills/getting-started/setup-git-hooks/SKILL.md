---
name: setup-git-hooks
description: Set up versioned git hooks via core.hooksPath (no Husky) with lint-staged (Biome where it applies, Prettier otherwise), plus typecheck and build. Use when user wants to add pre-commit hooks, commit-time formatting/linting/typechecking, or to replace Husky with git's built-in hooks path.
---

# Setup Git Hooks

## What This Sets Up

- **`core.hooksPath`** pointing at a committed `.githooks/` dir (git built-in, no Husky needed)
- **lint-staged** running Biome on supported files and Prettier on the rest
- **Biome** config (if missing)
- **Prettier** config (if missing, for languages Biome does not cover)
- **typecheck** and **build** scripts in the pre-commit hook

Why not Husky: Husky's only job is copying runners into `.git/hooks/`. `git config core.hooksPath .githooks` does the same with zero dependencies. A `prepare` script sets the config on every `npm install`, so teammates are covered on clone.

## Steps

### 1. Detect package manager

Check for `package-lock.json` (npm), `pnpm-lock.yaml` (pnpm), `yarn.lock` (yarn), `bun.lockb` (bun). Use whichever is present. Default to npm if unclear.

### 2. Install dependencies

Install as devDependencies:

```
lint-staged @biomejs/biome prettier
```

If the repo already has `biome` or `prettier`, skip reinstalling that one.

### 3. Create `.githooks/pre-commit`

Write this file and make it executable (`chmod +x .githooks/pre-commit`):

```bash
#!/bin/sh
npx lint-staged
npm run typecheck --if-present
npm run build --if-present
```

**Adapt**: Replace `npm` with detected package manager (`pnpm --if-present` is not supported, so check package.json for the script first and omit the line if missing). Omit `typecheck` or `build` if the repo has no such script in package.json, and tell the user.

### 4. Point git at the hooks dir

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

Merge into existing scripts; if `prepare` already exists, append the `git config` call (e.g. `&&`). Note: if the repo already uses Husky (`.husky/` dir or `prepare: husky`), ask the user whether to migrate off it or keep Husky and stop here.

### 5. Create `.lintstagedrc`

Biome handles format and lint (`check`) for languages it supports. Prettier covers the rest:

```json
{
  "*.{js,jsx,ts,tsx,json,jsonc,css,graphql}": "biome check --write --no-errors-on-unmatched",
  "*.{html,md,mdx,yaml,yml,scss,vue,svelte,astro}": "prettier --write"
}
```

Do not point both tools at the same glob. If the repo uses only Biome-supported languages, omit the Prettier entry (but keep Prettier installed as fallback). If the repo does not want Prettier at all, omit the second entry and tell the user.

### 6. Create `biome.json` and `.prettierrc` (if missing)

Only create a config if none exists (check for `biome.json`, `biome.jsonc`, `.prettierrc`, `.prettierrc.json`, `prettier.config.*`).

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

Prettier defaults (`.prettierrc`, for non-Biome languages only, mirrors Biome base):

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

### 7. Verify

- [ ] `.githooks/pre-commit` exists and is executable
- [ ] `git config core.hooksPath` prints `.githooks`
- [ ] `prepare` script in package.json sets `core.hooksPath`
- [ ] `.lintstagedrc` exists
- [ ] `biome.json` exists (or pre-existing Biome config found)
- [ ] `prettier` config exists (or pre-existing config found)
- [ ] Run `npx lint-staged` to verify it works

### 8. Commit

Stage all changed/created files and commit with message: `Add git hooks via core.hooksPath (lint-staged + biome + prettier)`

This will run through the new pre-commit hook: a good smoke test that everything works.

## Notes

- `core.hooksPath` overrides `.git/hooks/` entirely; hooks in `.git/hooks/` stop running
- The `prepare` script needs a git repo present; `npm install` in a non-git context fails unless guarded (e.g. `prepare": "git rev-parse && git config core.hooksPath .githooks || true"` in published packages)
- Biome `check` runs both format and lint in one pass; `--no-errors-on-unmatched` keeps lint-staged quiet when no supported files are staged
- Prettier handles only what Biome does not, so the two never fight over the same file
- The pre-commit runs lint-staged first (fast, staged-only), then full typecheck and build
- If the team needs more than pre-commit (parallel steps, per-glob runners without lint-staged), suggest lefthook as the next step up; Husky only adds convenience wrappers over what core.hooksPath already does
