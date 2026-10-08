# Handoff: autonomous skills

Supersedes: `2026-10-08-1102-autonomous-skills.md`
Workspace: Dyrits/SKILLS, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Finish the migration in architecture decision record 0005 (standalone skills connected through project artifacts) together with the system-and-capability model in record 0006. Done when no skill calls or suggests another, skills find each other's documents only through `AGENTS.md`, the bundled copies stay identical by a check, and the remaining 0005 renames and merges have landed. Retiring `document` and `design-modules` and removing the `reference/` bucket are done.

## State

- Committed on `main`, verified with `git log`: `d1ad6b2` (retire `document` and `design-modules`) on top of `eb56968` and the commits the superseded handoffs list. This handoff is committed and pushed right after `d1ad6b2` (assumed at writing time; check `git status` against `origin/main`).
- Retirement, verified by running the commands just before committing: `python3 scripts/check-skills.py` passes on 46 skills, 46 plugin paths, and 46 documentation pages; `python3 .agents/scripts/generate-skill-manifests.py --check` reports 47 manifests current; `python3 scripts/test-check-skills.py` passes all 34 tests; `claude plugin validate . --strict` passes. `grep -rIn "skills/reference"` finds only historical records (handoffs, `AUDIT.md`, `EXPLORATORY.md`, evaluations, records 0001 and 0006) and the fixture names in `scripts/test-check-skills.py`.
- Removed with it: `skills/reference/`, `documentation/skills/reference/`, the entries in `.claude-plugin/plugin.json`, `apm.yml`, `marketplace.json` (edited by hand, since it is normally written by `apm pack`; the format is unchanged), and `scripts/skill-graph/flow.json` (with its orphaned `technical-documents` artifact), the `reference` bucket in `scripts/build-skill-graph.py` and `AGENTS.md`, the two rows in `guide`'s `SKILL.md` and its documentation page, and the `document` links in the `engineer` and `write-for-agents` pages. The install wording now reads "install `setup-ai-workspace` first" in `README.md` and `documentation/maintenance/standard-installation-wording.md`. The root `README.md` says each skill carries the project-document rules it needs. `index.html` and the manifests were regenerated.
- Copy families, counted with `md5` after the retirement (files, versions): `PROJECT-DOCUMENTS.md` 14, 1; `CONVENTIONS-FORMAT.md` 5, 1; `DECISION-RECORD-FORMAT.md` 7, 1; `REQUIREMENTS-FORMAT.md` 4, 1; `INTERVIEW.md` 11, 1; `MODULES.md` 4, 1; `GLOSSARY-FORMAT.md` 9, 2 (`teach`'s unrelated format); `IMPLEMENT.md` 3, 2 (`address-feedback`'s narrowed version). Only the two intended variants differ.
- Per-skill evaluations stay paused (record 0005); no changed skill was run against an agent.

## Decisions

- The user asked for the retirement after reading the previous handoff; the handoff's own plan (nothing calls either skill) was verified by grep and by the checker.
- Earlier decisions stand: creation order is `AGENTS.md`, then the project's existing home, then the default location; reads are strict; one shared `PROJECT-DOCUMENTS.md` for readers and writers; `outline.md` and `blueprint.md` names.

## Next

1. Add a check that bundled copies stay identical: group files by name across `skills/`, report differing versions, and allow the intended variants (`address-feedback`'s `IMPLEMENT.md`, `teach`'s `GLOSSARY-FORMAT.md`). The short form of the creation procedure is repeated in non-identical files (the three grid skills, `setup-ai-tooling`, `LESSONS.md`), so a wording change there is a manual sweep: `grep -rn "existing home" skills`. `scripts/check-skills.py` compares only `divide-and-conquer`'s `ROUTING.md` with the delegation policy, not `iterate`'s copy.
2. Consider a check for the discovery rule: flag a `documentation/` or `.agents/` path in a skill's read steps that the skill does not create itself.
3. Apply the remaining record 0005 boundaries: `interview` renamed `brainstorm`, `memorize` narrowed to `script`, `rebase` and `resolve-merge-conflicts` merged into `reconcile`, `setup-git-hooks` and `setup-git-guardrails` folded into `codify`, `setup-delegation-policy` retired. Each rename also touches the copies' "Adapted from" headers, and `apm.yml`, `marketplace.json`, `plugin.json`, `flow.json`, `guide`, both README files, and the documentation pages.
4. Deferred by the user: push-test APM with `apm install Dyrits/SKILLS --target claude` in a scratch directory.

## Open questions

- `document` carried a four-step procedure for plain README, runbook, and API reference writing (name the reader and task, follow the repository's own rules, check claims against the system, link instead of copying). No remaining skill covers it; the user decides whether to keep that guidance somewhere.
- Record 0005 still describes `document` as to be removed; whether to add a dated note that it was retired on 2026-10-08. The user decides.
- Carried over: whether the boundary choices from the migration stand, whether removed README attributions are license-required, whether the `AGENTS.md` handoff line should stay out of git for local-only handoffs, and whether `iterate`'s size (24 files) is acceptable.

## Sources

- `AGENTS.md`
- `documentation/architecture-decision-record/0005-make-skills-autonomous.md`
- `documentation/maintenance/invocation.md`
- `skills/workflow/specify/PROJECT-DOCUMENTS.md` (one of the identical shared copies)
- Commits `d1ad6b2`, `d8332fc`, `16fe0d3`
- `.agents/handoffs/2026-10-08-1102-autonomous-skills.md` for the creation procedure and its decisions
- `.agents/handoffs/2026-10-08-0126-autonomous-skills.md` for the migration's boundary decisions
