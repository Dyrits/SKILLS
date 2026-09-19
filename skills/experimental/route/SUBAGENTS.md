# Subagents per harness

Reached from step 3 of [`SKILL.md`](SKILL.md): what each harness calls its delegation tool, where its agent definitions live, and which agents to add when a role has no home. Verify against the tool's own parameter list before dispatching, since a project can rename or replace any of these.

## Known bindings

| Role | Model tier | Claude Code | OpenCode | Codex CLI |
| --- | --- | --- | --- | --- |
| planner | read-only | `Plan` | `plan` | inline |
| explorer | read-only | `Explore` | `explore` | inline |
| reviewer | mid | `General`*, briefed to review only | `general`, briefed to review only | inline |
| implementer-fast | cheap | `Fast`* | `fast`* | inline |
| implementer | mid | `General`* | `general` | inline |
| implementer-heavy | strongest | `Heavy`* | `heavy`* | inline |

\* Not built in. A starred agent absent from the delegation tool's parameter list means setup has not run on this machine, which is what [scripts/setup-agents.sh](scripts/setup-agents.sh) is for. Until it does, the walk-down in `SKILL.md` applies: the outer implementer tiers fall back to the middle one, and the middle one falls back to the harness's general agent (`general-purpose` in a stock Claude Code, `general` in OpenCode).

**Claude Code** delegates through the `Agent` tool, whose `subagent_type` enumerates the built-ins plus every agent defined in `.claude/agents/*.md` (project) or `~/.claude/agents/*.md` (user). Project beats user beats built-in when names collide. A setup that adds `General` alongside the stock `general-purpose` usually also denies the built-in (`"permissions": {"deny": ["Agent(general-purpose)"]}`), so read the parameter list rather than assuming either name is present.

**OpenCode** delegates through the `task` tool, whose `subagent_type` covers the built-ins (`general`, `explore`, `scout`, and the primary `plan`) plus `.opencode/agents/*.md` (project) and `~/.config/opencode/agents/*.md` (user). The older singular `agent/` is still read. `build` is OpenCode's primary session agent rather than a routing target, so leave it out of the bindings.

**Codex CLI** has no delegation tool, so every role runs inline.

## Creating the missing tiers

[scripts/setup-agents.sh](scripts/setup-agents.sh) writes them, in the **user** scope, so every repository on the machine gets them. It is idempotent: existing files are reported as kept and never clobbered without `--force`, so running it a second time costs nothing.

```
scripts/setup-agents.sh --check   # report what is missing, write nothing, exit 1 if any
scripts/setup-agents.sh           # create whatever is missing
```

What it writes:

- `~/.claude/agents/General.md`, `Fast.md`, `Heavy.md`, one `model` pinned per tier.
- A `permissions.deny` entry for `Agent(general-purpose)` in `~/.claude/settings.json`, merged into any existing array. `General` sits **beside** the stock built-in rather than renaming it, and denying the built-in is what leaves one agent per role.
- `~/.config/opencode/agents/fast.md` and `heavy.md`, plus `general`, `explore` and `plan` model pins in `~/.config/opencode/opencode.json`. Skipped when no OpenCode install is found.

## The read-only tier

`planner`, `explorer` and `reviewer` all read and report rather than write, so they share one model tier, defaulting to the **mid** model rather than the cheap one: planning and review quality is what that tier decides, and exploring on mid still costs a fraction of heavy.

The two harnesses are not symmetric here. OpenCode pins a built-in's model through `opencode.json` and leaves its prompt intact, so `explore` and `plan` are pinned by default. Claude Code has no prompt-preserving equivalent: a file named `Explore.md` or `Plan.md` **replaces** the built-in wholesale, tuned prompt included. That trade is behind `--shadow-readonly` and off by default. Deleting the two files reverses it.

## Choosing the models

Claude Code takes the aliases `haiku`, `sonnet` and `opus`, which survive model releases, so its tiers are fixed defaults.

OpenCode has no alias form, so each tier carries a **preference list**, best first, and the script picks the first entry whose provider is authenticated in `~/.local/share/opencode/auth.json` (provider names only; the credentials in that file are never read). A machine on OpenCode Go resolves to those models, one on Z.ai to those, one on neither to the Anthropic backstop, with no flags. The capability ordering inside a provider is inferred from model names, which is a guess: override any tier with `--read`, `--fast`, `--mid`, `--heavy` or their `--oc-` counterparts, which win outright.

One agent means one model. Neither harness supports a per-agent fallback chain: OpenCode's agent entry takes `description`, `model`, `prompt` and `tools`, and Claude Code's frontmatter has no equivalent. The preference list is resolved once at setup, not per request, so a provider going down is a re-run of the script rather than an automatic failover.

Two things it deliberately does not touch. The harness's own default agent (in some wrappers a lowercase `claude`) runs when no agent name is typed, so denying it can break that default. `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS` would remove `Explore` and `Plan` too, and those are the planner and explorer bindings.

Claude Code picks new agent definitions up without a restart, though not instantly, so a dispatch in the same turn the script ran may still see the old list. Falling back once and binding the tier on the next turn is correct behaviour, not a failure.
