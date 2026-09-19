# Handoff: classify and route as experimental skills

Supersedes: `.agents/handoffs/2026-09-18-0108-tracker-kinds-and-triage-roles.md`

Created 2026-09-19 17:59. Session goal: turn an ad hoc OpenCode router command into real skills, backed by classifier.dev.

## Starting point

The untracked `opencode/` folder held a `command/route.md` that classified the user's request with two `curl` calls to classifier.dev and dispatched it to an OpenCode subagent, plus two agent definitions (`build-fast`, `build-heavy`) pinning a fast and a heavy model. The session also began by removing the installed `bulk-classify` skill (`npx skills remove bulk-classify -g -y`), which had wrapped the same API.

## Decisions made this session

All the user's calls:

1. **Two skills, not one.** `route` keeps its name and owns the dispatch policy; `classify` is a new skill that classifies any text against any labels and reports the verdict. The seam: `classify` owns the transport and API semantics, `route` owns the label taxonomy and the routing table, and calls the Skill tool with `classify` rather than embedding its own `curl`. One place to change when the API moves.
2. **Both in `skills/experimental/`.** So neither is promoted: no `.claude-plugin/plugin.json` entry, no documentation page under `documentation/`. The bucket's framing in both READMEs was widened, because these two are externally visible by sending the user's text to a third-party API rather than by posting to a tracker.
3. **Both model-invoked.** The user asked for automatic classification before the agent acts, and `route` has to be able to reach `classify`, which only works when `classify` carries a description.
4. **`opencode/` deleted.** The agent definitions survive as installable snippets inside `route/SUBAGENTS.md`; the two thin command files written mid-session went with the folder.

## What changed

See the commit diff rather than a file list. The shape of it:

- `skills/experimental/classify/`: three steps (fix the labels, call it, report the verdict). Covers all three request bodies (`input`, `inputs` batch, `dimensions`), the optional `instructions` / `tier` / `multi` parameters, the size and rate limits, and the failure path. Two disciplines are the substance: one call one verdict (sharpen labels or `instructions` instead of reshuffling until a preferred answer appears), and confidence is calibrated, so a verdict below `0.7` is reported as weak rather than as settled.
- `skills/experimental/route/`: route at the top only (a table covering the subagent case, the follow-up turn whose context a subagent would not get, and the user naming an agent), then classify, then a harness-neutral **role** layer (`planner`, `explorer`, `reviewer`, `implementer-fast` / `implementer` / `implementer-heavy`), then binding, then dispatch with a one-line report. `SUBAGENTS.md` holds the per-harness bindings and the agent definitions to install.
- Improvement over the original `route.md`: one request instead of two, using classifier.dev's `dimensions` form to return task type and complexity together.
- `what-is-next` gained both skills under Standalone, and its Subagent bullet under Phase boundaries now points at `/route`.

## Verification done

Exercised classifier.dev live and confirmed the documented shapes: singular `input`, batch `inputs`, and `dimensions` with `instructions`, including a deliberately ambiguous request that returned a low complexity confidence (`0.38`), which is the calibration the `classify` skill leans on. `claude plugin validate . --strict` passes. `scripts/link-skills.sh` re-run; both skills resolve in `~/.claude/skills` and `~/.agents/skills`.

## Update 2026-09-19 18:20: first end-to-end run, and the tiers it was missing

`/route` was run for the first time, on "Write a sum js script." The classifier returned `code change` 0.99 and `simple small change` 1.00, which is the `implementer-fast` role, and the dispatch then fell all the way down to `general-purpose` at the parent model, because no tiered agents existed on the machine. The tiering that is the whole point of routing a code change had never actually happened. Everything below follows from fixing that.

### Decisions made

All the user's calls:

1. **One naming convention per harness, not one across harnesses.** Claude Code's built-ins are `Explore` and `Plan`, so its tiers are Title Case: `General`, `Fast`, `Heavy`. OpenCode's are lowercase, so its additions are `fast` and `heavy`. Route binds on an agent's **description**, not its name, so the two sets differ without breaking anything.
2. **`General` does not rename `general-purpose`, it joins it.** There is no rename: a definition only shadows a built-in when `name:` matches exactly. One convention therefore required denying the built-in, via `"permissions": {"deny": ["Agent(general-purpose)"]}` in `~/.claude/settings.json`. The harness's own lowercase `claude` default agent was deliberately left alone: it runs when no agent name is typed, and denying it may break that.
3. **A script, not a skill.** A `setup-routing-agents` skill was written into `getting-started/` and then deleted in favour of `skills/experimental/route/scripts/setup-agents.sh`. Reasons: setup is deterministic, so it does not need a model to perform it; route can launch it directly when a tier is missing; and it keeps the router's hot path free of a setup check on every dispatch. The bucket `README.md` and `what-is-next` entries added for the skill were reverted with it.
4. **A fourth tier, read-only, covering `planner`, `explorer` and `reviewer`.** It defaults to the **mid** model rather than the cheap one, because planning and review quality is what that tier decides.
5. **The read-only tier is asymmetric between harnesses, on purpose.** OpenCode pins a built-in's model through `opencode.json` and keeps its prompt, so `explore` and `plan` are pinned by default. Claude Code has no prompt-preserving equivalent: an `Explore.md` replaces the tuned built-in wholesale. That trade sits behind `--shadow-readonly`, off by default.
6. **OpenCode tiers resolve from a preference list, Claude Code tiers are fixed.** Claude Code takes the aliases `haiku`, `sonnet`, `opus`, which survive model releases. OpenCode has no alias form, so each tier carries an ordered list and the script picks the first entry whose provider is authenticated: OpenCode Go, then Z.ai, then an Anthropic backstop. The user asked to spend the OpenCode Go and Z.ai subscriptions rather than Anthropic quota.
7. **Rejected: using `/classify` to pick the agent too.** Step 2 already turns the verdict into a role by lookup and step 3 turns the role into an agent by lookup. A second classifier call would re-decide a settled question, add latency, and let two verdicts disagree.

