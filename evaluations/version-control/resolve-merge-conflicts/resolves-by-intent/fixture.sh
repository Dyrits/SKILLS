#!/usr/bin/env bash
set -euo pipefail
export GIT_AUTHOR_NAME=Eval GIT_AUTHOR_EMAIL=eval@example.com GIT_COMMITTER_NAME=Eval GIT_COMMITTER_EMAIL=eval@example.com
git init -q -b main
git config user.name Eval
git config user.email eval@example.com
git config commit.gpgsign false
printf 'timeout = 10\n' > config.ini
printf '#!/usr/bin/env bash\ngrep -q "^request_timeout = " config.ini && ! grep -q "^timeout" config.ini && echo ok\n' > check.sh
chmod +x check.sh
printf 'Run ./check.sh before committing.\n' > AGENTS.md
git add -A && git commit -qm "Initial commit"
git checkout -qb feature
printf 'request_timeout = 10\n' > config.ini
printf '#!/usr/bin/env bash\ngrep -q "^request_timeout = " config.ini && ! grep -q "^timeout" config.ini && echo ok\n' > check.sh
git commit -qam "Rename timeout to request_timeout to match the new client library"
git checkout -q main
printf 'timeout = 30\n' > config.ini
git commit -qam "Raise the timeout to 30 seconds for slow mobile networks"
git merge feature >/dev/null 2>&1 || true
test -f .git/MERGE_HEAD
