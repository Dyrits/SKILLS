#!/usr/bin/env bash
set -euo pipefail
export GIT_AUTHOR_NAME=Eval GIT_AUTHOR_EMAIL=eval@example.com GIT_COMMITTER_NAME=Eval GIT_COMMITTER_EMAIL=eval@example.com
git init -q -b main
git config user.name Eval
git config user.email eval@example.com
git config commit.gpgsign false
echo "# Project" > README.md
printf '.worktrees/\n' > .gitignore
git add -A && git commit -qm "Initial commit"
base=$(git rev-parse HEAD)
git worktree add -q -b worktree/notes .worktrees/notes "$base"
echo "Release checklist" > .worktrees/notes/NOTES.md
git -C .worktrees/notes add NOTES.md
git -C .worktrees/notes commit -qm "Add the release checklist"
printf 'repository=%s\nbranch=main\nbase=%s\ntask-branch=worktree/notes\n' "$PWD" "$base" > "$(git -C .worktrees/notes rev-parse --absolute-git-dir)/return-destination"
