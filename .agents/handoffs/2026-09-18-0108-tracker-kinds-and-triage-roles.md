# Handoff: Two tracker kinds, always-on refinement, four triage roles

Supersedes: `.agents/handoffs/2026-09-18-0028-artifact-locations-rename.md`

Created 2026-09-18 01:08. Session goal: make `setup-custom-skills` simple and clear, and re-sync everything that reads it.

## Decisions made this session

All four were the user's calls, taken through explicit questions:

1. **Tracker is one question with two kinds.** Local markdown under `backlog/`, or a remote (GitHub, GitLab, Jira, other). The four seed templates stayed as separate files; only the skill prose collapsed.
2. **Refinement is always on, no longer a setup question.** Every repository drafts in `.refinement/` and publishes only on an explicit request, whatever its tracker. A remote tracker's own refinement or analysis status does not replace the local workspace.
3. **Four state roles instead of five**, with two renamed: `to-evaluate`, `on-hold`, `ready`, `not-planned`. Categories `bug` / `enhancement` unchanged. `on-hold` deliberately absorbs the upstream `needs-info` plus the blocked and deferred states users kept requesting; the hold is named in the triage notes so a later session can check whether it lifted. `ready` replaces the `ready-for-agent` / `ready-for-human` pair, because nothing in the repository ever queried the distinction: the delegability reason now lives in the agent brief.
4. **Lifecycle phases stay out of the role set.** The four roles answer "is this actionable" only. In progress, in review, and deployed belong to the tracker's own status field, a branch, or a pull request.

Rejected on the way, with reasons recorded in this session: renaming `bug` to `fix` (user kept `bug`), a full phase axis maintained by every skill (duplicates native status fields and drifts), and a terminal `implemented` role.

## What changed

See the commit diff rather than a file list here. The shape of it:

- New seed `skills/getting-started/setup-custom-skills/refinement.md`, appended to whichever tracker template setup writes. It is the single source of truth for the refinement workspace and the publication boundary; the duplicate section inside the Jira template is gone.
- `triage-labels.md` renamed to `triage-roles.md`, in the skill folder and as the generated `documentation/agents/triage-roles.md`. The old name contradicted its content: on a local tracker the roles are `Category:` and `Status:` lines, not labels.
- `issue-tracker-local.md` gained a `Category:` line, and wayfinder's claim state moved from `Status:` to `Progress:` because both vocabularies were colliding on one line.
- Consumer skills (`to-tickets`, `to-specifications`, `what-is-next`) lost their "when refinement is configured" conditionals.
- Documentation pages re-synced for `setup-custom-skills`, `triage`, `to-specifications`, `to-tickets`, `what-is-next`, plus both README listings.

Two pre-existing defects fixed while passing through: the triage documentation page said `.out-of-scope/` where the skill says `documentation/out-of-scope/`, and it named the upstream author, which `.agents/writing-documentation.md` forbids.

## Verification done

`claude plugin validate . --strict` passes. Checked for em-dashes and the abbreviations `repo`, `docs`, `spec`, `ADR` in added lines: none introduced. Grepped for every old role string across `skills/`, `documentation/`, and `README.md`; the only survivors are deliberate historical references to upstream naming in `documentation/upkeep/triage.md` and the untouched `.upstream/` archive.

## Open items for a next session

- No repository in the wild has been migrated. A repository set up before this session still has `documentation/agents/triage-labels.md` and the five old role strings; re-running `/setup-custom-skills` is the migration path, and nothing warns the user about that.
- `skills/upkeep/triage/AGENT-BRIEF.md` still opens its examples in GitHub terms in places. It works, but it is the least tracker-neutral file left in the triage skill.
- `ADR` as an abbreviation survives in several skills outside this session's scope, against the rule in `CLAUDE.md`.

## Suggested skills

- `/writing-for-agents` before editing any `SKILL.md` or documentation page here.
- `/code-review` against this session's commit if a second opinion on the diff is wanted.
- `/setup-custom-skills` to exercise the new flow end to end in a scratch repository, which is the one thing this session did not do.

## Git boundary

The user asked for a commit and a push at the end of this session. Verify actual local and remote state before any follow-up: this document is part of the commit and cannot record its own hash.
