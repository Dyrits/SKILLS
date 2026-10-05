#!/bin/bash
# PreToolUse guard: ask the user before a git command that can lose work or rewrite shared history.
# Only the command being run is matched: `echo "git push"` or a commit message mentioning it passes.

# Branches a push must never reach unconfirmed. The remote's default branch is added automatically.
PROTECTED_BRANCHES="main master"

INPUT=$(cat)
COMMAND=$(printf '%s' "$INPUT" | jq -r '.tool_input.command // empty')
CWD=$(printf '%s' "$INPUT" | jq -r '.cwd // empty')
[ -n "$CWD" ] || CWD=$PWD

ask() {
  jq -n --arg reason "$1" '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "ask",
      permissionDecisionReason: $reason
    }
  }'
  exit 0
}

is_protected() {
  local branch=$1 default
  default=$(git -C "$DIR" symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null)
  for protected in $PROTECTED_BRANCHES ${default#origin/}; do
    [ "$branch" = "$protected" ] && return 0
  done
  return 1
}

check_push() {
  local dry=0 forced=0 remote="" refspecs=() arg
  for arg in "$@"; do
    case $arg in
      --dry-run | -n) dry=1 ;;
      --force | -f) forced=1 ;;
      --delete | -d | --mirror | --all | --prune) ask "\`git push $arg\` can delete or overwrite remote branches." ;;
      -*) ;;
      *) if [ -z "$remote" ]; then remote=$arg; else refspecs+=("$arg"); fi ;;
    esac
  done
  [ "$dry" = 1 ] && return

  [ ${#refspecs[@]} -gt 0 ] || refspecs=(HEAD)
  local refspec destination
  for refspec in "${refspecs[@]}"; do
    case $refspec in +*) forced=1; refspec=${refspec#+} ;; esac
    case $refspec in :*) ask "\`git push $remote $refspec\` deletes a remote branch." ;; esac
    destination=${refspec#*:}
    destination=${destination#refs/heads/}
    [ "$destination" = HEAD ] && destination=$(git -C "$DIR" rev-parse --abbrev-ref HEAD 2>/dev/null)
    is_protected "$destination" && ask "This pushes to the protected branch \`$destination\`."
  done
  [ "$forced" = 1 ] && ask "A plain force push overwrites remote history; \`--force-with-lease\` passes without asking."
}

check_git() {
  local subcommand=""
  DIR=$CWD
  while [ $# -gt 0 ]; do
    case $1 in
      -C) DIR=$2; shift 2 ;;
      -c) shift 2 ;;
      -*) shift ;;
      *) subcommand=$1; shift; break ;;
    esac
  done

  local arg
  case $subcommand in
    push) check_push "$@" ;;
    reset)
      for arg in "$@"; do [ "$arg" = --hard ] && ask "\`git reset --hard\` discards uncommitted changes."; done ;;
    clean)
      local force=0 dry=0
      for arg in "$@"; do
        case $arg in
          --dry-run) dry=1 ;;
          --force) force=1 ;;
          --*) ;;
          -*) [[ $arg == *n* ]] && dry=1; [[ $arg == *f* ]] && force=1 ;;
        esac
      done
      [ "$force" = 1 ] && [ "$dry" = 0 ] && ask "\`git clean\` deletes untracked files." ;;
    branch)
      local delete=0 force=0
      for arg in "$@"; do
        case $arg in
          -*D*) delete=1; force=1 ;;
          --delete) delete=1 ;;
          --force) force=1 ;;
          --*) ;;
          -*) [[ $arg == *d* ]] && delete=1; [[ $arg == *f* ]] && force=1 ;;
        esac
      done
      [ "$delete" = 1 ] && [ "$force" = 1 ] && ask "\`git branch -D\` deletes a branch even when it is unmerged." ;;
    checkout)
      local after_separator=0
      for arg in "$@"; do
        if [ "$after_separator" = 1 ] || [ "$arg" = . ]; then
          ask "\`git checkout\` on paths discards uncommitted changes to them."
        fi
        [ "$arg" = -- ] && after_separator=1
      done ;;
    restore)
      local staged=0 worktree=0
      for arg in "$@"; do
        case $arg in
          --staged | -S) staged=1 ;;
          --worktree | -W) worktree=1 ;;
        esac
      done
      { [ "$staged" = 0 ] || [ "$worktree" = 1 ]; } && ask "\`git restore\` discards uncommitted changes in the working tree." ;;
  esac
}

# Check each command in a chain separately, skipping leading environment assignments.
while IFS= read -r segment; do
  read -ra words <<<"$segment"
  while [ ${#words[@]} -gt 0 ] && [[ ${words[0]} == *=* ]]; do words=("${words[@]:1}"); done
  [ "${words[0]}" = git ] && check_git "${words[@]:1}"
done < <(printf '%s\n' "$COMMAND" | awk '{ gsub(/&&|\|\||;|\|/, "\n"); print }')

exit 0
