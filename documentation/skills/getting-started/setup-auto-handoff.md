Fork-created skill: it has no upstream equivalent. Commit `f85ffd7` added it, and its session handoff records that it is new and distinct from the deleted `claude-handoff`, which launched a background agent with a summary. The [provenance audit](../../research/2026-10-03-retained-skill-provenance.md) records the evidence.

## What it does

Installs a Claude Code `PreCompact` hook that blocks compaction, automatic or manual, unless a handoff was written to `.agents/handoffs/` in the last five minutes. The block message tells the agent to run [hand-off](../productivity/hand-off.md) first, and the next compaction attempt passes once the file exists.

The five-minute window is the defining constraint: a stale handoff from earlier cannot satisfy the gate.

## When to reach for it

Type `/setup-auto-handoff`, or an agent or another skill can reach for it when you want automatic handoff at the context limit or protection for long sessions from compaction data loss.

## Prerequisites

- Claude Code, which is the only client with a pre-compact hook.
- `jq` on your path; the skill tells you if it is missing.

## What it changes

- Copies the gate script to `.claude/hooks/precompact-handoff-gate.sh` and makes it executable.
- Merges a `PreCompact` entry into `.claude/settings.json`, keeping other hooks.
- Verifies by simulating a compaction with and without a fresh handoff.

## Common questions

**What about Codex and OpenCode?**

They have no pre-compact hook, so there is no gate. The fallback is their persisted transcripts and running `hand-off` at phase boundaries. The skill tells you this plainly rather than faking coverage.

**What happens at the context limit?**

Auto-compact fires, the hook blocks it with an instruction, the agent writes a handoff, and compaction retries and passes. `/clear` is a different event and is not gated.

**Can I change the freshness window?**

Yes. Edit `FRESH_WINDOW_MINUTES` in the copied script.

**What if I do not want the gate any more?**

Remove the hook entry from `.claude/settings.json`.

## It's working if

- The simulated compaction with no fresh handoff returns a `decision: block` result.
- The same simulation with a fresh file in `.agents/handoffs/` produces no output.
- A real compaction at the context limit leaves a new handoff behind and then proceeds.

## Where it fits

Run-once setup per project, also offered as an optional stage of [setup-ai-workspace](./setup-ai-workspace.md). [hand-off](../productivity/hand-off.md) writes the handoff the gate demands, and [take-over](../productivity/take-over.md) resumes from it. [setup-ai-tooling](./setup-ai-tooling.md) records per-client recovery methods for the cases this gate cannot cover. [guide](./guide.md) routes the rest.
