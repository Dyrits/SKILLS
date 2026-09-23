# Optimize process skill

Supersedes: none. This handoff starts a separate thread from `.agents/handoffs/2026-09-23-1220-unslop-and-documentation-skills.md`.

## Current state

The user asked whether they had a skill like [Anthropic's process-optimization](https://www.skills.sh/anthropics/knowledge-work-plugins/process-optimization), then requested a similar skill called `optimize-process` with lighter impact estimates that account for agent work. The installed `~/.agents/skills/process-optimization/SKILL.md` already matched the linked skill. This session added a repository-owned variant at `skills/productivity/optimize-process/SKILL.md` and linked it into `~/.agents/skills` and `~/.claude/skills`.

The new skill is promoted in `.claude-plugin/plugin.json`. Its supporting metadata, human documentation, README entries, and `what-is-next` route are in the same change set. See the commit diff for their contents.

## Verification

`claude plugin validate . --strict`, `git diff --check`, and direct checks of skill metadata, documentation links, and local symlinks passed. The skill creator's `quick_validate.py` could not run because the system Python lacks `PyYAML`.

The user then asked to commit and push. This handoff and the skill changes are being committed to `main` and pushed to `origin/main` after this file is written. Check `git log` and `git status` for the result.

## Next session

No further implementation is requested. If the user wants to try the skill, use `/optimize-process` on a real recurring workflow and check whether its impact section distinguishes agent runtime, human attention, and waiting time.

## Suggested skills

- Call the Skill tool with `take-over` when resuming from this handoff.
- Call the Skill tool with `optimize-process` if the next task is to analyze a recurring process.
- Call the Skill tool with `writing-for-agents` if revising the skill instructions.
