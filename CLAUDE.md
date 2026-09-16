Skills are organized into bucket folders under `skills/`, named after the published navigation at aihero.dev/skills:

- `getting-started/`: set up once, then find your way around
- `flow/`: the idea-to-ship spine, in order
- `shaping/`: explore an open question and produce a decision or answer that feeds the flow
- `upkeep/`: keep the codebase and issue list healthy; generates work for the flow
- `productivity/`: human-facing workflows you run, not about code
- `reference/`: the reusable layer other skills invoke or cite
- `in-progress/`: beta: public on purpose, feedback wanted, not shipped in the plugin
- `deprecated/`: no longer used

**Promotion is per-path, not per-bucket.** A skill is promoted exactly when it has an entry in `.claude-plugin/plugin.json`'s `skills` array (the Claude Code plugin ships exactly that set). Every promoted skill must also have a reference in the top-level `README.md` and its bucket's `README.md`. The `setup-*` skills in `getting-started/`, and everything in `in-progress/` and `deprecated/`, carry no plugin entry and must not appear in either README's promoted listing (the `getting-started/` bucket README marks them "not in the plugin").

Install commands are copied verbatim from [.agents/install-block.md](./.agents/install-block.md). `.claude-plugin/marketplace.json` makes the repo its own single-plugin marketplace (a fallback the install block explains, not the documented route). Run `claude plugin validate . --strict` after touching either manifest. Why a Claude plugin but not (yet) a Codex one lives in [.agents/adr/0002-ship-as-a-claude-code-plugin.md](./.agents/adr/0002-ship-as-a-claude-code-plugin.md).

Each skill entry in the top-level `README.md` must link the skill name to its `SKILL.md`.

Each bucket folder has a `README.md` that lists every skill in the bucket with a one-line description, with the skill name linked to its `SKILL.md`. Bucket `README.md`s and the top-level `README.md` group entries into **User-invoked** and **Model-invoked** where the mix warrants it; buckets that are all one kind, and non-promoted buckets (`in-progress/`), use a flat list.

Every **promoted** skill also has a human-facing docs page at `documentation/<bucket>/<skill-name>.md` (the docs tree mirrors the bucket folders under `skills/`, one level deep; skills sit flat inside buckets). The published URL is `https://aihero.dev/skills-<skill-name>` regardless of bucket: the docs path is repo organisation only. When you add, rename, or change the behaviour of a promoted skill, create or re-sync its docs page following [.agents/writing-docs.md](./.agents/writing-docs.md). A finished page carries four sections: **What it does**, **When to reach for it**, **Common questions**, and **It's working if**. `writing-docs.md` holds the template, the section order, and where to hunt for the questions. Non-promoted skills (the `setup-*` trio, everything in `in-progress/` and `deprecated/`) get **no** docs page.

Every `SKILL.md` is either user-invoked (`disable-model-invocation: true` plus `policy.allow_implicit_invocation: false` in `agents/openai.yaml`, reachable only by the human) or model-invoked (model- or user-reachable). See [.agents/invocation.md](./.agents/invocation.md).

[`what-is-next`](./skills/getting-started/what-is-next/SKILL.md) is the router that maps every user-reachable skill and how they relate. The same trigger that re-syncs a docs page applies to it: whenever you add, rename, remove, or change how a user-reachable skill fits the flows, re-read `what-is-next`'s `SKILL.md` and update it so the map stays accurate: a new skill it never mentions, or a stale one it still routes to, is a router that lies.

To (re)link every skill outside `deprecated/` into the local harness skill directories (`~/.claude/skills`, `~/.agents/skills`), run `scripts/link-skills.sh`. Each entry is a symlink into this repo, so a `git pull` keeps installed skills current; re-run the script after adding, removing, or renaming a skill.

No em-dashes anywhere in this repo's prose (`SKILL.md` files, docs, `README.md`, `CHANGELOG.md`, ADRs, changesets, code comments). Where a sentence reaches for one, rewrite it instead with a comma, colon, period, parentheses, or a conjunction, whichever the sentence actually wants; never do a blind character substitution.
