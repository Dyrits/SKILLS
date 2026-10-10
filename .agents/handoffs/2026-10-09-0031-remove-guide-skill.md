# Handoff: remove the guide skill

Supersedes: none
Workspace: /Volumes/APFS-G-DRIVE/Codelab/Dyrits/SKILLS, branch `main` (at `99d9b00`, in sync with `origin/main`)

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Delete the `guide` router skill and every live reference to it, leaving the repository's checks green. Done means the removal is committed and pushed.

## State

- The removal is complete in the working tree and uncommitted: 63 files changed (134 insertions, 535 deletions), no untracked files. Verified with `git diff --stat HEAD`.
- Deleted: `skills/productivity/guide/` and `documentation/skills/productivity/guide.md` (staged as deletions).
- Removed from `.claude-plugin/plugin.json`, `marketplace.json`, `apm.yml` (via `python3 .agents/scripts/generate-skill-manifests.py`), the top-level `README.md`, and `skills/productivity/README.md` (the whole "Navigation" section, since `guide` was its only entry). `index.html` regenerated; the `guide` entry and the unused `recommendation` artifact are gone from `scripts/skill-graph/flow.json`.
- `AGENTS.md`: the paragraph requiring a `guide` re-sync on every skill change is removed. `documentation/maintenance/writing-documentation.md` and `invocation.md` no longer mention `guide`. `skills/upkeep/improve-skills/SKILL.md` and its page no longer mention a stale route in `guide`.
- About 45 documentation pages lost their closing "guide maps the whole system" sentence in "Where it fits". Dangling clauses were repaired by hand in `debug.md`, `write-for-agents.md`, `setup-ai-workspace.md`, `draft-merge-request.md`, and `implement.md`.
- `scripts/check-skills.py` no longer requires every skill to be named in the router and no longer exempts `guide` from the dependency-paragraph rule. `scripts/test-check-skills.py` dropped the router test and renamed its fixture skill from `guide` to `helper`.
- Verified in this session: `python3 scripts/check-skills.py` exits 0 (45 skills, 45 pages); `python3 scripts/test-check-skills.py` passes 33 tests; `claude plugin validate . --strict` passes; `generate-skill-manifests.py --check` reports 46 manifests current.
- Assumed, not checked: `git grep -n guide` outside historical files shows no other live reference to the skill.
- Not touched on purpose: `AUDIT.md`, `EXPLORATORY.md`, `documentation/research/`, and older handoffs still mention `guide`; they are historical records.
- The user's installed copy `~/.agents/skills/guide` (a real directory) and `~/.claude/skills/guide` (a symlink to it) still exist; `scripts/link-skills.sh` does not remove them.
- A separate idea, an onboarding skill that reports what an unfamiliar project is, was proposed and then dropped by the user because the README already carries that information. Nothing was built.

## Decisions

- Remove `guide` outright rather than trim it, at the user's request. The earlier `AUDIT.md` verdict (router with high upkeep cost) agrees but did not drive it.
- Keep historical records unchanged, per `documentation/maintenance/writing-documentation.md` ("Historical upstream archives and handoffs remain unchanged").
- No replacement router and no onboarding skill, at the user's request.

## Next

1. Review the working tree, commit it as one change with a message about removing the `guide` skill and its references (end the message with the attribution line the harness requires), then push `main` to `origin`. Confirm with the user first if the harness gates commits and pushes.
2. Optionally remove the stale installed copies `~/.agents/skills/guide` and `~/.claude/skills/guide` after the user agrees.

## Open questions

- Should the stale installed `guide` copies in the user's home directory be deleted? The user decides.

## Sources

- `git diff HEAD` on `main` for the full change.
- Earlier precedent for removing a skill: commit `5661d37` (classify) and `.agents/handoffs/2026-10-08-1406-remove-classify-skill.md`.
- `AGENTS.md` for the rules a skill removal must follow (manifests, README entries, documentation page, skill graph).
