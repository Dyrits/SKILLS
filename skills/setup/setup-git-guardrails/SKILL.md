---
name: setup-git-guardrails
description: Set up hooks and permission rules that make coding agents ask before git commands that can lose work or rewrite shared history (pushing to a protected branch, force pushes, reset --hard, clean -f, branch -D, discarding changes) across Claude Code, OpenCode, and Codex CLI. Use when the user wants to guard against destructive git operations by any coding agent.
metadata:
  forks: "mattpocock/skills/skills/misc/git-guardrails-claude-code"
---

# Setup Git Guardrails

Puts a confirmation in front of destructive git commands, so the human approves each one instead of the agent running it unchecked. Routine work (commits, pushes to feature branches, dry runs) passes without a prompt. Works across Claude Code, OpenCode, and Codex CLI.

## What asks for confirmation

- `git push` to a protected branch (`main`, `master`, and the remote's default branch), a plain force push (`--force`, `-f`, a `+` refspec), and pushes that delete or mirror (`--delete`, `:branch`, `--mirror`, `--all`, `--prune`). `--force-with-lease` to a feature branch and `--dry-run` pass.
- `git reset --hard`
- `git clean` with `-f`, unless it is a dry run (`-n`)
- `git branch -D` (or `--delete --force`)
- `git checkout .` and `git checkout -- <paths>`
- `git restore` on the working tree (`--staged` alone passes)

The Claude Code script matches only the command being run, segment by segment across `&&`, `||`, `;`, and `|`: text that merely mentions a command (`echo "git push"`, a commit message) passes.

## Steps

### 1. Ask scope and targets

Ask the user:

- **Scope**: this project only, or all projects (global config)?
- **Targets**: which agents? Claude Code, OpenCode, Codex CLI, or all of them. Default: all detected ones (check for `.claude/`, `.opencode/`/`opencode.json`, `.codex/` config presence).
- **Protected branches**: keep `main` and `master` (the remote's default branch is always included), or add others such as `develop`.

### 2. Install the Claude Code script

The bundled script is at: [scripts/confirm-dangerous-git.sh](scripts/confirm-dangerous-git.sh)

Copy it to `.claude/hooks/confirm-dangerous-git.sh` (project) or `~/.claude/hooks/confirm-dangerous-git.sh` (global) and `chmod +x`. Set `PROTECTED_BRANCHES` at its top to the branches from step 1.

### 3. Wire up each agent

For **Claude Code**, add to `.claude/settings.json` (project) or `~/.claude/settings.json` (global):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/confirm-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

(For global scope use `~/.claude/hooks/confirm-dangerous-git.sh` as the command.) The script answers with `permissionDecision: "ask"`, which shows the user the normal permission prompt with the reason.

For **OpenCode**, use its permission system in `opencode.json` (project) or `~/.config/opencode/opencode.json` (global). Rules are globs over the parsed command, and the **last matching rule wins**, so each exception follows the rule it narrows. Globs cannot read the current branch, so every non-dry-run push asks:

```json
{
  "permission": {
    "bash": {
      "git push": "ask",
      "git push *": "ask",
      "git push --dry-run*": "allow",
      "git reset --hard*": "ask",
      "git clean -*f*": "ask",
      "git clean -n*": "allow",
      "git clean --dry-run*": "allow",
      "git branch -D *": "ask",
      "git checkout .": "ask",
      "git checkout -- *": "ask",
      "git restore *": "ask",
      "git restore --staged *": "allow"
    }
  }
}
```

Merge into an existing `permission.bash` block, keeping its catch-all `"*"` rule first.

For **Codex CLI**, use the Git-level fallback: it has no hook scripts and supports sandbox and approval policy in `~/.codex/config.toml` but no per-command rules. Install a versioned `pre-push` hook (see step 5) and rely on remote branch protection. Tell the user Codex cannot be guarded at the configuration level.

### 4. Ask about customization

Ask if the user wants to add or remove guarded commands. Edit the copied script and the OpenCode rules accordingly.

### 5. Offer the git-level fallback

For any agent that cannot be intercepted (Codex, or future tools), offer the portable layer: a versioned `pre-push` hook via `core.hooksPath` that refuses pushes to protected branches, and protected branches on the remote. These apply no matter which agent runs `git push`.

### 6. Verify

For the Claude Code script, from inside the repository:

```bash
echo '{"tool_input":{"command":"git push origin main"},"cwd":"'"$PWD"'"}' | <path-to-script>
echo '{"tool_input":{"command":"echo \"git push origin main\""},"cwd":"'"$PWD"'"}' | <path-to-script>
```

The first prints JSON with `"permissionDecision": "ask"`; the second prints nothing. Both exit 0.

OpenCode rules: ask the user to run `git push origin main` in a session and confirm OpenCode prompts for it (or check `opencode.json` parses and the rules are listed).

## Notes

- A confirmation needs a human to answer it. In a non-interactive session nobody can, so expect the guarded command to be refused there.
- Keep the script's checks and the OpenCode rules in sync when customizing.
