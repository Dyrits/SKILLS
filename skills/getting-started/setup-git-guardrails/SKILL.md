---
name: setup-git-guardrails
description: Set up hooks and permission rules that block destructive git commands (reset --hard, clean, branch -D, force push) and gate commits and plain pushes behind user confirmation, across Claude Code, OpenCode, and Codex CLI, including in auto-approve mode. Use when user wants to prevent destructive git operations by any coding agent.
---

# Setup Git Guardrails

Blocks destructive git commands, and gates commits and pushes behind user confirmation, before any coding agent executes them. Works across Claude Code, OpenCode, and Codex CLI. Protection is enforced by hook scripts and permission rules, so it holds even when the agent runs in auto-approve / full-auto mode.

## What Gets Blocked

- `git push --force` and every other history-rewriting push: `-f`, `--force-with-lease`, `--delete`, `--mirror`, `--all`, `--prune`, `+branch`, and refspecs (`HEAD:main`, `:old`)
- `git reset --hard`
- `git clean -f` / `git clean -fd`
- `git branch -D`
- `git checkout .` / `git restore .`

When blocked, the agent sees a message telling it that it does not have authority to run these commands.

## What Needs Confirmation

Every `git commit` is held for the user to allow, and so is a plain `git push <remote> <branch>`. The prompt shows the exact command, so the user sees the commit message, or confirms the remote and branch, before anything happens. A push that omits the remote or branch is blocked, and the agent is told to rerun it with both named: the branch the user confirms is then always the branch that is pushed.

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

**Claude Code**: add to `.claude/settings.json` (project) or `~/.claude/settings.json` (global):

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

The script blocks with exit code 2 and answers allowed pushes with `permissionDecision: "ask"`, which prompts the user even in auto-approve mode. A chained command is checked whole: any blocked segment rejects it, otherwise one prompt covers every commit and push in it.

**OpenCode**: OpenCode has no PreToolUse hook runner; use its permission system in `opencode.json` (project) or `~/.config/opencode/opencode.json` (global). `ask` prompts the user and `deny` rejects outright, both before any approval mode. The last matching pattern wins, so list `ask` first and the `deny` rules after it:

```json
{
  "permission": {
    "bash": {
      "git commit*": "ask",
      "*git commit*": "ask",
      "git push *": "ask",
      "*git push*": "ask",
      "git push*--force*": "deny",
      "git push* -f*": "deny",
      "git push*--delete*": "deny",
      "git push*--mirror*": "deny",
      "git push*--all*": "deny",
      "git push* +*": "deny",
      "git push*:*": "deny",
      "git reset --hard*": "deny",
      "git clean -f*": "deny",
      "git branch -D*": "deny",
      "git checkout .*": "deny",
      "git restore .*": "deny",
      "*git reset --hard*": "deny",
      "*git clean -f*": "deny",
      "*git branch -D*": "deny"
    }
  }
}
```

Patterns are globs on the command string. Include both bare and `*`-prefixed variants so chained commands (`cd foo && git push`) are caught too. OpenCode cannot require a named branch, so tell the user to read the branch in the prompt before allowing. Merge into an existing `permission` block; never overwrite other rules.

**Codex CLI**: Codex has no hook scripts; it supports sandbox and approval policy in `~/.codex/config.toml` but no per-command deny list. The reliable guardrail is git itself: install a versioned `pre-push` hook (see step 5) and rely on remote branch protection. Tell the user Codex cannot be blocked at the config level.

### 4. Ask about customization

Ask if the user wants to add or remove patterns from the blocked list, or to make commits or pushes stricter (blocked outright: delete that section of the script and move its patterns to OpenCode's `deny` rules). Edit the copied script(s) and the OpenCode rules accordingly.

### 5. Offer the git-level fallback

For any agent that cannot be intercepted (Codex, or future tools), offer the portable layer: a versioned `pre-push` hook via Husky or `core.hooksPath`, and protected branches on the remote. These apply no matter which agent runs `git push`.

### 6. Verify

For each installed target:

Claude Code hook script:

```bash
echo '{"tool_input":{"command":"git push origin main"}}' | <path-to-script>
```

Should exit with code 2 and print a BLOCKED message to stderr (the branch is not named). Then confirm the two other outcomes:

```bash
echo '{"tool_input":{"command":"git push origin feature"}}' | <path-to-script>   # prints permissionDecision "ask", exit 0
echo '{"tool_input":{"command":"git commit -m test"}}' | <path-to-script>   # prints permissionDecision "ask", exit 0
echo '{"tool_input":{"command":"git push --force origin feature"}}' | <path-to-script>   # exit 2, BLOCKED
```

OpenCode rules: ask the user to have the agent run `git commit` and `git push origin <branch>` in a session and confirm OpenCode prompts for each, and that a `--force` push is refused (or check `opencode.json` parses and rules are listed).

## Notes

- Deny rules and PreToolUse hooks both fire before auto-approve: a blocked command is rejected outright, and a gated push still waits for the user.
- Keep the pattern lists in the script and in OpenCode's rules in sync when customizing.
- `git checkout .` / `git restore .` patterns use regex escaping in the shell script; OpenCode uses plain globs.
