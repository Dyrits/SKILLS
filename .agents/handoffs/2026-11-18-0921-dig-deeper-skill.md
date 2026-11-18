# Handoff: dig-deeper skill

Supersedes: `2026-11-17-1620-ask-why-skill.md`
Workspace: Dyrits/SKILLS repository, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Ship the five-whys learning skill as `dig-deeper` in the plugin and on `origin/main`.

## State

- Verified in the working tree: the active name is `dig-deeper`. The skill folder, manifest, documentation page, and generated skill map use that name.
- Verified by Git before amending: `9f4f1ed` was the tip of `main` and `origin/main`. The user requested an amend and a repush. Check the current branch and remote tip for the result.

## Decisions

- `dig-deeper` describes following each answer into the mechanism or constraint that explains it. The skill still uses the five-whys method and cites a source or flags an assumption at each layer.
- The lease for the requested push must expect `9f4f1edb2edae26599c9c953189e886c8ad08d77`.

## Next

If the rename is already on `origin/main`, no delivery work remains. Otherwise, check `git status` and the branch tips before resuming delivery.

## Open questions

Whether to add behavioral evaluations or the upstream MIT notice remains open.

## Sources

- `skills/productivity/dig-deeper/SKILL.md`
- `documentation/skills/productivity/dig-deeper.md`
- `.agents/handoffs/2026-11-17-1620-ask-why-skill.md`
