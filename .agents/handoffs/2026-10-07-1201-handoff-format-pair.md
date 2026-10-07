# Handoff: hand-off and take-over share one handoff format

Supersedes: none
Workspace: SKILLS repository, branch `main`

## Goal

Run the evaluations of the reworked `hand-off` and `take-over` skills and write one report per skill in `documentation/evaluations/`. Done looks like `documentation/evaluations/2026-10-07-hand-off.md` and `2026-10-07-take-over.md` (or the run date) in the format `documentation/evaluations/README.md` defines, with results as numerators over denominators.

## State

- The rework is in the commit that adds this handoff. It adds `HANDOFF-FORMAT.md`, identical in `skills/productivity/hand-off/` and `skills/productivity/take-over/`, and rewrites both `SKILL.md` files, their evals, the eval fixtures, both documentation pages, and a `Status (2026-10-07)` line under each skill in `AUDIT.md` (verified: `python3 scripts/check-skills.py` and `claude plugin validate . --strict` pass).
- `scripts/check-skills.py` fails when the two `HANDOFF-FORMAT.md` copies differ (verified: altered one copy, saw the error, restored it).
- No eval has been run against the new text. The behavior change is an editorial judgment so far.
- The installed copies under `~/.agents/skills/hand-off` and `~/.agents/skills/take-over` are real directories, not symlinks into this repository, so they still hold the old text (verified: `ls -la`; loading `hand-off` through the harness returned the old version). This handoff was written by following the repository's new `SKILL.md` by hand. `~/.agents/skills/setup-auto-handoff`, a removed skill, is also still installed there. `scripts/link-skills.sh` was not re-run, and whether it replaces real directories is not checked (assumed: it may not).

## Decisions

- Keep two skills; a merged `relay` skill that guesses the direction was rejected (recorded in `AUDIT.md`, `hand-off` status line): the two run in different sessions, and explicit names beat a guessed mode.
- The format lives in a file shipped identically in both skills, because each skill can be installed alone; a check keeps the copies equal, following the existing delegation-tier precedent in `scripts/check-skills.py`.
- Handoffs name no skills for the next agent: the user wants both skills autonomous from the rest of the collection and usable in any harness.
- Claims in State are marked verified (with how) or assumed, so `take-over` knows which to check against Sources.
- Threads: `Supersedes:` takes a filename, `none`, or `none (forked from <file>)`. `take-over` asks which thread to resume when the newest handoff does not supersede the second newest, unless a path or topic is passed.
- The local-or-shared question in `hand-off` is kept: it is asked once per repository.

## Next

1. Optionally re-run `scripts/link-skills.sh`, or ask the user to, so the installed skills match the repository; check that it replaces the stale real directories.
2. Stage each skill with `python3 .agents/scripts/stage-eval-run.py <workspace> skills/productivity/<skill> behavior trigger` in a scratch workspace outside the repository.
3. Run `hand-off` evals 2 to 6 and `take-over` evals 1 to 5, 8 and 9 with Sonnet subagents that read the skill by path and never see the expectations; grade by hand from the grading sheet.
4. Write the two reports per `documentation/evaluations/README.md`, following `documentation/evaluations/2026-10-06-rebase.md` as the model. State that the no-trigger evals (hand-off 7 and 8, take-over 6 and 7) were not run, and why.
5. Fix a skill, not an eval, when a run shows the skill text is at fault; fix the eval when its prompt or fixture is the defect, and say which in the report.

## Open questions

- Should the no-trigger evals be run at all, given that subagents told to use a skill cannot fairly test routing? The user has not said.
- Should `link-skills.sh` remove stale installed copies of removed skills? Not discussed.

## Sources

- `skills/productivity/hand-off/SKILL.md`, `skills/productivity/take-over/SKILL.md`, `skills/productivity/hand-off/HANDOFF-FORMAT.md`
- `skills/productivity/hand-off/evals/evals.json`, `skills/productivity/take-over/evals/evals.json`, fixtures under each `evals/files/`
- `AUDIT.md`, sections `### hand-off` and `### take-over`
- `documentation/evaluations/README.md`, `documentation/maintenance/writing-evaluations.md`
- `.agents/scripts/INDEX.md` (`stage-eval-run.py`)
