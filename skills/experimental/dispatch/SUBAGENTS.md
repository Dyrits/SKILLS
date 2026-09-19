# Subagents

Reached from step 2 of [`SKILL.md`](SKILL.md): what Claude Code calls its delegation tool, where its agent definitions live, and which agents to add when a role has no home. Verify against the tool's own parameter list before dispatching, since a project can rename or replace any of these.

Claude Code is the only harness bound here: the `setup-routing-for-claude` hook that feeds `dispatch` its recommendation is a Claude Code `UserPromptSubmit` hook, so no other harness has a recommendation to act on.

## Known bindings

| Role | Model tier | Claude Code |
| --- | --- | --- |
| planner | read-only | `Plan` |
| explorer | read-only | `Explore` |
| reviewer | mid | `General`*, briefed to review only |
| implementer-fast | cheap | `Fast`* |
| implementer | mid | `General`* |
| implementer-heavy | strongest | `Heavy`* |

\* Not built in. A starred agent absent from the `Agent` tool's `subagent_type` parameter list means setup has not run on this machine, which is what [scripts/setup-agents.sh](scripts/setup-agents.sh) is for. Until it does, the walk-down in `SKILL.md` applies: the outer implementer tiers fall back to the middle one, and the middle one falls back to `general-purpose`.

Claude Code delegates through the `Agent` tool, whose `subagent_type` enumerates the built-ins plus every agent defined in `.claude/agents/*.md` (project) or `~/.claude/agents/*.md` (user). Project beats user beats built-in when names collide. A setup that adds `General` alongside the stock `general-purpose` also denies the built-in (`"permissions": {"deny": ["Agent(general-purpose)"]}`), so read the parameter list rather than assuming either name is present.

## Creating the missing tiers

[scripts/setup-agents.sh](scripts/setup-agents.sh) writes them, in the **user** scope, so every repository on the machine gets them. It is idempotent: existing files are reported as kept and never clobbered without `--force`, so running it a second time costs nothing.

```
scripts/setup-agents.sh --check   # report what is missing, write nothing, exit 1 if any
scripts/setup-agents.sh           # create whatever is missing
```

What it writes:

- `~/.claude/agents/General.md`, `Fast.md`, `Heavy.md`, one `model` pinned per tier.
- A `permissions.deny` entry for `Agent(general-purpose)` in `~/.claude/settings.json`, merged into any existing array. `General` sits **beside** the stock built-in rather than renaming it, and denying the built-in is what leaves one agent per role.

## The read-only tier

`planner`, `explorer` and `reviewer` all read and report rather than write, so they share one model tier, defaulting to the **mid** model rather than the cheap one: planning and review quality is what that tier decides, and exploring on mid still costs a fraction of heavy.

Claude Code has no way to pin a built-in's model while keeping its prompt: a file named `Explore.md` or `Plan.md` **replaces** the built-in wholesale, tuned prompt included. That trade is behind `--shadow-readonly` and off by default. Deleting the two files reverses it.

## Choosing the models

Claude Code takes the aliases `haiku`, `sonnet` and `opus`, which survive model releases, so the tiers are fixed defaults: override any tier with `--read`, `--fast`, `--mid` or `--heavy`, which win outright.

One agent means one model: Claude Code's agent frontmatter has no per-agent fallback chain, so a model outage is a re-run of the script with a different flag, not automatic failover.

Two things it deliberately does not touch. The harness's own default agent (in some wrappers a lowercase `claude`) runs when no agent name is typed, so denying it can break that default. `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS` would remove `Explore` and `Plan` too, and those are the planner and explorer bindings.

Claude Code picks new agent definitions up without a restart, though not instantly, so a dispatch in the same turn the script ran may still see the old list. Falling back once and binding the tier on the next turn is correct behaviour, not a failure.
