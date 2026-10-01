#!/bin/bash

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command')

DANGEROUS_PATTERNS=(
  "git reset --hard"
  "git clean -fd"
  "git clean -f"
  "git branch -D"
  "git checkout \."
  "git restore \."
  "reset --hard"
)

for pattern in "${DANGEROUS_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qE "$pattern"; then
    echo "BLOCKED: '$COMMAND' matches dangerous pattern '$pattern'. The user has prevented you from doing this." >&2
    exit 2
  fi
done

# Commits and pushes are allowed only after the user confirms the exact command.
# Every segment is checked for blocks first; confirmation is requested once at the end.
ASK=""

while IFS= read -r COMMIT; do
  [ -z "$COMMIT" ] && continue
  ASK="$ASK Commit requested: $COMMIT."
done < <(echo "$COMMAND" | grep -oE 'git commit[^;&|]*')

while IFS= read -r PUSH; do
  [ -z "$PUSH" ] && continue

  # Force, deletion, mirroring, and refspec pushes rewrite or remove remote history.
  if echo "$PUSH" | grep -qE '(^|[[:space:]])(-f|-d|--force[^[:space:]]*|--delete|--mirror|--all|--prune)([[:space:]]|$)|[[:space:]]\+|[[:space:]][^[:space:]]*:'; then
    echo "BLOCKED: '$PUSH' is a force, delete, mirror, or refspec push. The user has prevented you from doing this." >&2
    exit 2
  fi

  # Remote and branch must both be named, so the user confirms the branch that moves.
  POSITIONALS=$(echo "$PUSH" | sed -E 's/^git push//' | tr -s ' ' '\n' | grep -cvE '^(-.*)?$')
  if [ "$POSITIONALS" -lt 2 ]; then
    echo "BLOCKED: '$PUSH' does not name both remote and branch. Rerun as 'git push <remote> <branch>' so the user can confirm the branch." >&2
    exit 2
  fi

  ASK="$ASK Push requested: $PUSH. Allow only if this remote and branch are the intended target."
done < <(echo "$COMMAND" | grep -oE 'git push[^;&|]*')

if [ -n "$ASK" ]; then
  jq -n --arg reason "${ASK# }" \
    '{hookSpecificOutput: {hookEventName: "PreToolUse", permissionDecision: "ask", permissionDecisionReason: $reason}}'
fi

exit 0
