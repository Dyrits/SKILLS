# Handoff: setup-ai-workspace offers every getting-started setup

Supersedes: [2026-10-03-2345-promote-all-skills.md](./2026-10-03-2345-promote-all-skills.md)

## Context

The user asked whether `setup-ai-workspace` still exists and whether today's commits aligned it with the new `documentation/` structure. Verified: it exists, is promoted, and its `SKILL.md` and templates match `skills/reference/document/PROJECT-DOCUMENTS.md`. The only stale term was "Wayfinder labels" in its documentation page (fixed).

The user then asked that the skill offer all `skills/getting-started/` setups, not just tooling.

## What changed

See the commit that adds this handoff for the full diff. In short:

- `skills/getting-started/setup-ai-workspace/SKILL.md`: section 4 is now "Optional setup", one multi-select question over `setup-ai-tooling`, `setup-git-hooks`, `setup-git-guardrails`, `setup-auto-handoff` (called through the Skill tool), and `setup-delegation-policy` (user-invoked and machine-wide, so the human is told to run it). A table gives the "already present" signal for each. Explore and Done steps and the description were updated to match.
- Synced: top-level `README.md`, `skills/getting-started/README.md`, `guide/SKILL.md` routing line, the setup-ai-workspace documentation page (new "Optional setups" section), and "Where it fits" on the four sibling setup pages.
- `scripts/check-skills.py` and `scripts/test-check-skills.py` pass.

## Open points

- The skill has not been exercised end to end on a real repository; the "present when" signals in the section 4 table are inferred from each setup skill's `SKILL.md` and may need tuning.
- `documentation/skills/getting-started/guide.md` line 15 still mentions only `setup-ai-tooling` as an optional stage; acceptable but could list the others.

## Suggested skills

- `write-for-agents` (model-invoked): when editing any `SKILL.md`.
- `document` (model-invoked): when touching project-document rules.
- `unslop` (model-invoked): prose passes on documentation pages.
- `/setup-ai-workspace` (user-invoked): for the human to trial the new optional stage on a sample repository.
- `/guide` (user-invoked): for the human to check the router reads correctly.
