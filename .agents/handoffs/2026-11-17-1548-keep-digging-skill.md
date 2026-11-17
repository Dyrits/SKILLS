# Handoff: keep-digging skill

Supersedes: none
Workspace: Dyrits/SKILLS repository, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Add a productivity skill, `keep-digging`, that explains how or why something works by asking why of each sourced answer until bedrock. It is a fork of the skill of the same name in the external repository Tarektouati/skills, so done means the skill is installed in the plugin, documented, and passes the repository checks.

## State

- Verified by reading the files: `skills/productivity/keep-digging/` holds `SKILL.md`, `apm.yml`, and `agents/openai.yaml`. Its `metadata.forks` names `Tarektouati/skills/keep-digging`.
- Verified by diff: the skill is listed in `.claude-plugin/plugin.json`, the top-level `README.md`, `skills/productivity/README.md` (under Sharpening), and `scripts/skill-graph/flow.json`. `index.html` was regenerated with `python3 scripts/build-skill-graph.py`.
- Verified by reading the file: `documentation/skills/productivity/keep-digging.md` has the provenance note and the four required sections plus Where it fits.
- Verified this session: `python3 scripts/check-skills.py` passed (43 skills, 43 plugin paths, 43 documentation pages), `claude plugin validate . --strict` passed, and no em dash appears in the skill or its page. The validator warns that `README.md` has no `/plugin install dyrits-skills --marketplace Dyrits/SKILLS` line; this predates the change and was left alone.
- Assumed: the source repository's `SKILL.md` and `README.md` fetched from raw.githubusercontent.com on 2026-11-17 are its current content.
- Not verified: behavioral evaluations of the skill, and local linking with `scripts/link-skills.sh`.
- Commit and push to `origin/main` were requested; check `git log` and `git status` for the final state before describing the work as published.

## Decisions

- Name it `keep-digging`, matching the source, and place it in `productivity` under Sharpening, beside the other skills that build understanding in conversation.
- Keep the technique as a comprehension tool, not incident root-cause analysis. The skill body does not name another skill; the documentation page points to `debug`, `teach`, and `re-explain` for the neighbors.
- Add one rule to the source: every layer cites a source or is flagged as an assumption, and a layer that cannot be sourced ends the chain. The reason is that a plausible unchecked chain can be wrong at every step.
- Stop at bedrock rather than at a fixed five layers, as the source does.

## Next

1. Confirm the commit and push state with `git log origin/main..HEAD` and `git status`.
2. Run `scripts/link-skills.sh` if the skill should be available in the local harness directories.
3. Optionally add an evaluation suite under `evaluations/productivity/keep-digging/` if asked; evaluations are allowed, not required.

## Open questions

Whether to add an evaluation suite. The user decides.

## Sources

- https://github.com/Tarektouati/skills/tree/main/keep-digging
- `skills/productivity/keep-digging/SKILL.md`
- `documentation/skills/productivity/keep-digging.md`
- `documentation/maintenance/writing-documentation.md`
- `scripts/check-skills.py`
