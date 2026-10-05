#!/usr/bin/env bash
# Nightly invoice export (invented example).
set -euo pipefail

LOCK=/var/run/harbor-export.lock
if [ -e "$LOCK" ]; then
  echo "export already running or stale lock at $LOCK" >&2
  exit 75
fi
trap 'rm -f "$LOCK"' EXIT
echo $$ > "$LOCK"

/opt/harbor/bin/build-csv --out /srv/exports/invoices.csv
/opt/harbor/bin/upload /srv/exports/invoices.csv s3://harbor-exports/nightly/
