# Wiring examples

Two worked hookups for the agent layer. They show the shape of each mechanism, not the list of supported harnesses. Check the harness's current documentation before copying either.

## A pre-command hook (Claude Code)

In `.claude/settings.json` (project) or `~/.claude/settings.json` (global). The `ask-json` format makes the normal permission prompt show the reason:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 -I \"$CLAUDE_PROJECT_DIR\"/.agents/hooks/guard-git.py --level 2 --protected main,master --format ask-json"
          }
        ]
      }
    ]
  }
}
```

For global scope, use the absolute path `~/.agents/hooks/guard-git.py` expanded.

## Permission rules (OpenCode)

In `opencode.json` (project) or `~/.config/opencode/opencode.json` (global). Rules are globs over the parsed command, and the last matching rule wins, so each exception follows the rule it narrows. Globs cannot read the current branch, so every non-dry-run push asks. Merge into an existing `permission.bash` block, keeping its catch-all `"*"` rule first. Add the blocks cumulatively up to the chosen level.

Level 1:

```json
{
  "permission": {
    "bash": {
      "git push": "ask",
      "git push *": "ask",
      "git push --dry-run*": "allow"
    }
  }
}
```

Level 2 adds:

```json
{
  "git reset --hard*": "ask",
  "git clean -*f*": "ask",
  "git clean -n*": "allow",
  "git clean --dry-run*": "allow",
  "git branch -D *": "ask",
  "git checkout .": "ask",
  "git checkout -- *": "ask",
  "git checkout -f*": "ask",
  "git switch --discard-changes*": "ask",
  "git restore *": "ask",
  "git restore --staged *": "allow",
  "git stash drop*": "ask",
  "git stash clear*": "ask",
  "git worktree remove --force*": "ask",
  "git reflog expire*": "ask",
  "git gc --prune*": "ask"
}
```

Level 3 adds:

```json
{
  "git rebase*": "ask",
  "git reset *": "ask",
  "git commit --amend*": "ask",
  "git tag -d *": "ask",
  "git branch -d *": "ask",
  "git filter-branch*": "ask"
}
```
