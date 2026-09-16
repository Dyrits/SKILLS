---
name: setup-git-guardrails
description: Set up hooks and permission rules that block dangerous git commands (push, reset --hard, clean, branch -D, etc.) across Claude Code, OpenCode, and Codex CLI before they execute, including in auto-approve mode. Use when user wants to prevent destructive git operations by any coding agent.
---

# Setup Git Guardrails

Blocks dangerous git commands before any coding agent executes them. Works across Claude Code, OpenCode, and Codex CLI. Protection is enforced by hook scripts and permission rules, so it holds even when the agent runs in auto-approve / full-auto mode.

## What Gets Blocked

- `git push` (all variants including `--force`)
- `git reset --hard`
- `git clean -f` / `git clean -fd`
- `git branch -D`
- `git checkout .` / `git restore .`

When blocked, the agent sees a message telling it that it does not have authority to run these commands.

## Steps

### 1. Ask scope and targets

Ask the user:

- **Scope**: this project only, or all projects (global config)?
- **Targets**: which agents? Claude Code, OpenCode, Codex CLI, or all of them. Default: all detected ones (check for `.claude/`, `.opencode/`/`opencode.json`, `.codex/` config presence).

### 2. Install the hook script

The bundled script is at: [scripts/block-dangerous-git.sh](scripts/block-dangerous-git.sh)

Copy it to each target's hooks directory and `chmod +x`:

- **Claude Code project**: `.claude/hooks/block-dangerous-git.sh`
- **Claude Code global**: `~/.claude/hooks/block-dangerous-git.sh`
- **OpenCode project**: `.opencode/hooks/block-dangerous-git.sh` (script dir; referenced by config, see step 3)
- **OpenCode global**: `~/.config/opencode/hooks/block-dangerous-git.sh`
- **Codex**: no script needed, uses config-only rules (see step 4)

### 3. Wire up each agent

**Claude Code** — add to `.claude/settings.json` (project) or `~/.claude/settings.json` (global):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

(For global scope use `~/.claude/hooks/block-dangerous-git.sh` as the command.)

**OpenCode** — OpenCode has no PreToolUse hook runner; use its permission system in `opencode.json` (project) or `~/.config/opencode/opencode.json` (global). Deny rules are enforced before any approval mode, including auto-approve:

```json
{
  "permission": {
    "deny": [
      "bash(git push*)",
      "bash(git reset --hard*)",
      "bash(git clean -f*)",
      "bash(git branch -D*)",
      "bash(git checkout .*)",
      "bash(git restore .*)",
      "bash(git push --force*)",
      "bash(*git push*)",
      "bash(*git reset --hard*)",
      "bash(*git clean -f*)",
      "bash(*git branch -D*)"
    ]
  }
}
```

The `bash(...)` patterns use glob matching on the command string. Include both bare and `*`-prefixed variants so chained commands (`cd foo && git push`) are caught too. Merge into an existing `permission` block; never overwrite other rules.

**Codex CLI** — Codex has no hook scripts; it supports sandbox and approval policy in `~/.codex/config.toml` but no per-command deny list. The reliable guardrail is git itself: install a versioned `pre-push` hook (see step 5) and rely on remote branch protection. Tell the user Codex cannot be blocked at the config level.

### 4. Ask about customization

Ask if the user wants to add or remove patterns from the blocked list. Edit the copied script(s) and the OpenCode deny rules accordingly.

### 5. Offer the git-level fallback

For any agent that cannot be intercepted (Codex, or future tools), offer the portable layer: a versioned `pre-push` hook via Husky or `core.hooksPath`, and protected branches on the remote. These apply no matter which agent runs `git push`.

### 6. Verify

For each installed target:

Claude Code hook script:

```bash
echo '{"tool_input":{"command":"git push origin main"}}' | <path-to-script>
```

Should exit with code 2 and print a BLOCKED message to stderr.

OpenCode deny rules: ask the user to run `git push --dry-run` in a session and confirm OpenCode refuses it (or check `opencode.json` parses and rules are listed).

## Notes

- Deny rules and PreToolUse hooks both fire before auto-approve: the agent never sees an approval prompt because the command is rejected outright.
- Keep the pattern lists in the script and in OpenCode's deny rules in sync when customizing.
- `git checkout .` / `git restore .` patterns use regex escaping in the shell script; OpenCode uses plain globs.
