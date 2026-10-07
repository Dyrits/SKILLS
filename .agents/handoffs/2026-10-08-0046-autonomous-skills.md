# Handoff: autonomous skills

Supersedes: `2026-10-07-2257-autonomous-skills.md`
Workspace: Dyrits/SKILLS, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Finish the migration in architecture decision record 0005 (standalone skills connected through project artifacts) together with the system-and-capability model in record 0006. Done when no skill calls or suggests another, `document` and `design-modules` are retired, the `reference/` bucket is gone, and the remaining 0005 renames and merges have landed.

## State

- Committed and pushed on `main` in the commit made right after this file was written (verified by reading the commit and push output at the end of the session).
- Verified by running the commands just before writing: `python3 scripts/check-skills.py` passes on 48 skills; `python3 .agents/scripts/generate-skill-manifests.py --check` reports 49 manifests current; `claude plugin validate . --strict` passes; `python3 scripts/test-check-skills.py` fails only `test_linker_includes_every_bucket`, a macOS `/private/var` path mismatch that also fails at earlier commits.
- Verified by file reads, done this session:
  - Record 0006 adds the grid: `delineate` (system, functional), `architect` (system, technical), `specify` (capability, functional), `engineer` (capability, technical). All four are standalone in `skills/workflow/`, each with local copies of `INTERVIEW.md` and the formats it writes, and each adds discovery lines to `AGENTS.md` and the root `README.md` when it creates a document.
  - `ask-someone-else` and `take-over` are deleted. `hand-off` writes self-contained handoffs with a "To resume" paragraph and keeps one `AGENTS.md` line per thread (`skills/productivity/hand-off/HANDOFF-FORMAT.md`).
  - Every skill has an `apm.yml`; the root `apm.yml` depends on every skill with `git: parent` sibling entries, so `apm install Dyrits/SKILLS` installs them all; `marketplace.json` is rebuilt by `apm pack`.
  - `.upstream/` is removed; the README no longer names other repositories; provenance stays in each `SKILL.md`'s `metadata.forks`. `LICENSE` is unchanged.
  - `codify` moved to `setup/`, `interview` to `shaping/`, `write-for-agents`, `unslop`, and `memorize` to `productivity/`. `reference/` holds only `document` and `design-modules`, described as awaiting retirement.
- Assumed, not verified: installing from GitHub resolves the `git: parent` dependencies. APM refuses local `file://` git sources, so only the root's dependency resolution was seen working in a scratch install.
- Per-skill evaluations stay paused (record 0005); no skill change was run against an agent.

## Decisions

- Every requirement, functional or not, belongs to the functional skill of its level; the technical skill answers it. Recorded in record 0006.
- Document names chosen by the agent and not challenged by the user: `documentation/domain.md`, `documentation/architecture.md`, `documentation/capabilities/<capability>/design.md`; `documentation/domain.md` replaces the glossary map. Recorded in record 0006.
- `specify` and `engineer` add one discovery line per kind of document (pointing to `documentation/capabilities/`), not one per capability, to keep `AGENTS.md` and `README.md` short.
- `codify` belongs in `setup/` because record 0005 has it absorb `setup-git-hooks` and `setup-git-guardrails`.
- `reference/` is emptied by retirement, not by moving `document` or `design-modules` elsewhere.

## Next

1. Push-test APM: in a scratch directory, `apm install Dyrits/SKILLS --target claude`, and confirm every skill lands, including those reached through `git: parent`.
2. Migrate the remaining callers to standalone form: skills that still say "Call the Skill tool with" (`iterate`, `triage`, `graphify`, `improve-codebase-architecture`, `review-and-refactor`, `implement`, `taskify`, `setup-ai-workspace`, and others; list them with `grep -rl 'Call the Skill tool' skills`). Give each a local copy of what it used, then remove the call and any next-skill suggestion.
3. Retire `document` and `design-modules` once nothing calls them, then delete `skills/reference/` and its `AGENTS.md` bucket line.
4. Apply the remaining record 0005 boundaries: `interview` renamed `brainstorm`, `memorize` narrowed to `script`, `rebase` and `resolve-merge-conflicts` merged into `reconcile`, `setup-git-hooks` and `setup-git-guardrails` folded into `codify`, `setup-delegation-policy` retired.
5. Decide how bundled copies stay identical (for example a checker rule comparing every `INTERVIEW.md`); nothing checks that yet.

## Open questions

- Whether the attributions removed from the README (HumanLayer for `illustrate`, Cursor for `unslop`, Anthropic for `document`) are required by those sources' licenses; the user decides, after checking each license.
- Whether the `AGENTS.md` handoff line should stay out of git when a project keeps handoffs local-only; raised with the user, not answered.
- Whether the agent-chosen document names in record 0006 stand.

## Sources

- `documentation/architecture-decision-record/0005-make-skills-autonomous.md`
- `documentation/architecture-decision-record/0006-describe-systems-and-capabilities-functionally-and-technically.md`
- `skills/productivity/hand-off/HANDOFF-FORMAT.md`
- `.agents/scripts/generate-skill-manifests.py`
- `.agents/deferred-tooling.md`
- `AUDIT.md`, `EXPLORATORY.md` (the latter untracked, the user's own)
