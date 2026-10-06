Skills are organized into bucket folders under `skills/`:

- `setup/`: set up once per repository or machine
- `workflow/`: the idea-to-ship spine, in order
- `shaping/`: explore an open question and produce a decision or answer that feeds the flow
- `upkeep/`: keep the codebase and issue list healthy; generates work for the flow
- `version-control/`: branches, merge requests, and their history
- `productivity/`: human-facing workflows and procedures you run, not part of the delivery flow
- `reference/`: disciplines that shape how another task is done, called by other skills; they produce no result of their own
- `deprecated/`: no longer used

**Every skill outside `deprecated/` is promoted.** A promoted skill has an entry in `.claude-plugin/plugin.json`'s `skills` array (the Claude Code plugin ships exactly that set), a reference in the top-level `README.md` and in its bucket's `README.md`, and a documentation page. Adding a skill means adding all four; deprecating one means removing its manifest entry and page. `scripts/check-skills.py` enforces this.

The skills page at the root `index.html`, one small graph per skill, is generated: each promoted skill also needs an entry in `scripts/skill-graph/flow.json` (the artifacts it reads and writes, and its usual next skills). Its section, order, and one-liner come from the bucket `README.md`, its text from the documentation page, and its calls and hand-overs from the dependency paragraph. Change `flow.json` or `scripts/skill-graph/template.html`, never `index.html`, then run `python3 scripts/build-skill-graph.py`; `check-skills.py` fails on a missing entry or a stale map.

Install commands are copied verbatim from [.agents/install-block.md](./.agents/install-block.md). `.claude-plugin/marketplace.json` makes the repository its own single-plugin marketplace (a fallback the install block explains, not the documented route). Run `claude plugin validate . --strict` after touching either manifest. Why a Claude plugin but not (yet) a Codex one lives in [architecture decision record 0002](./.upstream/architecture-decision-record/0002-ship-as-a-claude-code-plugin.md), an upstream decision archived under `.upstream/`; this fork's own decisions live in `documentation/architecture-decision-record/`.

Each skill entry in the top-level `README.md` must link the skill name to its `SKILL.md`.

Each bucket folder has a `README.md` that lists every skill in the bucket with a one-line description, with the skill name linked to its `SKILL.md`.

Every promoted skill has a human-facing documentation page at `documentation/skills/<bucket>/<skill-name>.md` (the documentation tree mirrors the bucket folders under `skills/`, two levels deep; skills sit flat inside buckets). When you add, rename, or change the behaviour of a skill, create or re-sync its documentation page following [.agents/writing-documentation.md](./.agents/writing-documentation.md). A finished page carries four sections: **What it does**, **When to reach for it**, **Common questions**, and **It's working if**. Each page starts with verified upstream skill names or an explicit fork-specific provenance note. `writing-documentation.md` holds the template, the section order, and where to hunt for the questions. Deprecated skills get **no** documentation page.

Every promoted skill has evaluations at `skills/<bucket>/<skill-name>/evals/evals.json`, in the format [.agents/writing-evals.md](./.agents/writing-evals.md) defines (at least three evals: `trigger`, `behavior`, `no-trigger`). When you add a skill or change what it does, add or update its evals; `scripts/check-skills.py` checks their shape.

Every `SKILL.md` is reachable by both the human and the model, so any skill can call any other: no `disable-model-invocation`, no `policy.allow_implicit_invocation: false`, and a model-facing description. See [.agents/invocation.md](./.agents/invocation.md).

[`guide`](./skills/productivity/guide/SKILL.md) is the router that maps every skill and how they relate. The same trigger that re-syncs a documentation page applies to it: whenever you add, rename, remove, or change how a skill fits the flows, re-read `guide`'s `SKILL.md` and update it so the map stays accurate: a new skill it never mentions, or a stale one it still routes to, is a router that lies.

To (re)link every skill outside `deprecated/` into the local harness skill directories (`~/.claude/skills`, `~/.agents/skills`), run `scripts/link-skills.sh`. Each entry is a symlink into this repository, so a `git pull` keeps installed skills current; re-run the script after adding, removing, or renaming a skill.

Call the Skill tool with "memorize" the moment the user corrects you, states a standing rule, or asks you to remember something, and when something is rebuilt a second time. Before writing a script or multi-step pipeline, read `.agents/scripts/INDEX.md` and reuse or extend a match; save new reusable scripts there following [memorize](./skills/reference/memorize/SCRIPTS.md).

## Writing skills

Before writing or editing a `SKILL.md` or its description, read the [skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), alongside `write-for-agents`.

## Language and naming

Prefer full words in repository-owned prose and paths when they remain clear: use `repository`, `document` or `documentation`, `specifications`, and `architecture decision record` instead of `repo`, `doc` or `docs`, `spec`, and `ADR`. Use an abbreviation when it is an external name, a literal command or API, a widely established technical term, or when the full term has already been introduced and repetition would reduce readability. Preserve literal URLs and historical quotations.

Name `AGENTS.md` as the steering file in skills, documentation, evaluations, and scripts: current Claude agents read it, so `CLAUDE.md` does not appear. Two things keep their literal `CLAUDE.md`: a home-directory path a skill installs into (`~/.claude/CLAUDE.md`), and historical records (handoffs, `.upstream/`, architecture decision records).

No em-dashes anywhere in this repository's prose (`SKILL.md` files, documentation, `README.md`, `CHANGELOG.md`, architecture decision records, changesets, code comments). Where a sentence reaches for one, rewrite it instead with a comma, colon, period, parentheses, or a conjunction, whichever the sentence actually wants; never do a blind character substitution.
