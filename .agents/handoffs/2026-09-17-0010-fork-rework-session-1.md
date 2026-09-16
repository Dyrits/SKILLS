# Skills repo fork rework, session 1

Supersedes: none (the earlier test handoff was deleted by request).

## What was in flight

Full rework of the fork at `git@github.com:Dyrits/SKILLS.git` (origin; `upstream` = mattpocock/skills, fetch-only via invalid push URL). All work is **committed and pushed** as `c31e22b` ("Reorganize skills into new buckets and update plugin manifest") on `main`. Working tree clean. Do not redo any of it; read the commit diff for detail.

## Skills reworked this session (explicit list, do not redo)

| Skill | What happened | Now at |
| --- | --- | --- |
| `what-is-next` (was `ask-matt`) | renamed; description covers boundary options too | `getting-started/` |
| `setup-custom-skills` (was `setup-matt-pocock-skills`) | renamed (rename re-applied after an earlier revert; only the tracker-template changes stayed reverted); "engineering skills" wording → "workflow skills" | `getting-started/` |
| `setup-git-hooks` (was `setup-pre-commit`) | renamed; Husky dropped for `core.hooksPath`; Biome-first + Prettier fallback; typecheck+build gate; user's formatter prefs (width 160, double quotes, semis, no trailing commas, sorted keys/attrs/props) | `getting-started/`, not in plugin |
| `setup-git-guardrails` (was `git-guardrails-claude-code`) | renamed; now multi-agent (Claude hook, OpenCode deny rules, Codex documented + git-level fallback) | `getting-started/`, not in plugin |
| `setup-auto-handoff` | **new**; PreCompact hook gating compaction on a fresh handoff; tested | `getting-started/`, not in plugin |
| `grill-with-docs`, `to-spec`, `to-tickets`, `implement`, `implement-all`, `tdd`, `code-review` | moved bucket (content unchanged unless listed below) | `flow/` |
| `implement-all` (was `implement-spec`) | renamed; promoted out of `in-progress/`; plugin + docs page + router route added | `flow/` |
| `wayfinder`, `research`, `prototype` | moved bucket; `wayfinder` also gained ask-then-fallback-on-missing-tracker | `shaping/` |
| `triage`, `diagnosing-bugs`, `improve-codebase-architecture`, `resolving-merge-conflicts` | moved bucket; `triage` gained ask-before-setup | `upkeep/` |
| `grilling`, `domain-modeling`, `codebase-design`, `writing-for-agents`, `wizard` | moved bucket (content unchanged) | `reference/` |
| `grill-me` | unchanged content; README grouping only | `productivity/` |
| `ask-someone-else` (was `to-questionnaire`) | renamed; output filename convention updated | `productivity/` |
| `wait-what` | answers in the user's language (asks if unclear); STE for English only; no-CONTEXT.md fallback | `productivity/` |
| `handoff` | writes versioned `.agents/handoffs/` files, supersedes chain, gitignore question | `productivity/` |
| `takeover` (was `handon` → considered `resume`/`pickup`) | **new** skill (renamed once before first use) | `productivity/` |
| `teach` | unchanged | `productivity/` |
| `scaffold-exercises` | **deleted** (repo + installed) | gone |
| `claude-handoff` | **deleted** (rejected merge-into-handoff idea) | gone |

Renames all include: folder, frontmatter, `plugin.json`, both READMEs, docs page move, `ask-matt`→`what-is-next` cross-references everywhere, and refreshed symlinks via `scripts/link-skills.sh`.

## Conventions to honour

- Skills sit flat inside buckets, no subfolders; grouping is README headings only
- Docs pages at `documentation/<bucket>/<skill>.md`, URL `aihero.dev/skills-<name>`
- **Before editing any `SKILL.md` / `AGENTS.md` / `CLAUDE.md`: call the Skill tool with `writing-for-agents`** (missed twice early in this session; the user checks)
- No em-dashes in repo prose
- Run `scripts/link-skills.sh` and `claude plugin validate . --strict` after structural changes

## What's next (candidates, user's call)

- Graduate `in-progress/` one by one: `loop-me`, `retro`, `setup-ts-deep-modules`, `writing-beats`, `writing-fragments`, `writing-shape`
- Known unfixed review findings: `flow/implement/SKILL.md` too thin (5 lines); `flow/tdd/SKILL.md:38` says refactoring belongs to review, contradicting red-green-refactor
- Sync with upstream occasionally: `git fetch upstream`, merge or rebase
- Other machines need one `git pull` + `./scripts/link-skills.sh` (many symlinks renamed today)

## Suggested skills

Call the Skill tool for:
- `writing-for-agents` before any skill or agent-doc edit
- `takeover` to resume from this file (newest in `.agents/handoffs/`)
- `what-is-next` for routing questions over the new buckets
