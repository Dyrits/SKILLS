# Handoff: Refinement workspaces, local tracker, and architecture audit reports

Supersedes: `.agents/handoffs/2026-09-17-1647-address-feedback-skill.md`

Created 2026-09-18 00:28; updated at the user's request after reviewing the refinement workflow.

## Current design

- `.refinement/<issue-key>/` or `.refinement/<feature-slug>/` holds working interviews, exploratory catalogues, playtest notes, draft specifications, and draft tickets. Setup offers this workspace for every tracker, including local markdown.
- `backlog/<feature-slug>/` is the committed local tracker for published issues, specifications, and wayfinder maps. A repository may use both directories. An issue link does not turn a supporting note into a tracker record.
- With refinement enabled, publication requires an explicit request. Publishing to the local tracker resolves ticket identifiers and blocking references, writes the selected records, and links drafts to their authoritative published versions. Supporting notes remain in refinement; material needed to understand published records belongs in version control.
- With direct publication configured, specification and ticket workflows publish to the selected tracker after their review steps.
- `documentation/architecture-audit/architecture-audit-<timestamp>.html` holds architecture audit reports, created lazily, one file per run, opened for the user, and reported with a repository-relative path.

## Changes and review

Setup, its local tracker template, specification and ticket workflows, router, README, and corresponding documentation now describe this model. The local tracker template contains only repository configuration, not setup-process references or migration history. The user asked to keep instructions focused on how the workflow should operate.

The earlier artifact-location commit also updates specification lookup in `code-review` and architecture audit output. Historical handoffs remain records of their sessions.

Review covered drafts versus published local records, source URLs versus local ticket paths, draft versus published status, direct publication, and supporting-document references. `git diff --check` and `claude plugin validate . --strict` passed before the amendment.

## Git boundary

The user explicitly requested updating this handoff, amending the latest commit, and force-pushing with lease on the current branch, `main`, to `origin` (`Dyrits/SKILLS`). The commit being amended is `e3f74e2d65ee031151eefbbdce9f36d337e51683`. Verify actual local and remote state before any follow-up; this document is included in the amendment and cannot record its own final hash.

## Follow-up context

In `/Volumes/APFS-G-DRIVE/Codelab/Roll'em`, the former mixed workspace has been renamed to `backlog/` and references updated. Separating its working material into `.refinement/` remains a follow-up; this skills update does not perform that reorganization.

Use `writing-for-agents` for further skill edits. No new architecture decision record was created. The user authorized committing this handoff.
