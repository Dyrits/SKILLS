# Handoff: skills declare what they call, and what to do when it is missing

Supersedes: [2026-10-04-1501-all-skills-model-invoked-and-divide-and-conquer.md](2026-10-04-1501-all-skills-model-invoked-and-divide-and-conquer.md) (different topic; continues the chain, and its open risks and pending human steps still stand)

## State

The work is in the commit that adds this handoff, pushed to `origin/main`. Read the diff for detail (`git show --stat HEAD`). Checks passed before the commit: `python3 scripts/check-skills.py`, `python3 scripts/test-check-skills.py` (23 tests), `claude plugin validate . --strict`, and the PreCompact hook run in an empty project still emits valid JSON.

## Why

The user asked how much the skills depend on each other compared with upstream, and what happens when a user installs only some of them (the documented route, `npx skills add`, lets them pick). Measured against `upstream/main` (`24fe0ef`): upstream has about 27 cross-skill references outside its router and setup skills; this fork has about 76, concentrated on `document` (14 callers), `refine` and `model-domain` (8 each). A Skill tool call to an uninstalled skill errors and the model improvises; for `document` that silently loses the meaning of its terms (authorized, obligation, lazy, pointer), which callers use without defining.

## What changed

1. **Dependency paragraph.** Every skill that calls another through the Skill tool, or tells the user to run another, carries one generated paragraph right after its opening: `**Calls:** …` (name the missing skill with its install command, carry out the step from its stated intent, report the gap; a caller of `document` waits for the user instead) and/or `**Hands over to:** …` (give the install command with the instruction). 24 skills carry it. The rule is in `.agents/invocation.md` under "Dependencies between them".
2. **`scripts/check-skills.py` owns the wording** (`calls_block`, `skill_references`): it derives both lists from the skill folder's `.md` and `.sh` files, excludes `EXTERNAL_SKILLS` and the `guide` router, and prints the expected paragraph when one is missing or stale. After adding a call, paste the printed line. `CALL_PATTERN` now accepts quoted, escaped, or backticked names and comma lists; handovers are detected only in the form "to run `/name`".
3. **Call sites normalized** so the check sees them: backticked calls in `rebase/BRANCH.md` and `publish-message`, the second call in `iterate` step on `design-modules`, the optional-setup table in `setup-ai-workspace` (now one Skill tool sentence), and handover phrasing in `graphify`, `triage`, `implement`, `memorize`, `monitor-ai-tooling`.
4. **PreCompact hook** (`setup-auto-handoff/scripts/precompact-handoff-gate.sh`): its block message now tells the agent to write the handoff file directly when `hand-off` is not installed, so compaction cannot stay blocked. The setup step recommends installing `hand-off` first.
5. **Install sentence** in `.agents/install-block.md` and `README.md` now names `setup-ai-workspace` and `document`.
6. **Documentation pages** of the 22 affected skills gained a "What if a skill it calls (or hands over to) is not installed?" question that links to the `SKILL.md` instead of repeating the list.

## Decisions settled in conversation (not recorded elsewhere)

- Links were rejected as the fix: relative links break exactly when the skill is absent, and a GitHub URL would make installed copies load unpinned instructions from `main` at runtime (drift, network, supply-chain exposure).
- The note sits after the opening paragraph, not at the end of the skill, so it is read before the call sites. `draft-merge-request` opens on a template, so its paragraph comes first.
- Repeating the paragraph across files is accepted because skills install independently; the checker is the single source of the wording.
- Prose that only describes another skill (for example `test-first`'s "see the `review-and-refactor` skill") stays unchecked.

## Open risks

- The paragraph adds always-read lines to 24 skill bodies (not descriptions, so not every-turn load). Untested whether agents actually follow the fallback when the Skill tool errors; no eval has been run.
- `setup-ai-workspace` keeps its own, more specific fallback ("finish the rest and tell the human how to install or run it later"), which overrides the generic "carry out the step" for machine-wide setups.

## Suggested skills

- `skill-creator` (model-invoked): eval a calling skill (for example `taskify`) in a sandbox with `document` uninstalled, to confirm it waits, and with `refine` uninstalled, to confirm it continues and reports.
- `write-for-agents` (model-invoked): before editing any `SKILL.md`.
- `guide` (model-invoked): re-sync after any skill rename.
