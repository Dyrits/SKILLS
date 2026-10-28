#!/usr/bin/env bash
set -euo pipefail
export GIT_AUTHOR_NAME=Eval GIT_AUTHOR_EMAIL=eval@example.com GIT_COMMITTER_NAME=Eval GIT_COMMITTER_EMAIL=eval@example.com
git init -q -b main
git config user.name Eval
git config user.email eval@example.com
git config commit.gpgsign false
printf '{\n  "name": "demo",\n  "scripts": {"lint": "eslint .", "test": "node --test"}\n}\n' > package.json
printf 'export default [];\n' > eslint.config.js
printf 'Write clean code.\n' > AGENTS.md
git add -A && git commit -qm "Initial commit"
