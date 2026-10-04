# Handoff: every skill model-invoked, implement-all became divide-and-conquer

Supersedes: [2026-10-04-0152-guidelines-portable-code-conventions.md](2026-10-04-0152-guidelines-portable-code-conventions.md) (different topic; continues the chain)

## State

The work is in the commit that adds this handoff, pushed to `origin/main`. Read the diff for detail (`git show --stat HEAD`). Checks passed before the commit: `python3 scripts/check-skills.py`, `python3 scripts/test-check-skills.py` (16 tests), `claude plugin validate . --strict`.

## What changed and why

1. **No more user-only skills.** The user asked that every skill be reachable by the human, the model, and other skills "without distinction", so a subagent can call `implement`. All 23 former user-invoked skills lost `disable-model-invocation` and the Codex `policy` block, and got model-facing descriptions. Heavy or outward skills trigger only on an explicit user request. Policy now lives in `.agents/invocation.md`, `CLAUDE.md`, and `skills/reference/write-for-agents/SKILL-MECHANICS.md`. READMEs are flat lists; documentation pages were reworded.
2. **`check-skills.py`**: fails when a skill blocks model invocation; replaces the hardcoded retired-name list with "every `Skill tool with "X"` call names a current, non-deprecated skill or an allowlisted external one" (`EXTERNAL_SKILLS = {"webapp-testing"}`); fails when the tiers in `divide-and-conquer/ROUTING.md` drift from `setup-delegation-policy/POLICY.md`.
3. **`implement`** no longer runs `review-and-refactor` (review runs once per batch, by the caller). When a coordinating skill hands it work, the caller owns `work-in-progress.md` and `CHANGELOG.md`. It absorbed the implementation rules that were in `iterate` step 4 (targeted edits, conventions, `debug` before bug fixes, `webapp-testing`). It commits only in a versioned project.
4. **`implement-all` renamed `divide-and-conquer`**: divide (route each task to the least expensive capable tier with effort and reason; the user approves the routing table before dispatch, which is the token-cost safeguard), conquer (implementer subagents call `implement` at their tier; one escalation to the next tier on failure, then blocked), combine (merge, one review). Rules in `skills/workflow/divide-and-conquer/ROUTING.md`.
5. **`iterate`** step 4 now calls `implement` for each batch, or `divide-and-conquer` when a batch splits into independent tasks.

## Decisions settled in conversation (not recorded elsewhere)

- `graphify` keeps its name for now; `divide-and-conquer` was judged a misfit for it (its core rule is "plan, don't do"). Alternatives offered and not chosen: `chart-decisions`, `map-decisions`. A wrapper skill around `graphify` was dropped.
- Suggested follow-up, not done: `graphify` could tell the user to run `/taskify` when its map is finished, and could offer an architecture decision record when a resolved decision passes `model-domain`'s three-part gate.
- An HTML call graph of the skills was rejected as a committed artifact; its useful checks went into `check-skills.py` instead.

## Open risks

- Every description now loads each turn (about 10,300 characters total, up from about 5,700). Claude Code caps the skill listing; if skills stop triggering, check truncation first. The limit was not verified.
- `divide-and-conquer` and the new `iterate` routing are untested by a real run.

## Human steps pending

- Re-run `scripts/link-skills.sh`, then remove installed `implement-all` entries from `~/.claude/skills` and `~/.agents/skills` (the latter holds real directories, not symlinks; the script never deletes).

## Suggested skills

- `skill-creator` (model-invoked): run evals on `divide-and-conquer` and `iterate` to confirm routing and the approval table behave.
- `write-for-agents` (model-invoked): before editing any `SKILL.md`.
- `guide` (model-invoked now): re-sync it after any further skill rename.
