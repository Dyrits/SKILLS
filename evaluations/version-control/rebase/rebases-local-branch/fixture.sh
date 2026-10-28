#!/usr/bin/env bash
set -euo pipefail
export GIT_AUTHOR_NAME=Eval GIT_AUTHOR_EMAIL=eval@example.com GIT_COMMITTER_NAME=Eval GIT_COMMITTER_EMAIL=eval@example.com
git init -q -b main
git config user.name Eval
git config user.email eval@example.com
git config commit.gpgsign false
echo base > app.txt
printf '.worktrees/\n' > .gitignore
git add -A && git commit -qm "Initial commit"
git checkout -qb feature
echo "feature change" >> app.txt
git commit -qam "Add greeting to the app"
git checkout -q main
echo "from main" > main.txt
git add main.txt && git commit -qm "Add release notes"
git checkout -q feature