### What changed

- New `skills/experimental/route/scripts/setup-agents.sh`, following the `<skill>/scripts/` convention `setup-git-guardrails` and `setup-auto-handoff` already use. Idempotent (`kept:` rather than clobbering, `--force` to overwrite), with `--check` reporting gaps and exiting 1, and per-tier model flags (`--read --fast --mid --heavy`, `--oc-*`) overriding the defaults outright.
- `route/SUBAGENTS.md` rewritten: the bindings table gained a model-tier column and names the tiers instead of "add one", with sections on the read-only tier, choosing the models, and what the script writes and deliberately does not touch.
- `route/SKILL.md`: step 3 runs the script when an implementer tier is missing rather than silently walking down; step 4 gained a paragraph on what a subagent does and does not inherit; the example report lines name `Heavy` and `General` instead of `build-heavy` and `build`.

### Facts established by verification, not assumption

- **OpenCode built-ins** (against a live install, resolving the previous session's open item): `build` and `plan` are **primary** agents, `general`, `explore` and `scout` are subagents. `build` is the primary session agent, not a routing target, and disabling it breaks the session.
- **OpenCode agent directory**: the documentation says `agents/` (plural); the binary contains both `agent/` and `agents/`, so the older singular is still read. Write the plural.
- **No per-agent model fallback anywhere.** OpenCode's agent entry takes `description`, `model`, `prompt`, `tools`, one model each, and Claude Code's frontmatter has no equivalent. The preference list is therefore resolved once at setup, not per request: a provider outage means re-running the script, not automatic failover. The `fallback` strings in the OpenCode binary are Bun and Solid internals.
- **Claude Code agent precedence**: managed settings, then `--agents`, then `.claude/agents/`, then `~/.claude/agents/`, then plugin agents, then built-in. Built-ins can be denied individually via `permissions.deny`; `CLAUDE_CODE_DISABLE_EXPLORE_PLAN_AGENTS=1` drops `Explore` and `Plan`; `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS=1` drops all of them but only in non-interactive mode and the Agent SDK. The last one is a trap for this use: it would remove the planner and explorer bindings.
- **New agent definitions are picked up without a session restart**, though not instantly. A dispatch in the same turn the script ran may still see the old list, which is why step 3 falls back once and binds the tier on the next turn.

### Machine state after this session

`~/.claude/agents/` holds `General` (sonnet), `Fast` (haiku), `Heavy` (opus); `~/.claude/settings.json` denies `Agent(general-purpose)`. OpenCode has `~/.config/opencode/agents/fast.md` (`opencode-go/glm-5.3-flash`) and `heavy.md` (`opencode-go/qwen3.8-max`), with `general`, `explore` and `plan` pinned to `opencode-go/glm-5.3` in `opencode.json`. None of this is in the repository: `setup-agents.sh` is what reproduces it.

## Open items for a next session

- `route` has now been run end to end once, on a trivial request that exercised only the `implementer-fast` path and its fallback. The `planner`, `explorer` and `reviewer` paths, and the heavy tier, are still unexercised. `classify` has been run end to end, both standalone and from inside `route`.
- The OpenCode heavy tier defaults to `opencode-go/qwen3.8-max`, chosen by reading model names (`-max` over `-flash`), not by benchmark. `kimi-k3`, `deepseek-v4-pro`, `minimax-m3` and `gpt-5.6-luna` are on the same plan. Revisit with evidence.
- `setup-agents.sh` has been exercised on macOS with a clean `HOME` and against the live machine, both write and `--check` paths. It has not been run on Linux, and `shellcheck` is not installed here, so it has never been linted.
- `route` running `setup-agents.sh` on its own writes to `~/.claude/settings.json` and `~/.claude/agents/` without asking. The user accepted this; it is worth revisiting if route is ever promoted out of `experimental/`, since a model-invoked skill mutating global configuration is a larger claim than an experimental one.
- The Codex CLI row is still documented from the previous session's reasoning: no delegation tool, every role inline. Unverified against a current Codex build.
- Promotion is still open: if either skill proves itself, moving it out of `experimental/` means a plugin entry, both README listings, and a documentation page per `.agents/writing-documentation.md`.

## Suggested skills

- `/writing-for-agents` before editing either `SKILL.md`, and its `SKILL-MECHANICS.md` for the invocation choice.
- `/code-review` against this session's commit for a second opinion on the two new skills.

## Git boundary

The user asked for a commit and a push at the end of this session. Verify actual local and remote state before any follow-up: this document is part of the commit and cannot record its own hash.
