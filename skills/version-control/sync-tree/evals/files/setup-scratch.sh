#!/bin/sh
# Build a scratch original repository and a linked task worktree with one committed change.
# Usage: sh setup-scratch.sh <empty-directory> <scenario>
# Layout: <dir>/orig (original checkout), <dir>/task (linked worktree on worktree/csv-export).
# Scenarios:
#   fast-forward  orig is on main, clean; main is an ancestor of the task commit
#   dirty-target  as fast-forward, but orig has an uncommitted edit to README.md
#   diverged      orig is on branch scratch; main also has a commit the task branch lacks
#   synced        orig is on branch scratch; main already equals the task commit
#   uncommitted   as fast-forward, but the task worktree has an uncommitted edit
#   unchecked     orig is on branch scratch; main is an ancestor of the task commit and not checked out
#   target-ahead  orig is on branch scratch; main already contains the task commit plus one more
set -eu
dir="$1"; scenario="$2"
mkdir -p "$dir" && cd "$dir"
git init -q -b main orig && cd orig
git config user.name "Eval Bot" && git config user.email "eval@example.test"
echo "# Demo" > README.md && echo "id,name" > data.csv
git add -A && git commit -q -m "Initial commit"
git worktree add -q -b worktree/csv-export ../task main
(cd ../task && echo "export_csv()" > export.py && git add -A && git commit -q -m "Add CSV export")
case "$scenario" in
  fast-forward) ;;
  dirty-target) echo "scratch notes" >> README.md ;;
  diverged)
    echo "hotfix" > hotfix.txt && git add -A && git commit -q -m "Hotfix on main"
    git checkout -q -b scratch ;;
  synced)
    git checkout -q -b scratch
    git branch -f main worktree/csv-export ;;
  unchecked) git checkout -q -b scratch ;;
  target-ahead)
    git checkout -q -b scratch
    git branch -f main worktree/csv-export
    git checkout -q main && echo "later" > later.txt && git add -A && git commit -q -m "Later work on main" && git checkout -q scratch ;;
  uncommitted) echo "wip" >> ../task/export.py ;;
  *) echo "unknown scenario" >&2; exit 1 ;;
esac
git worktree list
