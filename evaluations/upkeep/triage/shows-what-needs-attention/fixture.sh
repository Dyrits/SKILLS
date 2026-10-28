#!/usr/bin/env bash
set -euo pipefail
export GIT_AUTHOR_NAME=Eval GIT_AUTHOR_EMAIL=eval@example.com GIT_COMMITTER_NAME=Eval GIT_COMMITTER_EMAIL=eval@example.com
git init -q -b main
git config user.name Eval
git config user.email eval@example.com
git config commit.gpgsign false
mkdir -p tasks
printf 'The task tracker is local: one Markdown body per task in tasks/, with Category: and Status: lines near the top.\n' > AGENTS.md
printf '# CSV export drops the last row\n\nExporting 10 rows gives a file with 9.\n' > tasks/001-csv-export-drops-last-row.md
printf '# Dark mode\n\nCategory: enhancement\nStatus: to-evaluate\n\nUsers ask for a dark theme.\n' > tasks/002-dark-mode.md
printf '# Use the v2 search API\n\nCategory: enhancement\nStatus: on-hold\n\nWaiting on: the v2 search API release (task 4).\n' > tasks/003-use-v2-search.md
printf '# Release the v2 search API\n\nCategory: enhancement\nStatus: ready\n\n## Comments\n\n2026-10-20: v2 search API released.\n' > tasks/004-release-v2-search.md
printf '# Fix login redirect\n\nCategory: bug\nStatus: ready\n\nBrief attached.\n' > tasks/005-fix-login-redirect.md
git add -A && git commit -qm "Initial commit"
