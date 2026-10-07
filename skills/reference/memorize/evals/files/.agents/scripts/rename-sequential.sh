#!/usr/bin/env bash
# Renames every file in a directory to <prefix>-NNN.<extension>, numbered from 001 in name order.
# Arguments: <directory> <prefix>
# Usage: rename-sequential.sh photos 2026-trip
# Changes: renames files in place; prints each rename.
set -euo pipefail
directory="$1"
prefix="$2"
count=0
for path in "$directory"/*; do
  [ -f "$path" ] || continue
  count=$((count + 1))
  extension="${path##*.}"
  target="$directory/$(printf '%s-%03d.%s' "$prefix" "$count" "$extension")"
  echo "$path -> $target"
  mv -n "$path" "$target"
done
