---
name: setup-auto-handoff
description: Set up a Claude Code PreCompact hook that blocks compaction until a fresh handoff exists in .agents/handoffs/, so a session reaching its context limit never loses the conversation to auto-compact. Use when the user wants automatic handoff on context-limit, or to protect long sessions from compaction data loss.
---

# Setup Auto-Handoff

Gates compaction: when Claude Code is about to compact (auto or manual), a `PreCompact` hook blocks it unless a handoff was written to `.agents/handoffs/` in the last 5 minutes. The block reason tells the agent to run the `handoff` skill first; the next compaction attempt passes once the handoff exists.

## What works where

- **Claude Code**: fully supported (`PreCompact` hook). This setup's main path.
- **OpenCode / Codex**: no pre-compact hook exists. The fallback is their persisted transcripts (`codex resume`, OpenCode session storage) plus the user's habit of running `handoff` at phase boundaries. Tell the user this plainly; do not fake coverage.

## Steps

### 1. Copy the hook script

The bundled script is at [scripts/precompact-handoff-gate.sh](scripts/precompact-handoff-gate.sh)

Copy to `.claude/hooks/precompact-handoff-gate.sh` and make it executable (`chmod +x`).

### 2. Register the hook

In `.claude/settings.json` (project scope; hooks cannot be scoped tighter), merge into the existing `hooks` object:

```json
{
  "hooks": {
    "PreCompact": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/precompact-handoff-gate.sh"
          }
        ]
      }
    ]
  }
}
```

Do not overwrite other hooks; merge the array.

### 3. Verify

- [ ] `.claude/hooks/precompact-handoff-gate.sh` exists and is executable
- [ ] `.claude/settings.json` parses (`jq . .claude/settings.json`) and carries the `PreCompact` entry
- [ ] Simulate an auto-compact with no fresh handoff:

```bash
echo '{"trigger":"auto"}' | .claude/hooks/precompact-handoff-gate.sh; echo "exit: $?"
```

Expect a JSON `decision: block` on stdout and exit code 0.

- [ ] Simulate with a fresh handoff:

```bash
mkdir -p .agents/handoffs && touch .agents/handoffs/test.md
echo '{"trigger":"auto"}' | .claude/hooks/precompact-handoff-gate.sh; echo "exit: $?"
rm .agents/handoffs/test.md
```

Expect empty output, exit code 0.

### 4. Tell the user the loop

When the context limit hits: auto-compact fires, the hook blocks it with the instruction, the agent runs `handoff` (a fresh file lands in `.agents/handoffs/`), compaction retries and passes. If compaction is ever truly unwanted, the user can remove the hook from `.claude/settings.json`. Manual `/compact` is gated the same way; `/clear` is not affected (it is a different event).

## Notes

- The 5-minute freshness window stops a stale handoff from an hour ago satisfying the gate. Edit `FRESH_WINDOW_MINUTES` in the script to tune.
- The gate creates `.agents/handoffs/` if missing, so the first blocked compaction is also the first handoff.
- The hook needs `jq` on PATH; check and tell the user if absent.
