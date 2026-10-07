# Handoff: skill contracts and document ownership

Supersedes: none
Workspace: Dyrits/SKILLS, branch `main`

## Goal

Act on the 2026-10-06 skills audit for `memorize` and `document`, then restructure how skills depend on each other: each skill is complete for its own job, calls others for theirs, and knows them only by contract. Done when every shared document has one owner and the remaining leaks listed below are closed.

## State

- Committed and pushed on `main` in one commit after this file was written (verified by the commit and push output at the end of the session).
- `python3 scripts/check-skills.py` passes on 48 skills; `python3 .agents/scripts/generate-skill-manifests.py --check` reports 30 manifests current; `claude plugin validate . --strict` passes (verified, run just before writing this file).
- `python3 scripts/test-check-skills.py`: 37 tests, one failure, `test_linker_includes_every_bucket`, which also fails at the previous commit because macOS resolves the temporary directory under `/private/var` (verified by running it at the previous commit with the changes stashed).
- No eval was run in this session; every skill change is an editorial judgment, not measured behavior (assumed sound, not verified).
- Skill changes, all verified by reading the files after editing:
  - `skills/reference/document/`: `SKILL.md` holds the one layout table for every shared document under `documentation/` (changelog, glossary, conventions moved there from the root) and adds its own `AGENTS.md` pointer; the glossary, conventions, and decision record format files live here; `PROJECT-DOCUMENTS.md` defines an obligation as imposed from outside the code and outranking a code convention.
  - `skills/reference/interview/` was `refine`; `skills/reference/delineate/` was `model-domain`, now only the term discipline; `skills/reference/codify/` is new, holding the conventions offer, interview, audit, and decline.
  - `skills/reference/memorize/`: narrowed triggers, one-off-correction filter, eval fixtures in `evals/files/`.
  - Dependency paragraphs list skill names only; `check-skills.py` generates the wording and now also fails a paragraph placed inside the frontmatter.
  - Other skills name documents by role, not path; `setup-ai-workspace` calls `document` and `memorize` to add their own pointers instead of copying them.
- Stale installed copies of `refine` and `model-domain` remain in `~/.agents/skills/` and are linked from `~/.claude/skills/`, outside the repository; left for the user to remove (verified with `ls -la`).

## Decisions

- Skills know each other only by contract; `document` owns every path that more than one skill reads or writes. Recorded in `documentation/architecture-decision-record/0004-skills-know-each-other-only-by-contract.md`.
- Dependency paragraphs stay, as plain lists of names, with no install command or fallback: APM installs dependencies from each skill's `apm.yml`. Recorded in `documentation/maintenance/invocation.md`; the checker enforces it.
- Requirements say what the product must do and come from outside the code; conventions say how code is written and are the team's choice; a requirement wins a clash. Recorded in `PROJECT-DOCUMENTS.md` and `CONVENTIONS-FORMAT.md` under `skills/reference/document/`.
- No migration of existing projects' root `CHANGELOG.md`, `GLOSSARY.md`, or `CONVENTIONS.md`: the user does not want it.
- Work happens in place on `main`, without a branch, at the user's request.
- `AUDIT.md` keeps its 2026-10-06 findings unchanged; a follow-up section lists what was resolved.

## Next

1. Close the remaining contract leaks listed in the follow-up section of `AUDIT.md`: `graphify`'s map path restated in `skills/setup/setup-ai-workspace/issue-tracker-local.md`, the `.agents/domain.md` decline marker that `codify` reads from a file `setup-ai-workspace` owns, and the APM dependency cycle between `setup-ai-tooling` and `monitor-ai-tooling`.
2. Add a check against weakening the quality bar (lowered thresholds, skipped tests, new suppression comments) to `skills/workflow/review-and-refactor/` and a one-line rule to `skills/workflow/implement/`; proposed in this session, not yet approved.
3. Run the evals for `document`, `memorize`, `codify`, `delineate`, and `interview` and record a report under `documentation/evaluations/`.
4. Work through the remaining audit priorities in `AUDIT.md` (2 to 8, 10), starting with priority 4 (unsafe instructions in `triage` and `improve-skills`).

## Open questions

- Whether `triage`'s generic "refine" step word should become "interview" too; the user has not said.
- Whether this repository's own `AGENTS.md` should carry `document`'s pointer; it uses `documentation/` for decision records and maintenance guidance but none of the delivery documents. The user decides.

## Sources

- `AUDIT.md` (2026-10-06 audit and its 2026-10-07 follow-up)
- `documentation/architecture-decision-record/0004-skills-know-each-other-only-by-contract.md`
- `documentation/maintenance/invocation.md`
- `skills/reference/document/SKILL.md`
- https://github.com/addyosmani/agent-skills/blob/main/commands/constraints.toml (the constraints idea discussed for the quality-bar check)
