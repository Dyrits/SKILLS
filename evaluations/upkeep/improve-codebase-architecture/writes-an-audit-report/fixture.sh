#!/usr/bin/env bash
set -euo pipefail
export GIT_AUTHOR_NAME=Eval GIT_AUTHOR_EMAIL=eval@example.com GIT_COMMITTER_NAME=Eval GIT_COMMITTER_EMAIL=eval@example.com
git init -q -b main
git config user.name Eval
git config user.email eval@example.com
git config commit.gpgsign false
mkdir -p src
printf 'import { saveUser } from "./userRepository";\nexport const createUser = (name) => saveUser({ name });\n' > src/userService.js
printf 'import { insert } from "./db";\nexport const saveUser = (user) => insert("users", user);\n' > src/userRepository.js
printf 'const rows = {};\nexport const insert = (table, row) => { (rows[table] ||= []).push(row); return row; };\n' > src/db.js
printf 'import { createUser } from "./userService";\nexport const handleSignup = (req) => createUser(req.body.name);\n' > src/userController.js
git add -A && git commit -qm "Initial commit"
git commit -q --allow-empty -m "Tweak user signup"
