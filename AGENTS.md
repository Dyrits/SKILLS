Skills are organized into bucket folders under `skills/`:

- `setup/`: set up once per repository or machine
- `workflow/`: the idea-to-ship spine, in order
- `shaping/`: explore an open question and produce a decision or answer that feeds the flow
- `upkeep/`: keep the codebase and issue list healthy; generates work for the flow
- `version-control/`: branches, merge requests, and their history
- `productivity/`: human-facing workflows and procedures you run, not part of the delivery flow

Every skill has an entry in `.claude-plugin/plugin.json`'s `skills` array (the Claude Code plugin ships exactly that set), a reference in the top-level `README.md` and in its bucket's `README.md`, and a documentation page. Adding or removing a skill means updating all four. `scripts/check-skills.py` enforces this.

The skills page at the root `index.html`, one small graph per skill, is generated: each skill also needs an entry in `scripts/skill-graph/flow.json` (the artifacts it reads and writes, and its usual next skills). Its section, order, and one-liner come from the bucket `README.md`, its text from the documentation page, and its calls and hand-overs from the skill's Skill tool calls and "tell the user to run" lines. Change `flow.json` or `scripts/skill-graph/template.html`, never `index.html`, then run `python3 scripts/build-skill-graph.py`; `check-skills.py` fails on a missing entry or a stale map.

Repository-maintenance guidance lives in `documentation/maintenance/`; `.agents/` holds agent tools, installed skills, and session state.

`documentation/` serves humans and agents. `.agents/` and `AGENTS.md` serve agents only; `README.md` serves primarily humans. When creating shared documentation, add a concise discovery line to both `AGENTS.md` and the appropriate `README.md`. Keep agent-only records discoverable from `AGENTS.md` without adding their internal details to the human README.

For deferred installer and model-routing work, read [.agents/deferred-tooling.md](./.agents/deferred-tooling.md).

For the accepted autonomy and skill-boundary decisions, supersession scope, and unfinished migration, read [architecture decision record 0005](./documentation/architecture-decision-record/0005-make-skills-autonomous.md).

To resume the autonomy migration, read the [current handoff](./.agents/handoffs/2026-10-08-1112-autonomous-skills.md). Handoffs are shared and committed.

To resume the swarm skill, read the [current handoff](./.agents/handoffs/2026-10-08-1116-swarm-skill.md). Handoffs are shared and committed.

To resume the agent-agnostic setup skills and the audit follow-up, read the [current handoff](./.agents/handoffs/2026-10-08-2109-agnostic-setup-skills.md). Handoffs are shared and committed.

To resume the removal of the guide skill, read the [current handoff](./.agents/handoffs/2026-10-09-0031-remove-guide-skill.md). Handoffs are shared and committed.

Install commands are copied verbatim from [standard installation wording](./documentation/maintenance/standard-installation-wording.md). `.claude-plugin/marketplace.json` makes the repository its own single-plugin marketplace (a fallback the installation wording guide explains, not the documented route). Run `claude plugin validate . --strict` after touching either manifest. This repository's decisions live in `documentation/architecture-decision-record/`.

Each skill entry in the top-level `README.md` must link the skill name to its `SKILL.md`.

Each bucket folder has a `README.md` that lists every skill in the bucket with a one-line description, with the skill name linked to its `SKILL.md`.

Every skill has a human-facing documentation page at `documentation/skills/<bucket>/<skill-name>.md` (the documentation tree mirrors the bucket folders under `skills/`, two levels deep; skills sit flat inside buckets). When you add, rename, or change the behaviour of a skill, create or re-sync its documentation page following [documentation/maintenance/writing-documentation.md](./documentation/maintenance/writing-documentation.md). A finished page carries four sections: **What it does**, **When to reach for it**, **Common questions**, and **It's working if**. Each page starts with verified upstream skill names or an explicit fork-specific provenance note. `writing-documentation.md` holds the template, the section order, and where to hunt for the questions.

Per-skill evaluations are paused. Do not create or require `evals/` directories for repository-owned skills. Installed third-party evaluation tooling and historical reports are retained.

Every `SKILL.md` is reachable by both the human and the model: no `disable-model-invocation`, no `policy.allow_implicit_invocation: false`, and a model-facing description. Each skill must complete its advertised task when installed alone, with its own required references and artifact-writing instructions. Bundle local reference copies where necessary. Do not require another skill or suggest another skill as a next step. Connect workflows through discoverable project artifacts instead: a skill that creates a document adds a line for it to the project's `AGENTS.md`, and a skill that reads documents names the kind it needs (requirements, glossary, decision records) and finds it through `AGENTS.md`, never by a path another skill chose. A skill creating a kind `AGENTS.md` does not name looks for an existing home in the project first, falls back to its default location, and never overwrites an existing file, and matches the naming and style of the documents it finds.

To (re)link every skill into the local harness skill directories (`~/.claude/skills`, `~/.agents/skills`), run `scripts/link-skills.sh`. Each entry is a symlink into this repository, so a `git pull` keeps installed skills current; re-run the script after adding, removing, or renaming a skill.

Call the Skill tool with "memorize" the moment the user states a standing rule, asks you to remember something, or corrects how something is done, and when something is rebuilt a second time. Before writing a script or a pipeline longer than one line, read `.agents/scripts/INDEX.md` and reuse or extend a match; save new reusable scripts there following [memorize](./skills/productivity/memorize/SCRIPTS.md).

## Writing skills

Before writing or editing a `SKILL.md` or its description, read the [skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), alongside `write-for-agents`.

Before creating a reusable script, check existing project automation, installed commands, and maintained external tools or libraries. Reuse a suitable implementation; write a small adapter or new script only for an unmet need, considering compatibility, maintenance, licensing, and security.

Do not ship a skill whose only job is a judgement the agent can already make itself, such as sorting text already in context. Keep a skill that supplies a capability, state, or external action the agent lacks; otherwise delete it, or make the behaviour automatic through a mechanism.

Skills ship to other repositories, so a skill holds no rule that only this repository follows. This repository's writing rules live in this file; where a skill's rule could clash with a project's own, the skill defers to that project's steering file or style guide.

## Language and naming

Prefer full words in repository-owned prose and paths when they remain clear: use `repository`, `document` or `documentation`, `specifications`, and `architecture decision record` instead of `repo`, `doc` or `docs`, `spec`, and `ADR`. Use an abbreviation when it is an external name, a literal command or API, a widely established technical term, or when the full term has already been introduced and repetition would reduce readability. Preserve literal URLs and historical quotations.

Name `AGENTS.md` as the steering file in skills, documentation, evaluations, and scripts: current Claude agents read it, so `CLAUDE.md` does not appear. Two things keep their literal `CLAUDE.md`: a home-directory path a skill installs into (`~/.claude/CLAUDE.md`), and historical records (handoffs, architecture decision records).

No em-dashes anywhere in this repository's prose (`SKILL.md` files, documentation, `README.md`, `CHANGELOG.md`, architecture decision records, changesets, code comments). Where a sentence reaches for one, rewrite it instead with a comma, colon, period, parentheses, or a conjunction, whichever the sentence actually wants; never do a blind character substitution.
