# Handoff: verify skill added, fresh skill audit written

Supersedes: `2026-10-10-1253-setup-skill-and-layout.md`
Workspace: Dyrits/SKILLS repository, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Keep the skill collection consistent and standalone: land the new `verify` skill, replace the old audit with one made from the current files, then work through the audit's priority problems.

## State

- The `verify` skill is committed (`skills/workflow/verify/`, `documentation/skills/workflow/verify.md`) and `draft-merge-request` is removed with its documentation page. Verified: `python3 scripts/check-skills.py` passes (42 skills, 42 plugin paths, 42 documentation pages) and `claude plugin validate . --strict` passed before the commit.
- The previous `AUDIT.md` was deleted at the user's request and a new `AUDIT.md` was written from the current files. Four read-only reviewers produced the findings; the file lists a verdict for each of the 42 skills, seven priority problems, smaller defects, and four overlaps. Verified by hand: the credential-helper instruction (`skills/upkeep/improve-skills/SKILL.md:69`), the `webapp-testing` mentions (`implement/SKILL.md:16` and two bundled `references/implement.md:13`), the `test-first` `agents/openai.yaml` short description, the wrong `rebase` claim at `sync-tree/SKILL.md:125`, the dangling "requirements format" link in `memorize/references/project-documents.md:36`, the stale "merge requests" in `skills/version-control/README.md:3`, and the identical copies of `project-documents.md` (14) and `interview.md` (11). Every other finding is the reviewers' word and is unverified.
- No finding has been fixed yet.
- `EXPLORATORY.md` still cites the deleted audit in about 15 places; those citations now point at different content. Not changed.
- `scripts/link-skills.sh` has still not been run, so installed links in `~/.claude/skills` and `~/.agents/skills` may include removed skills (`guide`, the old setup skills, `draft-merge-request`). Assumed, not checked.

## Decisions

- The old audit was deleted and redone without reading it, so the new one stands alone. The old text is only in git history; do not use it as input.
- Handoffs are shared and committed (earlier ones are tracked).
- Leftover historical mentions of `draft-merge-request` stay: `documentation/evaluations/waza.md`, the provenance table in `documentation/research/2026-10-03-retained-skill-provenance.md`, and the retired-name list in `scripts/test-check-skills.py`.
- Decisions in the superseded handoff still stand: bucket `getting-started/`, lowercase kebab-case support file names.

## Next

1. Fix audit priority 1: remove the stored-credential route from `skills/upkeep/improve-skills/SKILL.md:69`.
2. Fix the single-edit defects listed under "Smaller defects" in `AUDIT.md`.
3. Work through priorities 2 to 7 in `AUDIT.md`, starting with the standalone gaps (priority 2) and the seam gap between `engineer`, `implement`, `test-first` and `divide-and-conquer` (priority 3).
4. Add a drift check to `scripts/check-skills.py` that compares bundled copies with their originals (priority 5), with a test in `scripts/test-check-skills.py`.
5. From the superseded handoff, still open: ask whether to run `scripts/link-skills.sh` and remove stale installed links; try `setup` in a real JavaScript or TypeScript repository and a Python repository.
6. Decide the four overlaps in `AUDIT.md` ("Overlaps worth a decision") with the user, and reword or drop the `AUDIT.md` citations in `EXPLORATORY.md`.

## Open questions

- Does the plan to retire `setup-delegation-policy` (architecture decision record 0005) still stand, given 0007 left it alone? The user decides.
- Merge `improve-skills` with `improve-environment`, and `work-in-tree` with `sync-tree`? The user decides.
- Remove `optimize-process` and `re-explain`, or keep them trimmed? The user decides.

## Sources

- `AUDIT.md` (this session's output) and `AGENTS.md` (rules the audit judges against).
- `skills/workflow/verify/SKILL.md` and `documentation/skills/workflow/verify.md`.
- `scripts/check-skills.py`, `scripts/test-check-skills.py`, `scripts/link-skills.sh`.
- `documentation/architecture-decision-record/0005-make-skills-autonomous.md` and `0007-merge-project-setup-into-one-skill.md`.
- Commits `a808c6b` (verify added, `draft-merge-request` removed) and the audit rewrite that follows it on `main`.
