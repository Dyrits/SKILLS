# Skills repository fork rework, session 7: code-review setup fallback

Supersedes: `.agents/handoffs/2026-09-17-1213-experimental-skills.md`

## Current state

The experimental publishing work from the previous handoff was committed and pushed as `363809a` (`Add experimental publish-message and publish-review skills`). This session changed `code-review` so missing repository setup no longer blocks a review. The user requested this handoff, commit, and push after reviewing the result.

## Decisions and completed changes

- Removed the hard dependency on `documentation/agents/issue-tracker.md` from `skills/workflow/code-review/SKILL.md`.
- Specification discovery now uses configured tracker lookup only when the tracker document exists. Without it, discovery continues through a supplied path and local specification files.
- When discovery finds no specification, the skill asks the user to choose among running `/setup-custom-skills`, providing a specification or path, and continuing with the Standards axis alone.
- A Standards-only run skips the Specification subagent and reports `no specification available`.
- Re-synchronised `documentation/workflow/code-review.md` with the changed behaviour.
- Updated `skills/getting-started/what-is-next/SKILL.md` so setup is described as a precondition for tracker-dependent flows rather than every flow. A redundant sentence explaining the `code-review` exception was removed after review with `writing-for-agents`.
- Audited other setup consumers. The user confirmed that the hard setup requirements in `to-specifications`, `to-tickets`, and `triage` are intentional. `wayfinder` already falls back to local Markdown, while `publish-message`, `domain-modeling`, and `wait-what` continue without setup.

## Primary artifacts

- `skills/workflow/code-review/SKILL.md`
- `documentation/workflow/code-review.md`
- `skills/getting-started/what-is-next/SKILL.md`

## Verification

- `git diff --check` passes.
- No manifest changed, so plugin validation was not required.

## What is next

No follow-up work is currently requested. The next session can start from the committed state and respond to a fresh brief.

## Suggested skills

- Call the Skill tool with `take-over` when resuming from this file.
- Call the Skill tool with `writing-for-agents` before editing another skill or router.
