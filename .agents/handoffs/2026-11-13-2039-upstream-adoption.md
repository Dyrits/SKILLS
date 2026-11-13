# Handoff: selective upstream adoption

Supersedes: none (forked from `2026-11-07-1723-skill-upkeep.md`)
Workspace: Dyrits/SKILLS repository, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Adopt useful upstream material without adding overlapping entrypoints or restoring sibling-skill dependencies. The approved factory-design references and tracker fixes are implemented; future upstream reviews must distinguish this selective port from adoption of the entire upstream interval.

## State

- Verified by Git history and source comparison: the previous port was `4dc4f3e`, through upstream `5beb35b`. This session compared `5beb35b..5863806` on `upstream/main`, nine commits, rather than merging upstream content.
- Verified by reading the files: `architect` has one conditional pointer to `references/unattended-agents.md`, which links to `unattended-agents-services.md`. Both references identify upstream `software-factory` at `5863806`; the human-facing page records their provenance and scope.
- Verified by the diff: `setup` now has the reachable-repository check, GitHub destination check, separate closing comment, native dependency commands and open-blocker count, separate pull-request body and comments reads, corrected GitLab JSON output flag, and linked GitLab decision tasks with their frontier query. Its documentation page describes the changes.
- Verified this turn: `python3 scripts/build-skill-graph.py`, `python3 scripts/check-skills.py`, `python3 .agents/scripts/generate-skill-manifests.py --check`, `python3 scripts/test-check-skills.py` (39 tests), `node scripts/sync-plugin-version.mjs --check`, and `git diff --check` passed. The graph generator reported writing `index.html`; inspect the final commit to see whether its content changed.
- Not verified: live tracker writes, vendor claims in the service orientation, and behavioral evaluations of the new references. No live issues were created or changed. Plugin validation was not run; neither plugin manifest changed.
- Verified by `git worktree list --porcelain` and `git rev-parse`: the attached workspace is the original repository checkout on `main`, not a separate linked worktree or isolated clone. No local transfer is needed. The user authorized committing and pushing this change to `origin/main`; publication was pending when this handoff was written. Verify its final commit and remote status before describing it as published.
- The earlier skill-upkeep handoff remains authoritative for unrelated evaluation and maintenance follow-ups; this handoff does not supersede them.

## Decisions

- Extend `architect` through conditional references rather than add a standalone factory-design skill, because the work belongs to system architecture.
- Leave `chief-of-staff` out. Its current implementation overlaps existing coordination and memory behavior and requires sibling skills.
- Keep product names as orientation, with current options researched before use. No claim of verified current vendor capabilities or measured behavioral improvement is supported.
- Leave upstream's legacy glossary migration out. No legacy migration was authorized.
- Do not apply fresh context indiscriminately to follow-up verification: this fork intentionally reuses reviewers. The broader upstream delegation changes were not ported.
- This is a selective port, not an ancestry merge or an adoption marker for every change through `5863806`.

## Next

1. Confirm the next requested scope. The implementation above is complete; the unverified behavior checks are possible follow-ups, not permission to start them.
2. If asked to validate the port, exercise the unattended-agent design branch and tracker recipes without creating remote records unless separately authorized.
3. For a later upstream review, use `5863806` as this review's tip while retaining the exclusions above. Assess fresh-context delegation separately and preserve reviewer reuse for verification.

## Open questions

None blocking the approved port. Whether to run behavioral evaluations or adopt more delegation changes remains for the user to decide.

## Sources

- `.agents/handoffs/2026-11-07-1723-skill-upkeep.md`
- Commit `4dc4f3e` and `git diff 5beb35b 5863806 -- skills/`
- https://github.com/mattpocock/skills/tree/5863806/skills/in-progress/software-factory
- `skills/workflow/architect/SKILL.md` and its two `references/unattended-agents*.md` files
- `skills/upkeep/setup/assets/issue-tracker-github.md`
- `skills/upkeep/setup/assets/issue-tracker-gitlab.md`
- `skills/upkeep/setup/references/workspace.md`
- `documentation/skills/workflow/architect.md`
- `documentation/skills/upkeep/setup.md`
- `documentation/architecture-decision-record/0005-make-skills-autonomous.md`
