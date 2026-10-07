# Handoff: autonomous skills

Supersedes: `2026-10-08-0046-autonomous-skills.md`
Workspace: Dyrits/SKILLS, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Finish the migration in architecture decision record 0005 (standalone skills connected through project artifacts) together with the system-and-capability model in record 0006. Done when no skill calls or suggests another, `document` and `design-modules` are retired, the `reference/` bucket is gone, and the remaining 0005 renames and merges have landed.

## State

- Three commits this session on `main`, verified with `git log`: `b85929e` (test root resolved, so `scripts/test-check-skills.py` passes on macOS), `7e5e5a0` (document renames), `0da82d4` (standalone migration). They are pushed together with the commit that adds this file (assumed at writing time; check `git status` against `origin/main`).
- Verified by running the commands just before writing: `python3 scripts/check-skills.py` passes on 48 skills; `python3 .agents/scripts/generate-skill-manifests.py --check` reports 49 manifests current; `python3 scripts/test-check-skills.py` passes all 34 tests; `claude plugin validate . --strict` passes.
- Verified by grep: outside `skills/reference/`, the only remaining Skill tool calls are to the external `webapp-testing` (in `implement` and its two `IMPLEMENT.md` copies) and `skill-creator` (`write-for-agents`), plus `memorize`'s pointer to itself. No `**Calls:**` or `**Hands over to:**` paragraph remains outside `skills/reference/document/`. Every `apm.yml` except `guide`'s and `document`'s has no dependencies.
- Document renames (verified by file reads): the system outline is `documentation/outline.md` with `skills/workflow/delineate/OUTLINE-FORMAT.md`; the capability's technical document is `documentation/capabilities/<capability>/blueprint.md` with `skills/workflow/engineer/BLUEPRINT-FORMAT.md`. Record 0006 gained a "Document names" decision explaining both. The artifact id in `scripts/skill-graph/flow.json` is now `blueprint`.
- Migration (verified by file reads and the checks above): all 25 former callers carry local copies, linked from their `SKILL.md`, each headed "Adapted from the `<skill>` skill" when copied. Copy families and how many distinct versions exist, counted with `md5`: `PROJECT-DOCUMENTS.md` 15 files, 3 versions (the callers' version, `specify`'s narrower one, `document`'s original); `INTERVIEW.md` 11 files, 1 version; `GLOSSARY-FORMAT.md` 10 files, 3 versions (one is `teach`'s unrelated format, one is `document`'s); `DECISION-RECORD-FORMAT.md` 7, 1; `CONVENTIONS-FORMAT.md` 6, 2 (`document`'s original differs by its `write-for-agents` mention); `AGENT-INSTRUCTIONS.md` 6, 1; `TEST-FIRST.md` 4, 1; `MODULES.md` 4, 1; `IMPLEMENT.md` 3, 2 (`address-feedback`'s is a narrowed version); `UNSLOP.md`, `RESEARCH.md` 3, 1 each; `REVIEW.md` 2, 1. Smaller families: `DIAGNOSE.md`, `tests.md`, `mocking.md`, `scripts/hitl-loop.template.sh`, `ROUTING.md`, `MERGE-REQUEST.md`, `SUMMARY-VISUAL.md`, `DEEPENING.md`, `DESIGN-IT-TWICE.md`, `PRIORITIZE.md`, `DIVIDE-AND-CONQUER.md`, `PUBLISH.md`, `inline-suggestions.md`, `PROTOTYPE.md`, `LOGIC.md`, `UI.md`, `ILLUSTRATE.md`, `HTML.md`, `LESSONS.md`, `WIZARD.md`, `template.sh`, `REBASE.md` (`sync-tree`), `RESOLVE.md` (`rebase`).
- The canonical copies used during the session lived in `/tmp/migration-brief/` and are not kept; the files in the repository are the only sources now.
- Also re-synced (verified by file reads): `guide`'s router text, `documentation/maintenance/invocation.md` and `writing-documentation.md`, `write-for-agents`'s `SKILL-MECHANICS.md` (skills are reachable two ways and never call each other), every affected documentation page, and the boilerplate "an agent or another skill can reach for it", which now reads "an agent can reach for it" on 27 pages.
- Per-skill evaluations stay paused (record 0005); no changed skill was run against an agent.

## Decisions

- `outline.md` and `blueprint.md`, chosen by the user; the reasons are in record 0006.
- What a caller used was copied; what record 0005 places in another skill's boundary was dropped instead, so the owning skill keeps its concern: `setup-ai-workspace` lost its optional stage for tooling, hooks, guardrails, and the delegation policy; `review-and-refactor`, `improve-codebase-architecture`, and `setup-ai-workspace` report a missing conventions file instead of drafting one (`codify` drafts); `iterate` records a single convention the user settles, using its `CONVENTIONS-FORMAT.md` copy. These choices were the agent's, made while the user was away, and are not recorded elsewhere.
- Where a skill used to hand over to `setup-ai-workspace` because tracker configuration was missing (`triage`, `graphify`, `divide-and-conquer`), it now names the missing file and stops, or asks and keeps remote updates pending.
- Skill findings in `memorize`, `improve-skills`, and `improve-environment` are listed for the user instead of handed to another skill.
- `address-feedback` carries a narrowed implement procedure (reproduce a bug first, test-first at established seams) instead of the full diagnosis loop; `divide-and-conquer`'s `REVIEW.md` drops the publication step.
- Descriptions changed to drop skill-to-skill triggers: `illustrate`, `interview`, `implement`, `test-first`, `setup-ai-workspace`, `setup-ai-tooling`.

## Next

1. Retire `document` and `design-modules`: nothing calls them now. Remove `skills/reference/` with its `README.md`, the two entries in `.claude-plugin/plugin.json`, the root `README.md` and `AGENTS.md` bucket lines, both documentation pages under `documentation/skills/reference/`, their `flow.json` entries, and the two rows in `guide`'s "Standalone and supporting skills" table; check documentation pages that still link `../reference/` (`grep -rn "reference/" documentation/skills`). Then run `python3 scripts/build-skill-graph.py`, `python3 .agents/scripts/generate-skill-manifests.py`, the checks listed in State, and `claude plugin validate . --strict`.
2. Decide how bundled copies stay identical (the old handoff's step 5, now pressing given the families listed in State): for example a checker rule that groups files by name and reports differing versions, with an allowlist for intended variants (`specify`'s `PROJECT-DOCUMENTS.md`, `address-feedback`'s `IMPLEMENT.md`, `teach`'s `GLOSSARY-FORMAT.md`). `scripts/check-skills.py` already compares `ROUTING.md` with the delegation policy, but only `divide-and-conquer`'s copy, not `iterate`'s.
3. Apply the remaining record 0005 boundaries: `interview` renamed `brainstorm`, `memorize` narrowed to `script`, `rebase` and `resolve-merge-conflicts` merged into `reconcile`, `setup-git-hooks` and `setup-git-guardrails` folded into `codify`, `setup-delegation-policy` retired. Each rename also touches the copies' "Adapted from" headers.
4. Deferred by the user ("ignore the APM part for now"): push-test APM with `apm install Dyrits/SKILLS --target claude` in a scratch directory.

## Open questions

- Whether the user accepts the boundary choices in Decisions (dropped tooling stage, reports instead of drafting conventions); the user decides.
- Whether the attributions removed from the README (HumanLayer for `illustrate`, Cursor for `unslop`, Anthropic for `document`) are required by those sources' licenses; the user decides, after checking each license.
- Whether the `AGENTS.md` handoff line should stay out of git when a project keeps handoffs local-only; raised with the user, not answered.
- Whether `iterate`'s size (24 files, mostly copies) is acceptable or wants a lighter copy of the parallel-implementation branch; the user decides.

## Sources

- `documentation/architecture-decision-record/0005-make-skills-autonomous.md`
- `documentation/architecture-decision-record/0006-describe-systems-and-capabilities-functionally-and-technically.md`
- `documentation/maintenance/invocation.md`
- Commits `b85929e`, `7e5e5a0`, `0da82d4`
- `scripts/check-skills.py`, `.agents/scripts/generate-skill-manifests.py`
- `AUDIT.md`, `EXPLORATORY.md` (the latter the user's own exploration notes)
