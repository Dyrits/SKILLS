# Handoff: "Still open" skill fixes, `write-for-agents` install fix, `taskify` hand-over

Supersedes: [2026-10-05-2338-memorize-trigger-sync-tree-rebase-agents-md.md](2026-10-05-2338-memorize-trigger-sync-tree-rebase-agents-md.md). Its "Still open" list (carried from the 2331 handoff) is now closed, except the two decisions under "Still undecided".

## Focus for the next session

**Commit and push.** The working tree holds about 46 uncommitted changed files and nothing is committed. Review `git status` and `git diff --stat`, split into sensible commits (suggested below), commit with the attribution line from the session's reminder, then push `main` to `origin`. The user typed "commit and push" as this handoff's argument; they did not yet approve a push in the conversation, so confirm the commit split and the push once before running them.

## What this session did

1. **`guide`**: `SKILL.md` now links `PHASE-BOUNDARIES.md`, says the decision belongs only at a phase boundary, works the table "first row that fits wins", and has the missing **Subagent** row. Documentation page and one eval updated.
2. **`write-for-agents` was not installed** because its unquoted `description` held `: `, which is invalid YAML, so installers skipped it. `memorize` had the same flaw. Both descriptions are now quoted. `scripts/check-skills.py` gained `frontmatter_error` (flags an unquoted description containing `: ` or ` #`), with a test in `scripts/test-check-skills.py`. A missing description is deliberately not flagged, because the test fixtures omit it. `memorize` lists `write-for-agents` under **Calls**, so it was affected too.
3. **Eleven "Still open" items fixed**, each with its documentation page and one new behavior eval:
   - `classify`: negative verdict defined (caller names the discard labels; ask when more than two labels); retry at most once in total.
   - `implement`: `webapp-testing` marked external, with a fallback when missing. Introduced in commit `56013c1` (moved there from `iterate`).
   - `specify`: closes by telling the user to run `/taskify`, `/implement`, or `/iterate`; "Hands over to" paragraph added.
   - `address-feedback`: calls `implement` for repository code, telling it this run owns the records and the review.
   - `hand-off`: follows an existing gitignore, tracked-handoff, or AGENTS.md answer; asks only when none exists.
   - `ask-someone-else`: confirms a supplied recipient and need in one line; one questionnaire per person.
   - `publish-message`: a tracker file naming another tool does not cover the destination.
   - `walk-through`: stops for the user's confirmation of the stage list before step 2.
   - `model-domain` (`CONVENTIONS-FORMAT.md`): a direct request skips the offer and overrides a recorded decline.
   - `triage`: conflicting states are shown with source and date, a recommendation is made, no role applied until the maintainer picks.
   - `divide-and-conquer`: a task kept in the coordinating session is built on its own branch and merged only after verification passes.
   - `debug`: SKILL.md gained the rule "a reproduction does not authorize changing agreed behavior" and "ADRs" became "architecture decision records"; the documentation page was rewritten to drop upstream issue commentary and to state the Redact behavior correctly.
4. **`taskify` hand-over** (the user asked after seeing nothing pointed at `divide-and-conquer`): `taskify` now closes by telling the user to run `/implement` (one task) or `/divide-and-conquer` (the whole graph); "Hands over to" paragraph, documentation answer, and eval added. `implement` does not call `divide-and-conquer`; only `guide` and `iterate` name it.
5. `index.html` regenerated with `python3 scripts/build-skill-graph.py`.

## Verification

Run before committing:

```sh
python3 scripts/build-skill-graph.py --check
python3 scripts/check-skills.py
python3 scripts/test-check-skills.py
claude plugin validate . --strict
git diff --check
```

All passed at the end of this session (33 tests), except `claude plugin validate` was last run before the `taskify` change and no manifest was touched since.

**Evals were run once, as dry runs.** The `skill-creator` method was used loosely: one Sonnet subagent per skill ran the newest behavior eval against the updated `SKILL.md` (guide, classify, implement, specify, address-feedback, hand-off, ask-someone-else, publish-message, walk-through, model-domain, triage, divide-and-conquer). All 12 met every expectation, graded by hand. No baseline against the old versions, one run each, so it shows the new text can be followed, not that it beats the old. Outputs sit in `/tmp/skill-evals/iteration-1/` (disposable). The `taskify` eval and the earlier `memorize` and `sync-tree` evals have not been run.

## Suggested commit split

1. Frontmatter fix: `skills/reference/write-for-agents/SKILL.md`, `skills/reference/memorize/SKILL.md`, `scripts/check-skills.py`, `scripts/test-check-skills.py`.
2. `guide` session-boundary fix (SKILL.md, page, eval).
3. The eleven skill fixes plus the `taskify` hand-over (SKILL.md, `CONVENTIONS-FORMAT.md`, pages, evals).
4. `index.html` with the skill map, plus this handoff (handoffs are tracked in this repository, so no gitignore question).

Splitting by file is easy except `index.html`, which covers all skill changes; put it with the last skill commit or its own.

## Still undecided

- Add a one-line `CLAUDE.md` containing `@AGENTS.md`? Claude Code reads `CLAUDE.md`, not `AGENTS.md`, so this repository's instructions are not auto-loaded.
- Run `skill-creator`'s description optimizer for `memorize`? Not run; use a reduced query set first and the session's model.

## Suggested skills

- `skill-creator` (typed by the user or called): run the remaining evals (`taskify`, `memorize`, `sync-tree`) or the description optimizer.
- `write-for-agents` (read from `skills/reference/write-for-agents/SKILL.md`; after the frontmatter fix and a reinstall it should be exposed to the Skill tool): before editing any `SKILL.md` or description. Re-run `scripts/link-skills.sh` if it is still missing locally.
- `memorize` (called): for standing rules the user states.
- `improve-skills` (typed by the user): to report skill problems found in use.
- `hand-off` (typed by the user): to write the next handoff.
