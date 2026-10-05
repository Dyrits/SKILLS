#!/bin/sh
# Build a scratch repository stopped on a merge conflict.
# Usage: sh setup-scratch.sh <empty-directory> [rebase]
# Result: branch "feature/discount" has `main` merged in and stopped on one conflict region in
# billing.py that mixes a compatible change (rounding vs discount) and an incompatible one
# (default currency USD vs EUR). `make check` runs python3 -m unittest.
# With "rebase": feature/discount has a second, non-conflicting commit (a README note) and
# `git rebase main` is run instead, so it stops on the first commit with one more to replay.
set -eu
dir="$1"
mkdir -p "$dir" && cd "$dir"
git init -q -b main
git config user.name "Eval Bot" && git config user.email "eval@example.test"
cat > billing.py <<'PY'
DEFAULT_CURRENCY = "GBP"


def total(items):
    return sum(items)
PY
cat > test_billing.py <<'PY'
import unittest
from billing import total


class TotalTests(unittest.TestCase):
    def test_plain_total(self):
        self.assertEqual(total([10, 5]), 15)

    def test_rounds_to_cents(self):
        self.assertEqual(total([0.1, 0.2]), 0.3)

    def test_discount(self):
        self.assertEqual(total([100], discount=0.1), 90)


if __name__ == "__main__":
    unittest.main()
PY
cat > Makefile <<'MK'
check:
	python3 -m unittest -q
MK
cat > AGENTS.md <<'MD'
Run `make check` before finishing any merge or rebase.
MD
git add -A && git commit -q -m "Add billing total with GBP default"
git checkout -q -b feature/discount
cat > billing.py <<'PY'
DEFAULT_CURRENCY = "USD"


def total(items, discount=0):
    return sum(items) * (1 - discount)
PY
git commit -qam "Add discount to total and default to USD (ticket PAY-12: launch in the US market)"
if [ "${2:-}" = "rebase" ]; then
  echo "Discounts are applied as a fraction, for example 0.1 for ten percent." > README.md
  git add README.md && git commit -q -m "Document the discount parameter"
fi
git checkout -q main
cat > billing.py <<'PY'
DEFAULT_CURRENCY = "EUR"


def total(items):
    return round(sum(items), 2)
PY
git commit -qam "Round totals to cents and default to EUR (ticket PAY-7: float drift on invoices, shop moved to the euro area)"
git checkout -q feature/discount
if [ "${2:-}" = "rebase" ]; then
  git rebase main >/dev/null 2>&1 || true
else
  git merge main >/dev/null 2>&1 || true
fi
git status --short
