# Handoff: first evaluation reports written; fixes deliberately not started (token budget)

Supersedes: [2026-10-05-2351-still-open-fixes-and-write-for-agents-install.md](2026-10-05-2351-still-open-fixes-and-write-for-agents-install.md). Its "run the remaining evals" item is done; its two "Still undecided" items are still open (below).

## Why this stops here

The user said the remaining token budget may not cover fixing the findings and re-running the evals in the same session. The session therefore stopped after the evaluation and the reports, and committed and pushed them. **Nothing below "Open work" has been started.** Do not read that as a decision to skip it: the fixes are small, the cost is in the re-runs, so plan the next session around that cost (cheapest order listed below).

## What this session did

1. Ran the behavior evals for `memorize`, `sync-tree`, and `taskify` once each, one Sonnet subagent per eval (19 runs), graded by hand against expectations the runners never saw. Also ran a shuffled selection simulation of the 11 trigger and no-trigger messages: 11 of 11 correct.
2. Wrote one report per skill in `documentation/evaluations/` (`2026-10-05-memorize.md`, `2026-10-05-sync-tree.md`, `2026-10-05-taskify.md`) and the format README there (the user's French template, reworded into English). The reports hold the full results, limits, and reproduction steps; do not duplicate them here.
3. Added `.agents/scripts/stage-eval-run.py` (indexed in `.agents/scripts/INDEX.md`): stages a skill's evals for a run, withholding the expectations from the runner, and writes a grading sheet.
4. Answered the user's question "should we have an evaluation script?": yes for staging only; running and grading need agents. A report-skeleton generator was left for later, until a few more reports show what stays constant.

Totals: `memorize` 13 of 15 applicable expectations (2 of 4 evals fully met), `sync-tree` 32 of 33 (8 of 9), `taskify` 25 of 26 (5 of 6). One run each, no baseline, one model.

## Open work, cheapest first

None of these edits has been made. Each skill change also needs its documentation page and `evals.json` re-synced and `scripts/check-skills.py` plus `python3 scripts/build-skill-graph.py --check` to pass (see `AGENTS.md`).

1. **Fixture mismatch (trivial, no re-run needed).** `skills/workflow/taskify/evals/files/specification.md` declares the path `documentation/capabilities/search/specification.md`, while `skills/reference/document/PROJECT-DOCUMENTS.md` names the file `specifications.md`. Pick one and align the fixture or the convention, and the `taskify` eval prompts that mention it.
2. **`taskify` eval 2 (acceptance claims another task's result).** The limit-of-20 task's criterion (c), "saving works again after a delete", depends on the rename-and-delete task. Decide whether the skill should tell the decomposer to keep each criterion verifiable with only its own task and blockers, or whether the eval expectation is too strict. Re-run that one eval.
3. **`sync-tree` eval 8 (target defaulting).** The skill says to default to the source branch name "only when it identifies the corresponding branch unambiguously" and to ask for a "temporary branch", without defining how a temporary branch is recognized. The eval's premise ("does not exist in the original") is also false for linked worktrees, which share refs. Either define the rule in the skill or reword the expectation to the observable (asks for the target, offers `main`, updates nothing). Re-run that one eval.
4. **`memorize` eval 3 (reason has no home).** `memorize` wants the lesson with its reason; `model-domain`'s glossary holds definitions only and records an architecture decision only for hard-to-reverse choices, so the reason landed nowhere. Decide where a reason goes when the choice is easy to reverse (a note in the glossary entry, an architecture decision record anyway, or drop the "with its reason" expectation for glossary routes). Re-run that eval.
5. **`memorize` eval 5 (idempotence untested).** The eval says running the skill again adds no second copy, but the single-run harness never ran it twice. Either add a second invocation to the runner's brief or drop the expectation.
6. **Runner-reported ambiguities with no expectation behind them** (optional, from the reports): where in `CLAUDE.md` the memorize pointer goes and whether it applies when the lesson goes to another home; `memorize`'s "without `document`, wait" line on routes that never need `document`; whether `sync-tree` skips `rebase`'s report-and-ask step when the user already chose rebase, and `rebase`'s undo advice after the rebased commit is already on `main`; whether published issue bodies carry `Blocked by:` lines next to native links.

Cheapest re-run method: stage only the affected eval, for example `python3 .agents/scripts/stage-eval-run.py /tmp/skill-evals/run-2 skills/workflow/taskify behavior`, and delete the staged folders for evals you do not want to run (the script stages all of one kind). Then follow the Method section of the matching report. Update the report the same day, or write a new dated file; never delete the earlier one.

## Still undecided (carried over)

- Add a one-line `CLAUDE.md` containing `@AGENTS.md`? Claude Code reads `CLAUDE.md`, not `AGENTS.md`, so this repository's instructions are not auto-loaded.
- Run `skill-creator`'s description optimizer for `memorize`? Not run; use a reduced query set first. The selection simulation now gives a small baseline: all three `memorize` trigger messages and both no-trigger messages selected correctly.

## State to trust and not to trust

- Raw runner outputs are in `/tmp/skill-evals/run-1/` and are disposable; the reports are self-contained. Do not depend on that folder.
- The grader was the same session that edited the skills, and the runners read each skill by path instead of through the Skill tool. A pass shows the text can be followed, not that it beats the previous text.
- `claude plugin validate . --strict` was not re-run this session; no manifest was touched.

## Suggested skills

- `skill-creator` (called): run or re-run evals, or the description optimizer.
- `write-for-agents` (called): before editing any `SKILL.md` or its description.
- `memorize` (called): for standing rules the user states, and before writing a script (check `.agents/scripts/INDEX.md` first).
- `improve-skills` (typed by the user): to report skill problems found in use.
- `hand-off` (typed by the user): to write the next handoff; `take-over` to resume from this one.
