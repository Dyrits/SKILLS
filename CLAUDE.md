Skills are organized into bucket folders under `skills/`:

- `getting-started/`: set up once, then find your way around
- `workflow/`: the idea-to-ship spine, in order
- `shaping/`: explore an open question and produce a decision or answer that feeds the flow
- `upkeep/`: keep the codebase and issue list healthy; generates work for the flow
- `productivity/`: human-facing workflows you run, not about code
- `reference/`: the reusable layer other skills invoke or cite
- `work-in-progress/`: beta: public on purpose, feedback wanted, not shipped in the plugin
- `deprecated/`: no longer used

**Promotion is per-path, not per-bucket.** A skill is promoted exactly when it has an entry in `.claude-plugin/plugin.json`'s `skills` array (the Claude Code plugin ships exactly that set). Every promoted skill must also have a reference in the top-level `README.md` and its bucket's `README.md`. The `setup-*` skills in `getting-started/`, and everything in `work-in-progress/` and `deprecated/`, carry no plugin entry and must not appear in either README's promoted listing (the `getting-started/` bucket README marks them "not in the plugin").

Install commands are copied verbatim from [.agents/install-block.md](./.agents/install-block.md). `.claude-plugin/marketplace.json` makes the repository its own single-plugin marketplace (a fallback the install block explains, not the documented route). Run `claude plugin validate . --strict` after touching either manifest. Why a Claude plugin but not (yet) a Codex one lives in [architecture decision record 0002](./documentation/architecture-decision-record/0002-ship-as-a-claude-code-plugin.md).

Each skill entry in the top-level `README.md` must link the skill name to its `SKILL.md`.

Each bucket folder has a `README.md` that lists every skill in the bucket with a one-line description, with the skill name linked to its `SKILL.md`. Bucket `README.md`s and the top-level `README.md` group entries into **User-invoked** and **Model-invoked** where the mix warrants it; buckets that are all one kind, and non-promoted buckets (`work-in-progress/`), use a flat list.

Every **promoted** skill also has a human-facing documentation page at `documentation/<bucket>/<skill-name>.md` (the documentation tree mirrors the bucket folders under `skills/`, one level deep; skills sit flat inside buckets). When you add, rename, or change the behaviour of a promoted skill, create or re-sync its documentation page following [.agents/writing-documentation.md](./.agents/writing-documentation.md). A finished page carries four sections: **What it does**, **When to reach for it**, **Common questions**, and **It's working if**. `writing-documentation.md` holds the template, the section order, and where to hunt for the questions. Non-promoted skills (the `setup-*` trio, everything in `work-in-progress/` and `deprecated/`) get **no** documentation page.

Every `SKILL.md` is either user-invoked (`disable-model-invocation: true` plus `policy.allow_implicit_invocation: false` in `agents/openai.yaml`, reachable only by the human) or model-invoked (model- or user-reachable). See [.agents/invocation.md](./.agents/invocation.md).

[`what-is-next`](./skills/getting-started/what-is-next/SKILL.md) is the router that maps every user-reachable skill and how they relate. The same trigger that re-syncs a documentation page applies to it: whenever you add, rename, remove, or change how a user-reachable skill fits the flows, re-read `what-is-next`'s `SKILL.md` and update it so the map stays accurate: a new skill it never mentions, or a stale one it still routes to, is a router that lies.

To (re)link every skill outside `deprecated/` into the local harness skill directories (`~/.claude/skills`, `~/.agents/skills`), run `scripts/link-skills.sh`. Each entry is a symlink into this repository, so a `git pull` keeps installed skills current; re-run the script after adding, removing, or renaming a skill.

## Language and naming

Prefer full words in repository-owned prose and paths when they remain clear: use `repository`, `document` or `documentation`, `specification`, and `architecture decision record` instead of `repo`, `doc` or `docs`, `spec`, and `ADR`. Use an abbreviation when it is an external name, a literal command or API, a widely established technical term, or when the full term has already been introduced and repetition would reduce readability. Preserve literal URLs and historical quotations.

No em-dashes anywhere in this repository's prose (`SKILL.md` files, documentation, `README.md`, `CHANGELOG.md`, architecture decision records, changesets, code comments). Where a sentence reaches for one, rewrite it instead with a comma, colon, period, parentheses, or a conjunction, whichever the sentence actually wants; never do a blind character substitution.
