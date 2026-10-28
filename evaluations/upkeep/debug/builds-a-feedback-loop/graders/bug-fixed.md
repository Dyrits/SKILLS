---
type: regex
target:
  source: file
  path: pricing.py
pattern: 'def\s+checkout\([^)]*applied\s*=\s*\[\]'
flags: m
match: not_contains
---
