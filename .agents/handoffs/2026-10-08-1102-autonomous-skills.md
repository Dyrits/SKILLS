# Handoff: autonomous skills

Supersedes: `2026-10-08-0843-autonomous-skills.md`
Workspace: Dyrits/SKILLS, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Finish the migration in architecture decision record 0005 (standalone skills connected through project artifacts) together with the system-and-capability model in record 0006. Done when no skill calls or suggests another, skills find each other's documents only through `AGENTS.md`, `document` and `design-modules` are retired, the `reference/` bucket is gone, and the remaining 0005 renames and merges have landed.

## State

- Committed on `main`, verified with `git log`: `d8332fc` (adopt an existing home before creating, never overwrite) on top of `16fe0d3` and the earlier commits the superseded handoffs list. Pushed together with the commit that adds this file (assumed at writing time; check `git status` against `origin/main`).
- Verified by running the commands just before committing `d8332fc`: `python3 scripts/check-skills.py` passes on 48 skills; `python3 .agents/scripts/generate-skill-manifests.py --check` reports 49 manifests current; `python3 scripts/test-check-skills.py` passes all 34 tests; `claude plugin validate . --strict` passes.
- Document discovery, verified by file reads: reads are strict (a kind `AGENTS.md` does not name is absent, and a reader that notices a likely unlisted document reports it without using it). Creation follows four steps: look for an existing home of that kind in the project (judged by content, asking when unclear), fall back to the default location, never overwrite (adopt a file at the target and add to it in its own style), and announce it in `AGENTS.md` and the README. The full procedure is the "Finding them" and "Creating one" sections of the shared `PROJECT-DOCUMENTS.md` (14 identical copies, verified with `md5`); the short form is in the glossary, decision record, and requirements formats (one version each), the creation steps of `architect`, `delineate`, and `engineer`, `setup-ai-tooling`, the shared `LESSONS.md`, and the rule's wording in `AGENTS.md`, record 0005, and `documentation/maintenance/invocation.md`. The report clause for readers without the shared file is in `debug` and its `DIAGNOSE.md` copies, `improve-codebase-architecture`, and the three grid skills.
- Copy families are as the superseded handoff lists, with the same version counts (verified with `md5` for `PROJECT-DOCUMENTS.md`, the three formats, `LESSONS.md`, and `DIAGNOSE.md` after this session's edits).
- Per-skill evaluations stay paused (record 0005); no changed skill was run against an agent.

## Decisions

- The user approved the creation procedure above and its order (`AGENTS.md`, then the project's existing home, then the default), matching the standing preference to probe existing mechanisms before a local fallback. This settles the superseded handoff's question about files at default paths: strict for reads, adopt-and-announce for writes.
- One shared `PROJECT-DOCUMENTS.md` for readers and writers, confirmed by the user.
- Earlier decisions in the superseded handoffs still stand.

## Next

1. Retire `document` and `design-modules`: nothing calls them. Remove `skills/reference/` with its `README.md`, the two entries in `.claude-plugin/plugin.json`, the root `README.md` and `AGENTS.md` bucket lines, both pages under `documentation/skills/reference/`, their `flow.json` entries, and the two rows in `guide`'s "Standalone and supporting skills" table; find leftover links with `grep -rn "reference/" documentation/skills skills`. Then run `python3 scripts/build-skill-graph.py`, `python3 .agents/scripts/generate-skill-manifests.py`, the checks in State, and `claude plugin validate . --strict`.
2. Add a check that bundled copies stay identical: group files by name across `skills/`, report differing versions, and allow the intended variants (`address-feedback`'s `IMPLEMENT.md`, `teach`'s `GLOSSARY-FORMAT.md`). The short form of the creation procedure is repeated in non-identical files (the three grid skills, `setup-ai-tooling`, `LESSONS.md`), so a wording change there is a manual sweep: `grep -rn "existing home" skills`.
3. Consider a check for the discovery rule: flag a `documentation/` or `.agents/` path in a skill's read steps that the skill does not create itself.
4. Apply the remaining record 0005 boundaries: `interview` renamed `brainstorm`, `memorize` narrowed to `script`, `rebase` and `resolve-merge-conflicts` merged into `reconcile`, `setup-git-hooks` and `setup-git-guardrails` folded into `codify`, `setup-delegation-policy` retired.
5. Deferred by the user: push-test APM with `apm install Dyrits/SKILLS --target claude` in a scratch directory.

## Open questions

- Carried over: whether the boundary choices from the migration stand, whether removed README attributions are license-required, whether the `AGENTS.md` handoff line should stay out of git for local-only handoffs, and whether `iterate`'s size (24 files) is acceptable.

## Sources

- `AGENTS.md`
- `documentation/architecture-decision-record/0005-make-skills-autonomous.md`
- `documentation/maintenance/invocation.md`
- `skills/workflow/specify/PROJECT-DOCUMENTS.md` (one of the identical shared copies)
- Commits `16fe0d3`, `d8332fc`
- `.agents/handoffs/2026-10-08-0126-autonomous-skills.md` for the migration's copy families and boundary decisions
