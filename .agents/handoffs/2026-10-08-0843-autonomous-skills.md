# Handoff: autonomous skills

Supersedes: `2026-10-08-0126-autonomous-skills.md`
Workspace: Dyrits/SKILLS, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Finish the migration in architecture decision record 0005 (standalone skills connected through project artifacts) together with the system-and-capability model in record 0006. Done when no skill calls or suggests another, skills find each other's documents only through `AGENTS.md`, `document` and `design-modules` are retired, the `reference/` bucket is gone, and the remaining 0005 renames and merges have landed.

## State

- Committed on `main`, verified with `git log`: `16fe0d3` (documents found through `AGENTS.md`) on top of the commits the superseded handoff lists (`b85929e`, `7e5e5a0`, `0da82d4`, `6feefb4`). Pushed together with the commit that adds this file (assumed at writing time; check `git status` against `origin/main`).
- Verified by running the commands just before writing: `python3 scripts/check-skills.py` passes on 48 skills; `python3 .agents/scripts/generate-skill-manifests.py --check` reports 49 manifests current; `python3 scripts/test-check-skills.py` passes all 34 tests; `claude plugin validate . --strict` passes.
- Standalone migration: done and described in the superseded handoff; no skill outside `skills/reference/` calls another, except the external `webapp-testing` and `skill-creator` and `memorize`'s pointer to itself (verified by grep last session; this session's edits added no call, confirmed by the checker passing).
- New this session, verified by file reads and grep: skills name the kind of document they read and find it through the project's `AGENTS.md`; a kind it does not name does not exist yet. A skill that creates a document uses its own default location only when `AGENTS.md` names none, and adds the document's line to `AGENTS.md`. The rule is in `AGENTS.md` (the standalone-skills paragraph), record 0005's "Documentation and discovery" section, and `documentation/maintenance/invocation.md`. Applied in the shared `PROJECT-DOCUMENTS.md` (now a table of kinds with default locations and a "Finding them" section), the glossary, decision record, and requirements formats, the four grid skills, every reader of the tracker configuration and the AI tooling record, `guide`, and the documentation pages. `setup-ai-workspace` no longer adds a generic `documentation/` line. Skills that create their own records now add an `AGENTS.md` line: `setup-ai-tooling`, `monitor-ai-tooling`, `improve-skills`, `triage`, `improve-codebase-architecture`, `research`, `iterate`.
- Copy families, counted with `md5` just before writing (files, versions): `PROJECT-DOCUMENTS.md` 15, 2 (the second is `document`'s original); `INTERVIEW.md` 11, 1; `GLOSSARY-FORMAT.md` 10, 3 (`teach`'s unrelated format and `document`'s original); `DECISION-RECORD-FORMAT.md` 7, 1; `REQUIREMENTS-FORMAT.md` 4, 1; `CONVENTIONS-FORMAT.md` 6, 2 (`document`'s original); `AGENT-INSTRUCTIONS.md` 6, 1; `IMPLEMENT.md` 3, 2 (`address-feedback`'s is narrowed on purpose); `TEST-FIRST.md` 4, 1; `MODULES.md` 4, 1; `RESEARCH.md`, `DIAGNOSE.md` 3, 1; `LESSONS.md`, `REVIEW.md` 2, 1. Once `document` retires, every family except the two intended variants has one version.
- Per-skill evaluations stay paused (record 0005); no changed skill was run against an agent.

## Decisions

- The user's standing rule: skills are independent, so they never rely on a path another skill chose; they read kinds through `AGENTS.md`, and a creator announces its document there. Recorded in `AGENTS.md` and record 0005.
- A kind `AGENTS.md` does not name is treated as absent, even when a file sits at the default path; the agent chose this strict reading while applying the rule.
- One identical `PROJECT-DOCUMENTS.md` serves readers and writers, so reader-only skills also see the default-location column; chosen to keep a single version.
- `teach`, `design-workflow`, and `walk-through` add no `AGENTS.md` line: their files live in their own workspace folder or are scripts.
- Earlier decisions in the superseded handoff still stand (`outline.md` and `blueprint.md`; dropped tooling stage; reports instead of drafting conventions).

## Next

1. Retire `document` and `design-modules`: nothing calls them. Remove `skills/reference/` with its `README.md`, the two entries in `.claude-plugin/plugin.json`, the root `README.md` and `AGENTS.md` bucket lines, both pages under `documentation/skills/reference/`, their `flow.json` entries, and the two rows in `guide`'s "Standalone and supporting skills" table; find leftover links with `grep -rn "reference/" documentation/skills skills`. Then run `python3 scripts/build-skill-graph.py`, `python3 .agents/scripts/generate-skill-manifests.py`, the checks in State, and `claude plugin validate . --strict`.
2. Add a check that bundled copies stay identical: group files by name across `skills/`, report differing versions, and allow the intended variants (`address-feedback`'s `IMPLEMENT.md`, `teach`'s `GLOSSARY-FORMAT.md`). `scripts/check-skills.py` compares only `divide-and-conquer`'s `ROUTING.md` with the delegation policy, not `iterate`'s copy.
3. Consider a check for the new rule: flag a `documentation/` or `.agents/` path in a skill's read steps that the skill does not create itself. The current exceptions are defaults in creation steps and each skill's own records.
4. Apply the remaining record 0005 boundaries: `interview` renamed `brainstorm`, `memorize` narrowed to `script`, `rebase` and `resolve-merge-conflicts` merged into `reconcile`, `setup-git-hooks` and `setup-git-guardrails` folded into `codify`, `setup-delegation-policy` retired. Each rename also touches the copies' "Adapted from" headers.
5. Deferred by the user: push-test APM with `apm install Dyrits/SKILLS --target claude` in a scratch directory.

## Open questions

- Whether a file at a default path that `AGENTS.md` does not name should count as absent (current strict reading) or be found and then announced in `AGENTS.md`; the user decides.
- Whether reader-only skills should carry a version of `PROJECT-DOCUMENTS.md` without default locations; the user decides.
- Carried over: whether the boundary choices from the migration stand, whether removed README attributions are license-required, whether the `AGENTS.md` handoff line should stay out of git for local-only handoffs, and whether `iterate`'s size (24 files) is acceptable.

## Sources

- `AGENTS.md`
- `documentation/architecture-decision-record/0005-make-skills-autonomous.md`
- `documentation/architecture-decision-record/0006-describe-systems-and-capabilities-functionally-and-technically.md`
- `documentation/maintenance/invocation.md`
- `skills/workflow/specify/PROJECT-DOCUMENTS.md` (one of the identical shared copies)
- Commits `0da82d4`, `16fe0d3`
- `scripts/check-skills.py`, `.agents/scripts/generate-skill-manifests.py`
