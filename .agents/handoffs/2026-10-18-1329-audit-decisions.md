# Handoff: skill audit, remaining decisions

Supersedes: `2026-10-18-1144-audit-fixes.md`
Workspace: Dyrits/SKILLS repository, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Close out the 2026-10-18 skill audit: settle its remaining open items with the user and clear the long-standing follow-ups. Done when the "Still open" line in `AUDIT.md`'s Status section is empty and the follow-ups in Next are done or declined.

## State

- The audit fixes are in commit `0b019dd`; the superseded handoff describes them.
- This session's commit (the one adding this file) applies three user decisions, recorded in the Status section of `AUDIT.md` (verified: file read):
  - `optimize-process` is trimmed to its impact-estimating rules, with its description, both README lines, `agents/openai.yaml`, `apm.yml`, and documentation page updated.
  - `re-explain`, `improve-skills`, and `improve-environment` are kept unchanged.
  - `work-in-tree` writes a `return-destination` file (`key=value` lines for `repository`, `branch`, `base`, `task-branch`) in `git rev-parse --absolute-git-dir` of the task checkout; `sync-tree` reads it as a candidate and verifies it. Verified in a scratch repository that a linked worktree's Git directory is private to it (`.git/worktrees/<name>`). The two skills have not been run end to end on a real task (assumed to work).
- Verified now: `python3 scripts/check-skills.py` passes (42 skills), `python3 scripts/test-check-skills.py` passes, `python3 .agents/scripts/generate-skill-manifests.py --check` reports 43 manifests current.

## Decisions

- Keep `optimize-process` only for what the agent gets wrong unaided (impact estimates); the general process advice was cut as judgement the agent already has.
- Keep the retrospective pair and the worktree pair as separate skills: different audiences and triggers. The worktree link is persisted in a file instead of merging.
- Earlier decisions in the superseded handoff still stand (same-name copies identical, fallbacks over hard stops).

## Next

1. Ask the user before running `scripts/link-skills.sh`, which relinks `~/.claude/skills` and `~/.agents/skills` and likely drops stale links to removed skills (`guide`, the old setup skills, `draft-merge-request`).
2. Bring the three conflict procedures together (`skills/version-control/resolve-merge-conflicts/SKILL.md`, `skills/version-control/rebase/references/resolve.md`, `skills/version-control/sync-tree/references/rebase.md`): give the shared steps one file name so the drift check covers them, and keep the rebase-specific wording in each `SKILL.md`.
3. Try `setup` in a real JavaScript or TypeScript repository and a Python repository.
4. Go through the remaining audit items with the user, each with the audit's reason and a recommendation, then record the answers in `AUDIT.md`'s Status section.

## Open questions

- Trim `illustrate` to its HTML report path and `unslop` to the AI-specific tells? The user decides.
- Make `iterate` a thin router or cut its reference chain? Keep `research`? The user decides.
- The generic "Trim" verdicts in `AUDIT.md` name no specific cut; the user or a reviewer must say what to trim.
- Does the plan to retire `setup-delegation-policy` (architecture decision record 0005) still stand? The user decides.

## Sources

- `AUDIT.md` (Status section) and `AGENTS.md`.
- Commit `0b019dd` and the commit that adds this file.
- `skills/version-control/work-in-tree/SKILL.md`, `skills/version-control/sync-tree/SKILL.md`, `skills/productivity/optimize-process/SKILL.md`.
- `documentation/verification/2026-10-18-audit-fixes.md`.
- `documentation/architecture-decision-record/0005-make-skills-autonomous.md`.
