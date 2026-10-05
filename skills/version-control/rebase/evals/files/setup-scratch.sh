#!/bin/sh
# Build a scratch repository with a local bare "origin" and two feature branches.
# Usage: sh setup-scratch.sh <empty-directory>
# Result in <dir>/work (on main), with origin at <dir>/origin.git:
#   develop  has a commit that conflicts with fix/a
#   fix/a    conflicts with develop in settings.py; pushed and equal to origin/fix/a
#   feat/b   rebases cleanly; pushed and equal to origin/feat/b
#   `make check` runs python3 -m unittest
set -eu
dir="$1"
mkdir -p "$dir" && cd "$dir"
git init -q --bare -b main origin.git
git clone -q origin.git work 2>/dev/null && cd work
git config user.name "Eval Bot" && git config user.email "eval@example.test"
cat > settings.py <<'PY'
TIMEOUT_SECONDS = 30
RETRIES = 1
PY
cat > notes.txt <<'TXT'
changelog
TXT
cat > test_settings.py <<'PY'
import unittest
import settings


class SettingsTests(unittest.TestCase):
    def test_timeout_positive(self):
        self.assertGreater(settings.TIMEOUT_SECONDS, 0)

    def test_retries_not_negative(self):
        self.assertGreaterEqual(settings.RETRIES, 0)


if __name__ == "__main__":
    unittest.main()
PY
printf 'check:\n\tpython3 -m unittest -q\n' > Makefile
echo 'Run `make check` before reporting a branch as validated.' > AGENTS.md
git add -A && git commit -q -m "Initial settings" && git push -q origin main
git checkout -q -b develop && git push -q origin develop
git checkout -q -b fix/a
sed -i.bak 's/TIMEOUT_SECONDS = 30/TIMEOUT_SECONDS = 60/' settings.py && rm settings.py.bak
git commit -qam "Raise the timeout to 60 seconds (ticket OPS-31: slow exports time out)" && git push -q origin fix/a
git checkout -q develop
sed -i.bak 's/TIMEOUT_SECONDS = 30/TIMEOUT_SECONDS = 45/' settings.py && rm settings.py.bak
git commit -qam "Set the timeout to 45 seconds to match the gateway limit (ticket OPS-28)" && git push -q origin develop
git checkout -q main
git checkout -q -b feat/b
echo "added by feat/b" >> notes.txt
git commit -qam "Note the feat/b change" && git push -q origin feat/b
git checkout -q main
git branch --list
