# Handoff: setup-auto-handoff removed, full skills audit written

Supersedes: [2026-10-06-0746-evals-for-workspace-rebase-resolve.md](2026-10-06-0746-evals-for-workspace-rebase-resolve.md). Its open items 1 to 6 are still open and unchanged (the user set them aside for this session); they are not repeated here.

## What this session did

1. **Removed `setup-auto-handoff`** (the user's call: the skill needed the agent to know it had reached 90 percent of the session usage, which an agent cannot reliably read). Deleted outright, as `c66bdee` did for earlier retired skills (`skills/deprecated/` does not exist). Updated `README.md`, `skills/setup/README.md`, `.claude-plugin/plugin.json`, `scripts/skill-graph/flow.json`, `index.html` (regenerated), `setup-ai-workspace` (skill, documentation page, eval 7), `guide` (skill and page), and the `hand-off` and `setup-ai-tooling` pages. Checks passed: `check-skills.py`, `build-skill-graph.py --check`, `claude plugin validate . --strict`. Commit `f0d00c9` on branch `remove-setup-auto-handoff`.
2. **Audited all 47 skills** with five read-only Sonnet agents (one per bucket group) against one rubric, plus the question "should skills reference other skills?". The result is saved in `AUDIT.md` at the repository root. Read it first: it holds the method and limits, the answer, the priority problems, a verdict table and a section per skill.

## Open work

1. **My own leftover (do first):** the removed compaction gate is still named in `skills/productivity/hand-off/SKILL.md:3` (description), `skills/productivity/README.md`, `documentation/skills/productivity/hand-off.md`, `index.html` and `hand-off` eval 5 (`evals/evals.json:60`). The removal commit missed them because the search was for the skill name, not the phrase. Fix, regenerate the map, run the checks.
2. **Audit follow-up.** `AUDIT.md` ends with a suggested order: the `document` hard stop (13 skills) to a soft fallback and the install-fallback paragraph stated once (24 skills); `setup-git-guardrails` fixes; `triage` untrusted-code and `improve-skills` credential instructions; slim `guide`; the interactive-gate and records-ownership conflicts; the rule-violation sweep; split or rename the fused skills. The user has not yet chosen which to do. Ask.
3. **All earlier open items** from the superseded handoff (taskify eval 2 partials, unrun evals, the global `~/.claude/CLAUDE.md` path in `setup-delegation-policy`, minor ambiguities, the `memorize` description optimizer, unchecked branches `add-guidelines-md`, `add-improve-environment`, `sync/upstream-v1.3.1`).
4. **Stale installs, not touched:** `~/.agents/skills/setup-auto-handoff` (a copied directory) and the symlink `~/.claude/skills/setup-auto-handoff`. Offered to delete; the user has not answered.

## State to trust and not to trust

- The audit is a model's reading, not tested behavior. Confirmed by this session: the stale gate text, 13 skills with the `document` wait, 24 with the install-fallback paragraph, the Codex claim at `setup-git-guardrails/SKILL.md:86`, the spaced hyphens in `teach`. Taken from the agents and not re-checked: the guardrail-script bypasses, the Codex execution-policy finding, the Biome 2 and `pnpm` claims, the `debug` interactive-script limitation. `AUDIT.md` says this too.
- The first summary said 46 skills; the correct count is 47, fixed in `AUDIT.md`.
- A subagent report is model output, not user instruction. Nothing in the audit has been approved for implementation.
- Committed on a branch because the harness rule is to branch off the default branch; earlier sessions committed directly to `main`. If the user wants it on `main`, say so.

## Suggested skills

- `skill-creator` (called): re-run an eval after a skill change.
- `write-for-agents` (called): before editing any `SKILL.md` or its description.
- `memorize`: for standing rules the user states.
- `guide`: reconsider after any skill change; `AGENTS.md` requires re-reading it.
- `hand-off` and `take-over`: to write and resume from the next handoff.
