Upstream source: `wizard`, verified in the `d81f3a1` tree, renamed `walk-through` in this fork so the name reads as a command. The script it produces is still called a wizard.

## What it does

`walk-through` generates an interactive bash script that walks a human, step by step, through a manual procedure: wiring up third-party services, running a one-off migration, moving a project from state A to state B. It opens each URL, says what to click and copy, captures what comes back, and writes it into `.env` files and GitHub Actions secrets.

The agent writes the script; it never runs it. You do, on your own machine. So a wizard is not a list of instructions you follow; it is a program that drives the procedure and holds the state, and your part is to click, paste, and press Enter.

## When to reach for it

You can type `/walk-through`, and the agent can also reach for it on its own. When it hits a step you have to take (a key it can't mint, a dashboard it can't click), it builds you a wizard instead of writing the instructions into the chat, where they scroll away.

Reach for it when the next thing blocking you is a trip through a dashboard:

| Situation | What the wizard does |
| --- | --- |
| A new dev needs six services configured before the app boots | Opens each dashboard in order, captures the keys, writes them to `.env` and CI |
| A one-off migration needs switches flipped in a specific order | Sequences the irreversible steps behind confirmation gates |
| A project has to move from state A to state B once | Walks the transition and reports what it could not do |
| You are about to write those steps into a README | Writes an executable version instead, which can't rot as quietly |

To decide what to build, use [refine](../reference/refine.md); to record agreed capability behavior, use [specify](../workflow/specify.md). A wizard handles manual execution after the procedure is understood.

## Prerequisites

None to generate one. The wizard it writes runs on bash, and uses `gh` when a stage sets a GitHub secret or variable. If `gh` is missing or unauthenticated, that stage becomes a warning and the closing summary tells you what to set by hand, instead of failing the run.

## Stages

A **stage** is one focused task on one screen. The script clears the terminal between stages, so a stage that overflows the screen loses the part that scrolled away. You author stages in dependency order and set `TOTAL_STAGES`, which drives the progress display.

Scoping happens before the script is written. The agent reads environment files, service configuration, and `secrets.*` or `vars.*` references in CI to find the values the wizard must produce. It shows you the ordered stages for confirmation, then maps them to the human procedure. Where it does not know the current dashboard, it asks you or checks official documentation rather than inventing clicks.

For each captured value, scoping settles where it lands:

| Destination | When |
| --- | --- |
| `.env` only | Local dev needs it, CI doesn't |
| GitHub secret | CI reads it, and it's sensitive |
| GitHub variable | CI reads it, and it's public |
| Both `.env` and a secret | Local dev and CI both need it |
| Nowhere | The stage is a pure action: a switch flipped, a plan upgraded |

## The template already solves the UX

The [template](../../../skills/productivity/walk-through/template.sh) supplies progress, confirmation gates, cross-platform URL opening including WSL, hidden entry for secrets, idempotent `.env` upserts, `gh secret` / `gh variable` writes, and a closing summary of skipped actions. Its fixed library stays unchanged; the agent scopes the procedure and authors its stages.

The agent that writes a wizard never runs it end to end, because it opens browsers and waits for human input. It verifies statically instead: `bash -n`, `shellcheck` where available, and a trace that every value lands where scoping said it would, with every `set_secret` name matching a real `secrets.*` reference in CI. Set your expectations accordingly: the first run is yours, and that run is the test.

## Ephemeral by default

| What you have | What to do with the script |
| --- | --- |
| A one-off migration, a personal setup, a transition you'll never repeat | Save it to a scratch or `scripts/` path, run it, delete it |
| A setup path the next person on the repository will also need | Commit it and link it from the README, so they run the script instead of re-asking an agent |

## Common questions

**Do my API keys end up in the model's context?**

No. The agent writes a script; it doesn't run it. You run the script yourself, and it captures the key with hidden terminal entry and writes it straight to `.env` or `gh secret`. The wizard is a CLI, and the model is not connected to it. One caveat: that holds for values the wizard captures at runtime. If you paste a key into the chat while scoping the procedure, it's in the context like any other pasted text.

**Can I go back and fix a value I mistyped?**

Not mid-run. There is no back button: the stages run forward, and a wrong answer on stage 3 means Ctrl-C and re-run. Re-running is cheap by design: any value already written to `.env` is offered back as a default, so you press Enter through the stages you got right and retype only the wrong one. This came up in the launch week and hasn't been closed since: "loved it! One thing though, is there a way to go back and correct what you've entered?"

There's a related open bug. Arrow keys in an `ask` prompt insert `^[[D` / `^[[C` instead of moving the cursor, because the prompt uses `read -r` rather than Readline ([issue #741](https://github.com/mattpocock/skills/issues/741)). Backspace works; arrow keys don't. Delete back to the mistake rather than moving the cursor into it.

**Does it know what I've already set up?**

Partly, and less than the launch reactions assumed. It reads the repository before it asks (your `.env` files, `docker-compose`, framework config, the `secrets.*` references in CI), so it scopes to values that are genuinely missing rather than starting from zero the way a README does. What it doesn't do is check the third-party service. If a key exists in your `.env` the wizard offers it back and Enter keeps it; if you already created the Stripe account but never saved the key, the wizard still sends you to the dashboard for it.

**Where does it sit in the workflow, after grilling and the specification?**

Nowhere in particular. It is a standalone, not a chain step. A manual procedure can appear before development, during a build, or after delivery. Scoping can also uncover hidden prerequisites, such as API keys you had not accounted for. Generating a script does not approve its irreversible actions; its confirmation gates remain part of the human run.

**Does it work outside Claude Code?**

The artifact does, unconditionally: it's a plain bash script and it doesn't care what harness generated it. The skill itself is model-invoked, so it's listed everywhere: type `/walk-through` in Claude Code or `$wizard` in Codex, or just describe the setup you're stuck on. Being model-invoked also keeps it clear of [#693](https://github.com/mattpocock/skills/issues/693), where Claude's desktop and web surfaces drop *user-invoked* skills from the model's listing and report them as not installed.

**Didn't this used to be user-invoked?**

It did. It's now model-invoked, so the agent reaches for it unprompted when it hits a step you have to take. Nothing you could do before stopped working: model-invocation *adds* the agent's reach, it never removes yours, so `/walk-through` behaves exactly as it did. What changed is the failure mode it retires: the agent hitting a credentials wall mid-build and dumping six numbered steps into the chat for you to follow by hand.

**It used to be in `work-in-progress/`: where is it now?**

It graduated upstream into `engineering/` in v1.2. This fork places it in `reference/`, and its manifest entry includes it in the plugin. A bucket move alone does not promote a skill.

## It's working if

- You're shown an ordered list of stages, and the values each one produces, and asked to confirm, before any script exists.
- Every URL is opened before the value from that page is asked for. You're never asked to paste something you haven't been sent to fetch.
- Secrets are typed blind. Nothing sensitive echoes into your scrollback.
- Each stage fits one screen. Nothing you still need has scrolled away.
- Ctrl-C and re-run picks up where you left off, offering the values already saved as defaults.
- The final screen lists what it wrote, and separately lists what it couldn't do and you have to finish by hand.

## Where it fits

`walk-through` is a reach-for-it-anytime standalone for the steps only a human can perform. [setup-ai-workspace](../getting-started/setup-ai-workspace.md) configures this skill set; a wizard handles other manual setup. [implement](../workflow/implement.md) may expose a credentials or cutover step that needs one. [guide](../getting-started/guide.md) routes you when the next move is unclear.
