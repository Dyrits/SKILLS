#!/bin/sh
# Build a scratch repository for work-in-tree.
# Usage: sh setup-scratch.sh <empty-directory> [dirty]
# Result: <dir>/project on branch main with two commits and a test command (`make check`).
# With "dirty", an uncommitted edit to app.py is left in the working tree.
set -eu
dir="$1"
mkdir -p "$dir" && cd "$dir"
git init -q -b main project && cd project
git config user.name "Eval Bot" && git config user.email "eval@example.test"
printf 'def greet(name):\n    return "hello " + name\n' > app.py
printf 'import app\nassert app.greet("a") == "hello a"\n' > test_app.py
printf 'check:\n\tpython3 test_app.py\n' > Makefile
echo 'Worktrees for this project live in ../project-trees/<task-name>. Run `make check` before committing.' > AGENTS.md
git add -A && git commit -q -m "Add greeter"
echo "# Project" > README.md && git add -A && git commit -q -m "Add readme"
[ "${2:-}" = "dirty" ] && echo "# half-done edit" >> app.py
git status --short; git log --oneline
