# Handoff: security-audit skill import

Supersedes: none
Workspace: Dyrits/SKILLS repository, branch `add-security-audit-skill` (from `main` at `1f7bc18`)

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Land Cloudflare's `security-audit` skill in the collection: merge the branch, then take up the optional follow-ups (evaluations, a way to sync with upstream). Done when the branch is merged and each follow-up is done or declined by the user.

## State

- Commit `da9a115` on `add-security-audit-skill` adds `skills/upkeep/security-audit` and registers it everywhere `AGENTS.md` requires (plugin manifest, `marketplace.json`, root `apm.yml`, both READMEs, `flow.json` and `index.html`, documentation page, Cloudflare's MIT notice in `LICENSE`). Verified: `documentation/verification/2026-10-28-security-audit-import.md` proves C1 to C7, reproduced by a fresh-context agent against `85988ab` (the same content before the proof's reproduction note was amended in).
- The run-location behavior (C8: runs saved in `documentation/security-audit/run-<N>/`, ignored by Git, with an `AGENTS.md` line) is unproven: it needs a full audit run by an agent with the skill loaded.
- `scripts/link-skills.sh` was run; `~/.claude/skills/security-audit` and `~/.agents/skills/security-audit` point into this repository. Verified by `ls -l`.
- `npm run test-detect-harnesses` fails on `main` too: `package.json` names `scripts/test-detect-harnesses.py`, which does not exist. Verified on `1f7bc18`. Not fixed.
- Untracked at the repository root and not part of this branch: `brief.md` (another agent's brief for a new review-history skill, in progress in parallel), `evaluations/upkeep/`, and `evaluations/version-control/` (both predate this session).

## Decisions

- Added because nothing in the collection audits security and the skill ships deterministic validators; placed in `upkeep/` under its upstream name, since no repository rule forces a verb name (user agreed, this session).
- Keep `needs_validation` rather than renaming it `unresolved`: `unresolved` is already a coverage-ledger field, and the value is in the schema, both validators, and earlier runs' files (user asked, this session).
- Runs go to `documentation/security-audit/run-<N>/`, mirroring `documentation/architecture-audit/`, ignored by Git unless the user confirms committing them, and excluded from every sandbox view of the target. This is the one behavior that differs from upstream, which saves outside the repository (user: "Do what you see best to keep consistency"). Recorded on the documentation page's provenance note.
- Import changes only layout and wording otherwise, so an upstream sync can diff against upstream `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`.

## Next

1. Push state: the branch is pushed to `origin`; ask the user whether to open a pull request or merge into `main`.
2. Offer skill evaluations (allowed, not required, per architecture decision record 0008): a trigger case (guidance mode versus full audit) and, if the user accepts the cost of many agents, one small full-audit case that would prove C8. Suites go in `evaluations/upkeep/security-audit/`.
3. Decide with the user whether to record upstream syncing for this skill, for example in the upstream detachment record the skill-upkeep handoff lists as pending.
4. Optionally fix or remove the stale `test-detect-harnesses` script entry in `package.json`.

## Open questions

- Whether the user wants runs committed in some repositories (the skill supports it after confirmation) is per project; nothing to settle now.

## Sources

- Commit `da9a115` and `git diff 1f7bc18..add-security-audit-skill`.
- `documentation/verification/2026-10-28-security-audit-import.md` and its `checks.py`.
- `documentation/skills/upkeep/security-audit.md`.
- Upstream: https://github.com/cloudflare/security-audit-skill at `c1c8a8c1471069fb0e188eeaff69b8e8db6564a8`.
- `.agents/handoffs/2026-10-23-1405-skill-upkeep.md` (the separate upkeep thread).
