# Handoff: remove the classify skill

Supersedes: none
Workspace: Dyrits/SKILLS repository, branch `main`

To resume: read this whole file first. Treat every claim in State not marked verified as unverified, and check it against the Sources. Read the superseded handoff only when something here cannot be resolved from this file and its Sources. Confirm what was in flight and what you will do next with the user before starting. Never edit this file: a later state goes into a new handoff.

## Goal

Remove `classify` from the repository, because it asked the agent to make a judgement it can already make itself, and say so in `AGENTS.md` so the same kind of skill is not shipped again. Done when no installable skill, manifest, page, or graph entry names it.

## State

Done (goal reached):

- Deleted `skills/productivity/classify/` (SKILL.md, `agents/openai.yaml`, `apm.yml`) and `documentation/skills/productivity/classify.md`. Verified by file listing: the directories are gone.
- Removed its entries from `.claude-plugin/plugin.json`, `marketplace.json`, `apm.yml`, `README.md`, `skills/productivity/README.md`, `skills/productivity/guide/SKILL.md`, and `documentation/skills/productivity/guide.md`. The guide page heading changed from "Setup and outbound skills" to "Setup skills". Verified by `git status` and `git diff`.
- Removed `items` and `labeled-items` from `scripts/skill-graph/flow.json` because only the removed skill used them. Verified by `python3 -m json.tool` (valid JSON).
- Regenerated `index.html`. Verified: `python3 scripts/build-skill-graph.py --check` reports "index.html is current" (exit 0).
- Added a rule to `AGENTS.md` under "Writing skills": do not ship a skill whose only job is a judgement the agent can already make. Verified by reading the file.
- Deleted the local installed copies `~/.claude/skills/classify` (symlink) and `~/.agents/skills/classify` (directory). Verified: both are gone. The copy's `SKILL.md` matched the committed version before deletion.

Checks run on 2026-10-08 at 14:06, all passing:

- `python3 scripts/check-skills.py`: "Checked 46 skills, 46 plugin paths, 46 documentation pages, and 246 Markdown files", exit 0.
- `python3 scripts/test-check-skills.py`: 34 tests, OK.
- `claude plugin validate . --strict`: "Validation passed".

Not done on purpose:

- `scripts/link-skills.sh` was not run. It replaces real directories in `~/.agents/skills` with symlinks into the repository, which changes about 50 installed skills, not only this one.
- Historical references to `classify` remain in `AUDIT.md`, earlier handoffs, `documentation/research/2026-10-03-retained-skill-provenance.md`, and `documentation/evaluations/waza.md`. They are records and are left as written.

Git: `main` was level with `origin/main` (0 ahead, 0 behind) before this handoff. The removal is one commit after `c98b486`, and this handoff is committed after it. Both are pushed to `origin/main`.

## Decisions

- Delete `classify` rather than convert it to a hook. A hook would classify every prompt through a third-party API, which the skill's own privacy rule forbids and which `documentation/architecture-decision-record/0005-make-skills-autonomous.md` defers. Its routing variant is recorded in `.agents/deferred-tooling.md`.
- The user asked that the classifier-based routing idea (classifier verdict to model or agent, prompt forwarded) stay out of the repository for now. Do not add it to `.agents/deferred-tooling.md` unless the user asks.
- The new `AGENTS.md` rule (under "Writing skills") is the reason the skill was removed, not only a note about it.

## Next

None. The goal is reached and nothing here is in flight. Any further work starts a new thread.

## Open questions

- Should `scripts/link-skills.sh` be run now? It replaces real directories in `~/.agents/skills` with symlinks, which affects about 50 installed skills. The user decides; ask before running it.

## Sources

- Removed skill, last committed at `c98b486`: `git show c98b486:skills/productivity/classify/SKILL.md`.
- Rule added: `AGENTS.md`, section "Writing skills".
- Decision record: `documentation/architecture-decision-record/0005-make-skills-autonomous.md`.
- Deferred routing record: `.agents/deferred-tooling.md`.
- Earlier rating of the skill ("medium, narrow"): `AUDIT.md`, section "classify", dated 2026-10-06.
