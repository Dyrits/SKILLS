#!/usr/bin/env bash
set -euo pipefail
export GIT_AUTHOR_NAME=Eval GIT_AUTHOR_EMAIL=eval@example.com GIT_COMMITTER_NAME=Eval GIT_COMMITTER_EMAIL=eval@example.com
git init -q -b main
git config user.name Eval
git config user.email eval@example.com
git config commit.gpgsign false
cat > pricing.py <<'EOF'
DISCOUNTS = {"SAVE10": 0.10}


def checkout(items, codes=None, applied=[]):
    for code in codes or []:
        applied.append(DISCOUNTS[code])
    subtotal = sum(items)
    for rate in applied:
        subtotal -= subtotal * rate
    return round(subtotal, 2)
EOF
git add -A && git commit -qm "Initial commit"
