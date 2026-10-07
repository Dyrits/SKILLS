#!/usr/bin/env bash
# Exports every invoice of the given month to ./exports/<month>.csv.
# Usage: export-invoices.sh 2026-09
set -euo pipefail
month="$1"
mkdir -p exports
sqlite3 -csv ledger.db "SELECT id, number, total FROM invoices WHERE month = '$month'" > "exports/$month.csv"
