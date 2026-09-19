---
name: setup-routing-for-claude
description: Install a Claude Code UserPromptSubmit hook that classifies every prompt with classifier.dev and speaks only when the verdict changes, writing a route recommendation for the model to act on. Run once per repository.
disable-model-invocation: true
---

# Setup Routing for Claude

Classification only happens if the model remembers to trigger it first, and reasoning about a task before classifying it bends the verdict toward whatever was already being planned. A `UserPromptSubmit` hook closes that gap: it runs outside the model's control, on every prompt, before any reasoning starts. It stays silent unless the verdict *changes* from the previous prompt in the session, so the `route:` line it writes into context means a boundary: work starting, ending, or shifting shape.

## What works where

- **Claude Code**: fully supported (`UserPromptSubmit` command hook). This setup's only path.
- **OpenCode / Codex CLI**: neither exposes a `UserPromptSubmit` hook. There is no fallback here; routing on those harnesses stays manual.

## Steps

### 1. Copy the hook script

The bundled script is at [scripts/classify-and-route.sh](scripts/classify-and-route.sh).

Copy to `.claude/hooks/classify-and-route.sh` and make it executable (`chmod +x`).

### 2. Register the hook

In `.claude/settings.json` (project scope; hooks cannot be scoped tighter), merge into the existing `hooks` object:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/classify-and-route.sh"
          }
        ]
      }
    ]
  }
}
```

Do not overwrite other hooks; merge the array.

### 3. Verify

- [ ] `.claude/hooks/classify-and-route.sh` exists and is executable
- [ ] `.claude/settings.json` parses (`jq . .claude/settings.json`) and carries the `UserPromptSubmit` entry
- [ ] A prompt that should route (remove any `${TMPDIR:-/tmp}/classify-and-route-*.json` left by earlier tests first):

```bash
echo '{"user_prompt":"rename this variable to snake_case"}' | .claude/hooks/classify-and-route.sh
```

Expect a `systemMessage` shaped `Route: Implementation or refactoring (...) | Fast and simple (...)...`.

- [ ] The same prompt again, unchanged: expect `{"continue":true}` with no `systemMessage`, because the verdict did not change.
- [ ] A prompt that should not route:

```bash
echo '{"user_prompt":"hey, thanks"}' | .claude/hooks/classify-and-route.sh
```

Expect `{"continue":true}` with no `systemMessage`.

### 4. Tell the user a restart is required

Hooks load only at session start; there is no hot-swap. Tell the user to restart Claude Code before the hook takes effect.

## Notes

- Fails open: a missing `jq`/`curl`, a classifier timeout, error, or `429` all emit `{"continue":true}` with no `systemMessage`, never blocking the turn.
- Fires only on change: the verdict is classified on every prompt (`curl --max-time 4` bounds the cost) but announced only when the task label or complexity label differs from the previous prompt's, and never for a transition to `Undefined`. The last verdict lives in `${TMPDIR:-/tmp}/classify-and-route-<session id>.json`, one file per session, reaped by the reboot.
- The hook only recommends; it never dispatches anything itself. Which skill or agent fits the verdict, and whether the turn is a fresh unit of work at all, stays the model's judgement.
- Needs `jq` and `curl` on `PATH`.
