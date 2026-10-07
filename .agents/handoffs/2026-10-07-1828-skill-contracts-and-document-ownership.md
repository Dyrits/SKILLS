# Handoff: skill contracts and document ownership

Supersedes: `2026-10-07-1752-skill-contracts-and-document-ownership.md`
Workspace: Dyrits/SKILLS, branch `main`

## Goal

Every skill is complete for its own job, calls others for theirs, and knows them only by contract; every shared document has one owner (`document`). Done when the two remaining leaks below are closed and the changed skills have been run against their evals.

## State

- Since the superseded handoff, all of the following is committed and pushed on `main` in one commit after `1b7c842`, made right after this file was written (verified by the commit and push output at the end of the session).
- `python3 scripts/check-skills.py` passes on 48 skills, `python3 .agents/scripts/generate-skill-manifests.py --check` reports 30 manifests current, and `claude plugin validate . --strict` passes (verified, run just before writing this file).
- `python3 scripts/test-check-skills.py`: 37 tests, one failure, `test_linker_includes_every_bucket`, a macOS `/private/var` path mismatch that also fails at earlier commits (verified, run just before writing this file).
- Changes since `1b7c842`, verified by reading the files after editing:
  - `skills/reference/codify/SKILL.md` no longer describes `document`'s internals: it hands each confirmed rule to `document`, which files or routes it, and its audit asks `document` to check the conventions file. `skills/reference/document/CONVENTIONS-FORMAT.md` regained a "Checking an existing file" section.
  - `.agents/domain.md` is retired: `skills/setup/setup-ai-workspace/domain.md` is deleted, `setup-ai-workspace` no longer writes it or its `AGENTS.md` block, and `codify` keeps no record of a declined offer. A missing `documentation/conventions.md` means `codify` offers again; with no user to ask (a subagent), it returns and reports the conventions as missing.
  - `document`'s `AGENTS.md` pointer now also says to use the glossary's terms and respect the decision records.
  - Conventions are called project-agnostic everywhere (defined in `skills/reference/document/CONVENTIONS-FORMAT.md`), and `scripts/skill-graph/flow.json` has a separate `conventions` artifact instead of filing them under domain records.
  - `codify` evals 2, 4, and 5 and `setup-ai-workspace` evals 2, 3, and 6 match the no-memory behavior; the `declined` fixture is removed.
  - `AUDIT.md`'s follow-up records `.agents/domain.md` as retired.
- No eval was run; every skill change is an editorial judgment (assumed sound, not verified).
- Stale installed copies of `refine` and `model-domain` remain in `~/.agents/skills/`, linked from `~/.claude/skills/`, outside the repository; left for the user (assumed unchanged since the superseded handoff).

## Decisions

- A declined conventions offer is not remembered: the user prefers being asked again over a state file. Recorded in `skills/reference/codify/SKILL.md`.
- Conventions are project-agnostic: they apply to the project and could be transposed to another project on the same stack, tied to no product or domain. Recorded in `skills/reference/document/CONVENTIONS-FORMAT.md`; the stack qualifier was kept deliberately and the user was told.
- `codify` names `document` and the outcome it wants, never what `document`'s format files contain, per `documentation/architecture-decision-record/0004-skills-know-each-other-only-by-contract.md`.
- A folder is created with its first document; when `document` first creates `documentation/`, it adds its `AGENTS.md` pointer and, only if the root `README.md` already lists the project's documentation, one link there. No `documentation/README.md` index. Recorded in `skills/reference/document/SKILL.md`.
- Earlier decisions in the superseded handoff still hold.

## Next

1. Close the two remaining leaks listed in `AUDIT.md`'s follow-up: `graphify`'s map path restated in `skills/setup/setup-ai-workspace/issue-tracker-local.md`, and the APM dependency cycle between `setup-ai-tooling` and `monitor-ai-tooling`.
2. Add a check against weakening the quality bar (lowered thresholds, skipped tests, new suppression comments) to `skills/workflow/review-and-refactor/` and a one-line rule to `skills/workflow/implement/`; proposed, not yet approved by the user.
3. Run the evals for `document`, `memorize`, `codify`, `delineate`, `interview`, and `setup-ai-workspace`, and record a report under `documentation/evaluations/`.
4. Work through the remaining audit priorities in `AUDIT.md`, starting with priority 4 (unsafe instructions in `triage` and `improve-skills`).

## Open questions

- Whether `triage`'s generic "refine" step word should become "interview"; the user has not said.
- Whether this repository's own `AGENTS.md` should carry `document`'s pointer; the user decides.

## Sources

- `.agents/handoffs/2026-10-07-1752-skill-contracts-and-document-ownership.md`
- `AUDIT.md`
- `documentation/architecture-decision-record/0004-skills-know-each-other-only-by-contract.md`
- `skills/reference/document/SKILL.md` and `skills/reference/document/CONVENTIONS-FORMAT.md`
- `skills/reference/codify/SKILL.md`
