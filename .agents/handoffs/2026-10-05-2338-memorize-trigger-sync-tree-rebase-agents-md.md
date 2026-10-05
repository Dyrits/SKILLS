# Handoff: `memorize` triggering, `sync-tree` rebase path, `AGENTS.md` replaces `CLAUDE.md`

Supersedes: [2026-10-05-2331-memorize-evals-and-skill-fixes.md](2026-10-05-2331-memorize-evals-and-skill-fixes.md). Its "Still open" list carries over unchanged, except where noted below.

## What this session did

The user opened with `/take-over` plus four requests; the handoff's own "next steps" (run evals) were set aside in favor of them.

1. **`AGENTS.md` is now the real file; `CLAUDE.md` is deleted.** `AGENTS.md` had been a symlink to `CLAUDE.md`. `scripts/check-skills.py` and `scripts/test-check-skills.py` point at `AGENTS.md`. A new "Writing skills" section links the [Anthropic skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) alongside `write-for-agents`. Claude Code reads `CLAUDE.md`, not `AGENTS.md`, so this repository's instructions are **no longer auto-loaded by Claude Code**. The user was told; a one-line `CLAUDE.md` containing `@AGENTS.md` restores it if wanted. Other documents still say "`AGENTS.md` or `CLAUDE.md`" generically for other projects; that is intentional.
2. **`memorize` triggers earlier.** Diagnosis: the description led with abstract identity and put the cues at the tail; the always-loaded pointer buried the correction trigger at the end of a script paragraph; nothing said to file in the turn the cue arrives. Fixes: the description now opens with the cues ("the moment the user corrects you", "always", "never", "from now on", "remember", scripts and pipelines, a second rebuild) and says to use it even when the harness has its own memory; the pointer now leads with the `memorize` call (changed in `AGENTS.md`, `setup-ai-workspace` `SKILL.md`, and `memorize`'s Pointers section); the Memorize section says to file in that turn, before carrying on. Documentation page re-synced; one new trigger eval (mid-task correction).
3. **`sync-tree` considers rebasing and no longer dead-ends.** It lists `rebase` under **Calls**. On diverged histories it offers: rebase the source onto the target through `rebase` then fast-forward (recommended), replace the target (explicit approval), or stop. "Target ahead of source" is reported as already landed instead of a refusal. A table maps every stop to a state, reason, and next move. Documentation, `index.html`, evals (diverged and target-ahead rewritten; rebase and conflict evals added), and the `conflicting` scenario in `evals/files/setup-scratch.sh` are updated. The conflict scenario was checked by hand: it does produce a rebase conflict.
4. The user's own rename `documentation/evaluation/waza.md` to `documentation/evaluations/waza.md` is committed with everything else.

## Not done

- **No eval was run against a model**, including the new ones. The `memorize` description is a reasoned rewrite, not a measured one.
- The skill-creator description optimizer (`scripts.run_loop`, about 60 `claude -p` calls per iteration, up to 5 iterations) was offered and explained but not run. If run, use a reduced query set first and the session's model.

## Still open

Unchanged from the previous handoff (the list under "Still open" there): `guide`, `classify`, `implement`, `address-feedback`, `specify`, `hand-off`, `ask-someone-else`, `publish-message`, `walk-through`, `model-domain`, `triage`, `divide-and-conquer`, and the `debug` documentation page. Ask the user which to fix.

## Verification commands

```sh
python3 scripts/build-skill-graph.py --check
python3 scripts/check-skills.py
python3 scripts/test-check-skills.py
claude plugin validate . --strict
git diff --check
```

All passed before the commit (32 tests).

## Suggested skills

- `skill-creator` (typed by the user or called): run `memorize`'s and `sync-tree`'s `evals/evals.json`, or the description optimizer for `memorize`.
- `write-for-agents` (read from `skills/reference/write-for-agents/SKILL.md`; it is not exposed to the Skill tool in this session): before editing any `SKILL.md`, description, or pointer.
- `document` (called): when a skill's behavior changes, re-sync its documentation page.
- `memorize` (called): for standing rules the user states.
- `improve-skills` (typed by the user): to report skill problems found in use.
- `hand-off` (typed by the user): to write the next handoff.

## Next session

Likely order: run the evals for `memorize` and `sync-tree` and fix whichever side disagrees; decide whether to run the description optimizer for `memorize`; decide on the `@AGENTS.md` shim for Claude Code; then the "Still open" list.
