# Handoff: `memorize` improvements, per-skill evals, and the fixes the evals surfaced

Supersedes: [2026-10-05-0725-conventions-rename-and-no-legacy-migration.md](2026-10-05-0725-conventions-rename-and-no-legacy-migration.md) (its commits landed as `c3f3fca` and `db19b1b`).

## What this session did

The user ran `/improve-skills` but asked to work directly instead of opening an issue. Three things followed.

1. **`memorize` fires more often.** Its description is now third person, names concrete cues ("always", "never", "from now on", "remember", before any script or pipeline, a second rebuild), and says what it does. A plain "remember" still routes through it, because the harness memory is one home among several. The always-loaded pointer now carries both halves (script index, plus "call memorize on a correction, a standing rule, or a second rebuild") in the skill's Pointers section, in `setup-ai-workspace`'s block, and in this repository's `CLAUDE.md`. Commit `e9be8d0` (made by the user mid-session) already swept these in.
2. **Best-practices audit** of every skill against the Anthropic skill authoring guide. Fixed: second-person descriptions (`classify`, `resolve-merge-conflicts`), thin descriptions (`write-for-agents`, `prototype`), and a Contents list on the five reference files over 100 lines.
3. **Evals for every skill.** There was no repository convention. Decision, confirmed by the user: evals live **inside each skill** in the `skill-creator` format, `skills/<bucket>/<skill>/evals/evals.json` with fixtures under `evals/files/` (the `files` paths are relative to the skill folder). Convention: [.agents/writing-evals.md](../writing-evals.md). `scripts/check-skills.py` requires and validates them (at least three evals covering `trigger`, `behavior`, `no-trigger`); eval folders are excluded from its link, dependency, and em-dash scans. There are 48 files and about 400 evals, written by six Sonnet subagents. **No eval has been run against a model.**

The user explicitly chose to keep evals scoped per skill. Do **not** write a second set for `claude plugin eval` (it expects plugin-root `evals/<case>/prompt.md` plus `graders/`, a different format that neither tool reads). A generator script was offered and declined for now.

## Skill fixes made because writing evals exposed them

Approved by the user, one by one:

- `setup-ai-workspace` checks for `confirm-dangerous-git.sh` (was `block-dangerous-git.sh`); its documentation now says it calls `setup-delegation-policy` after the user agrees.
- `sync-tree` no longer references `report-landed`.
- `test-first` description says it leaves refactoring to `review-and-refactor`.
- `design-modules` no longer claims "find deepening opportunities" (that is `improve-codebase-architecture`).
- `setup-git-hooks` asks the Husky question in step 1, before installing anything.
- `setup-delegation-policy` removal covers OpenCode, ZCode, and Gemini tier agents.
- `prototype` narrows a whole-application request to one question or tells the user to run `/iterate` (a new hand-over, so its dependency paragraph and `index.html` changed).
- `research` does the work itself when already a subagent.
- `teach` workspace paths are relative to the current directory, never the skill folder.
- `resolve-merge-conflicts` now owns the stop-and-ask path (never `--abort` on its own) and finishes with `git rebase --continue` in a rebase; the override in `rebase/BRANCH.md` is removed.
- Documentation pages re-synced: `walk-through`, `debug`, `improve-codebase-architecture`, `teach`, `research`, `prototype`, `setup-git-hooks`, `setup-delegation-policy`, `setup-ai-workspace`, `resolve-merge-conflicts`.

## Still open

Raised by the eval-writing agents and not fixed (the user chose which to fix; these were left out):

- `guide`: `SKILL.md` never links `PHASE-BOUNDARIES.md`, and its session-boundary table omits the subagent option and the "first yes wins" ordering that file defines.
- `classify`: "negative verdict" is undefined for multi-class label sets; "retry once on 429 or 5xx" does not say once in total or once per failure kind.
- `implement`: calls `webapp-testing` (external, allowed by the checker) without listing it as a dependency in prose; `address-feedback` and `specify` carry no Calls line for skills they name as next steps.
- `hand-off`: no rule for the gitignore question when a prior answer exists.
- `ask-someone-else`: no step for when the user already supplies recipient and need; single-recipient rule only in the documentation.
- `publish-message`: no rule when `.agents/issue-tracker.md` names a different tool than the destination.
- `walk-through`: no explicit stop after scoping to confirm the stage list.
- `model-domain`: `CONVENTIONS-FORMAT.md` asks "create CONVENTIONS.md now?" even on a direct user request.
- `triage`: only "flag and ask" for a task with two conflicting state lines.
- `divide-and-conquer`: no rule for the merge step of a task kept in the coordinating session.
- `setup-ai-workspace` documentation and `SKILL.md` were aligned; the rest of the `debug` page still reads as upstream text.

## Working tree note

At handoff time the tree also held a rename the user made on their own, `documentation/evaluation/waza.md` to `documentation/evaluations/waza.md` (unstaged, not part of this work). Leave it for the user to commit. The user's own commit `e9be8d0` also added `skill-creator` under `.agents/skills/`.

## Verification commands

```sh
python3 scripts/build-skill-graph.py --check
python3 scripts/check-skills.py
python3 scripts/test-check-skills.py
claude plugin validate . --strict
git diff --check
```

All passed at handoff time (32 tests).

## Suggested skills

- `improve-skills` (typed by the user): this session was one. Its issue-opening step was skipped at the user's request.
- `skill-creator` (typed by the user or called): to run the evals. Point it at a skill's `evals/evals.json`; it grades the written expectations and opens its viewer.
- `write-for-agents` (called): before editing any `SKILL.md` or description, for the pointer-wording rules.
- `document` (called): when changing a skill's behavior, re-sync its documentation page; `.agents/writing-documentation.md` holds the template.
- `memorize` (called): for project lessons the next session learns.
- `hand-off` (typed by the user): to write the next handoff.

## Next session

Likely next steps, in order of value: run a few evals with `skill-creator` on the skills changed here (`memorize`, `resolve-merge-conflicts`, `setup-git-hooks`, `prototype`) and fix the skill or the eval where they disagree; then work through the "Still open" list, asking the user which to fix.
