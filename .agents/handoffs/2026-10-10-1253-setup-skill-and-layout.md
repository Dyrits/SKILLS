# Handoff: setup skill follow-up and the audit priorities

Supersedes: `2026-10-10-0949-setup-skill-and-layout.md`
Workspace: Dyrits/SKILLS repository, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Finish the follow-ups of the `setup` merge (relinking installed skills, trying `setup` in real repositories), then work through the open `AUDIT.md` priorities.

## State

- The bucket question from the superseded handoff is settled: the user chose to rename `skills/setup/` to `skills/getting-started/` (upstream's original bucket name for these skills). `setup` lives at `skills/getting-started/setup/`, `setup-delegation-policy` at `skills/getting-started/setup-delegation-policy/`, and their pages under `documentation/skills/getting-started/`. Verified: file listing and `python3 scripts/check-skills.py`.
- Every file in `scripts/`, `references/`, and `assets/` now uses lowercase kebab-case names (144 references renamed from UPPERCASE). `scripts/check-skills.py` fails on any other name, and `AGENTS.md` states the rule. Historical records were left unchanged, and the provenance line in `documentation/skills/shaping/prototype.md` keeps upstream's literal `LOGIC.md` and `UI.md`. Verified: no live file names an uppercase reference (searched with `git grep`).
- `marketplace.json` was stale from the setup merge until this commit (it still listed the removed setup skills); it is regenerated with `apm pack`, whose `build/` output is not committed. Verified: it lists 42 packages, with the two `getting-started` paths.
- Verified at the end of the session, all passing: `npm run -s test-inspect-project`, `test-detect-harnesses`, `test-guard-git`, `test-skills-check`, `test-scriptbook-helpers`, `check-skills`, `check-skill-manifests`, `check-plugin-version`, and `claude plugin validate . --strict`.
- The orphaned `skills/productivity/teach/references/glossary-format.md` is a known upstream gap, already described on `documentation/skills/productivity/teach.md` with upstream issue #559. It stays as it is.
- Not done: `scripts/link-skills.sh` was not run, so the user's installed links may still include `guide` and the four removed setup skills. Assumed, not checked.

## Decisions

- Bucket `getting-started/` for per-repository and machine setup. The user chose it from three options (rename, keep `setup/`, flatten all buckets). Recorded in `AGENTS.md`'s bucket list.
- One case for all support files, lowercase kebab-case: the folder already says what kind of file it is, assets become ordinary project files, and scripts were lowercase already. `SKILL.md`, `README.md`, and `AGENTS.md` keep their fixed names. Recorded in `AGENTS.md`.
- The decisions in the superseded handoff still stand.

## Next

1. Ask whether to run `scripts/link-skills.sh` and delete the stale installed links in `~/.claude/skills` and `~/.agents/skills`.
2. Try `setup` in a real repository (one JavaScript or TypeScript project, one Python project) and correct what it gets wrong.
3. Continue the open `AUDIT.md` priorities listed in `2026-10-08-2109-agnostic-setup-skills.md` (2, 4, 5, the rest of 8, 9); 10 is resolved by the `guide` removal, and the Biome and "Token Monitor" items of 8 should be rechecked against `skills/getting-started/setup/references/`.

## Open questions

- 0005 still plans to retire `setup-delegation-policy`; 0007 left that untouched. Does the plan stand? The user decides.

## Sources

- `documentation/architecture-decision-record/0007-merge-project-setup-into-one-skill.md` and `0005-make-skills-autonomous.md`.
- `AGENTS.md` (bucket list, layout and naming rule, catalogue warning).
- `scripts/check-skills.py`, `scripts/test-check-skills.py`, `scripts/build-skill-graph.py`.
- `documentation/maintenance/standard-installation-wording.md`, "Publishing" (the `apm pack` step).
- `AUDIT.md`, section "Priority problems", and `.agents/handoffs/2026-10-08-2109-agnostic-setup-skills.md`.
