Upstream skill: `setup-pre-commit`, adapted here as `setup-git-hooks`. Commit `f85ffd7` replaced Husky with `core.hooksPath`, made formatting Biome-first, and added a typecheck and build gate. The [provenance audit](../../research/2026-10-03-retained-skill-provenance.md) records the original at `d81f3a1:skills/misc/setup-pre-commit/`.

## What it does

Sets up versioned git hooks through `core.hooksPath` pointing at a committed `.githooks/` directory, with no Husky. The pre-commit hook runs lint-staged on staged files, then the project's typecheck and build scripts.

lint-staged assigns Biome to the languages it supports, including those it covers only once enabled, and keeps any formatter the project already uses. Prettier is offered only for the languages left over, and you can decline it. Each glob gets exactly one tool. Husky only copies runners into `.git/hooks/`, which `core.hooksPath` does with no dependency; a `prepare` script sets the config on every install so teammates are covered on clone.

## When to reach for it

Type `/setup-git-hooks`, or an agent can reach for it when you want commit-time formatting, linting, or typechecking, or want to replace Husky.

| Situation | Use |
| --- | --- |
| You want checks on every commit, for people and agents | This skill |
| You want agents to ask before pushing to a protected branch or resetting | [setup-git-guardrails](./setup-git-guardrails.md) |

## Prerequisites

A Node project with a package manager the skill can detect from its lock file (npm, pnpm, yarn, or bun, defaulting to npm).

## What it changes

- Maps every language in the repository to a formatter, then installs lint-staged and Biome, plus Prettier only if you accepted it, skipping any already present.
- Writes `.githooks/pre-commit` and the `prepare` script.
- Writes `.lintstagedrc`, and `biome.json` (and `.prettierrc` when accepted) only when no configuration exists, after asking for formatter preferences.
- Commits only the files it created or changed, and asks first when the default branch holds other uncommitted work.
- Omits typecheck or build lines when the repository has no such script, and tells you.

## Common questions

**My repository already uses Husky.**

Before it installs or writes anything, the skill asks whether to migrate off it or keep Husky and stop.

**Do hooks in `.git/hooks/` still run?**

No. `core.hooksPath` overrides that directory entirely.

**Does `prepare` break installs outside a git repository?**

It can. For published packages, guard it with a `git rev-parse` check.

**What if I need more than pre-commit?**

The skill suggests lefthook as the next step up, for parallel steps or per-glob runners without lint-staged.

## It's working if

- `git config core.hooksPath` prints `.githooks`.
- `npx lint-staged` runs cleanly.
- The skill's own commit runs through the new hook and succeeds.
- A fresh clone gets the hook path after a package install.

## Where it fits

Run-once setup per repository, run on its own request. [setup-git-guardrails](./setup-git-guardrails.md) pairs with it: its optional `pre-push` fallback uses this same hooks path.
