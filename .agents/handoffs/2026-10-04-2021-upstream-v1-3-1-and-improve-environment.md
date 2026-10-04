# Handoff: upstream v1.3.1 synced, and `retro` restored as `improve-environment`

Supersedes: [2026-10-04-1516-missing-skill-dependency-paragraphs.md](2026-10-04-1516-missing-skill-dependency-paragraphs.md) (different topic; continues the chain, and its open risks and pending human steps still stand)

## State

All work is on `origin/main` in four commits: `aea8609` (ancestry merge), `43080ee` (port), `74f8828` (new skill), and the commit adding this handoff. The local branches `sync/upstream-v1.3.1` and `add-improve-environment` are fully merged into `main` and can be deleted. Checks passed before the commits: `python3 scripts/check-skills.py` (48 skills, 48 manifest paths, 48 pages), `python3 scripts/test-check-skills.py` (23 tests), `claude plugin validate . --strict`. `scripts/link-skills.sh` was re-run, so `improve-environment` is linked locally.

## Upstream sync through `24fe0ef` (v1.3.1)

The user asked to rebase onto upstream while keeping every fork skill. Rebasing is ruled out by [architecture decision record 0001](../../documentation/architecture-decision-record/0001-maintain-as-an-independent-fork.md); the established route is an `ours` merge for ancestry plus a separate content port. `main` is now 0 behind `upstream/main`.

Only one upstream commit carried new content, `c5b9869` (route post-bug reflection to `retro`, drop the stale architecture hand-off). The record, inventory, and snapshot are in [.upstream/sync/2026-10-04.md](../../.upstream/sync/2026-10-04.md), [.upstream/sync/2026-10-04.json](../../.upstream/sync/2026-10-04.json), and `.upstream/snapshots/24fe0ef/`. Repeat the same procedure for the next upstream release: fetch, `git merge -s ours upstream/main`, port by reading `git diff <last-tip> upstream/main`, snapshot changed files byte for byte, write a dated sync record and inventory, add a line to `.upstream/README.md`.

## `improve-environment`

Comparing upstream `retro` with `improve-skills` showed the fork had narrowed the retrospective to skill problems (rename in `e5572d5`), dropping six of `retro`'s seven environment categories. The user agreed to restore it as its own skill rather than widen `improve-skills`, matching the memory rule to keep each concern in its owning skill.

Design decisions, read `74f8828` for the full diff:

- Five steps with completion criteria: trace friction, read the environment, find candidates (every friction moment must end with a candidate, a skill finding, or a stated reason), agree with the user, apply.
- Written lessons (navigation pointers, `GUIDELINES.md` rules, conventions) go through `memorize`, which owns their homes; the skill itself builds checks and changes tools and access.
- Hands over to `/setup-git-hooks` when no guardrail exists, and to `/improve-skills` for skill findings; `improve-skills` hands environment findings back.
- `guide`'s `/debug` row now routes "what would have prevented the bug" to it, adopting the part of upstream v1.3.1 the port first declined.

## Open

- The skill has not been run against a real session. The first real run is its test: watch whether step 3 produces generic advice and whether the hand-overs with `improve-skills` duplicate work.
- `CHANGELOG`: this fork keeps none; nothing to update.

## Suggested skills

- `improve-environment` (type `/improve-environment`, or call the Skill tool) to exercise the new skill after a hard session.
- `improve-skills` to report how it behaved.
- `write-for-agents` before editing any `SKILL.md`, `AGENTS.md`, or `CLAUDE.md`.
- `guide` if the routing between the retrospective skills needs rechecking.
