# Handoff: open eval fixes done and re-run; `CLAUDE.md` mentions removed; changes committed on a branch

Supersedes: [2026-10-06-0001-eval-reports-and-fixes-to-schedule.md](2026-10-06-0001-eval-reports-and-fixes-to-schedule.md). Its open items 1 to 5 are done (below). Item 6 (runner-reported ambiguities) and the "still undecided" items are carried over or closed as noted.

## What this session did

1. **Item 1, fixture path.** `skills/workflow/taskify/evals/files/specification.md` now declares `specifications.md`, matching `skills/reference/document/PROJECT-DOCUMENTS.md`.
2. **Item 2, `taskify` (strict, the user's choice).** `skills/workflow/taskify/SKILL.md` now requires each acceptance criterion to be verifiable with only the task's own work and its blockers' results; a criterion needing another task's result moves there or makes that task a blocker. Eval 2 expectation, documentation page updated.
3. **Item 3, `sync-tree` (user chose B).** Eval 8 reworded to the observable (asks for the target, offers `main`, updates nothing). Skill text unchanged.
4. **Item 4, `memorize` (user chose A).** `skills/reference/model-domain/GLOSSARY-FORMAT.md` allows an optional one-line `_Why_` under a glossary entry, only when the user states a reason and the choice is easy to reverse. `model-domain` documentation page updated.
5. **Item 5, `memorize` (user chose A).** Eval 5 now runs the skill twice.
6. **Standing rule from the user: name only `AGENTS.md`, never `CLAUDE.md`.** Filed in `AGENTS.md` (Language and naming). Removed from skills, documentation, evals, and scripts; `setup-ai-workspace` now edits `AGENTS.md` and creates it when missing, with evals and its documentation page rewritten. Kept literal: the global `~/.claude/CLAUDE.md` install path in `setup-delegation-policy`, and historical records (handoffs, `.upstream/`, architecture decision record 0001, the results sections of the earlier evaluation reports). This closes the old "add `@AGENTS.md` to `CLAUDE.md`" question.
7. **Re-ran four evals** (one Sonnet runner each, graded by hand): `taskify` 2 is 3 of 5 met and 2 partial, `sync-tree` 8 is 3 of 3, `memorize` 3 is 6 of 6, `memorize` 5 is 4 of 4. A "Re-run 2026-10-06" section was appended to each of the three reports in `documentation/evaluations/`; they hold the details and caveats.

`scripts/check-skills.py` and `python3 scripts/build-skill-graph.py --check` passed after the edits (`index.html` rebuilt).

## Open work

1. **`taskify` eval 2 partials.** The limit-of-20 and rename-and-delete acceptance appear in both the service task and the browser task, and the frontier is implied rather than named at the presentation stage. Decide whether to loosen the expectation ("exactly one task" versus a service and page split) or tighten the skill, then re-run that eval once.
2. **`setup-ai-workspace` evals not re-run.** Its skill text, evals, and documentation page changed to `AGENTS.md` only (creates it when missing). Re-run at least evals 2 and 3 before trusting them.
3. **Global `~/.claude/CLAUDE.md` path.** Left in `setup-delegation-policy` on purpose: it is a real file on the user's machine. Ask the user whether they want it dropped before changing it.
4. **Runner-reported ambiguities, still unaddressed** (optional): where in `AGENTS.md` the memorize pointer goes and what to report on a no-op second run; `sync-tree` never defines "temporary branch" or "corresponding branch"; whether `rebase`'s report-and-ask step is skipped when the user already chose rebase; whether published issue bodies carry `Blocked by:` lines next to native links.
5. **Description optimizer for `memorize`** (carried over, undecided): not run; use a reduced query set first.

## State to trust and not to trust

- The grader was the same session that edited the skills, and runners read skills by path instead of through the Skill tool. A pass shows the text can be followed, not that it beats the earlier text.
- The `memorize` 3 runner may have copied the new `GLOSSARY-FORMAT.md` example (same term); `memorize` 5's second run was simulated inside one runner.
- Raw runner outputs are in `/tmp/skill-evals/run-2/` and are disposable.
- `claude plugin validate . --strict` was not re-run; no manifest was touched.
- The work was committed on `align-evals-and-agents-md-only`, then fast-forwarded into `main` (`f67c816`) and pushed to `origin/main`. That branch was deleted locally and on `origin`. Branches `add-guidelines-md`, `add-improve-environment`, and `sync/upstream-v1.3.1` still exist and were not checked for merge status.

## Suggested skills

- `skill-creator` (called): re-run an eval.
- `write-for-agents` (called): before editing any `SKILL.md` or its description.
- `memorize` (called): for standing rules the user states, and before writing a script (read `.agents/scripts/INDEX.md` first; `update-references.py` and `stage-eval-run.py` were reused this session).
- `hand-off` (typed by the user): to write the next handoff; `take-over` to resume from this one.
