---
type: regex
target:
  source: file
  path: pricing.py
pattern: 'applied\s*=\s*\[\]'
flags: m
match: not_contains
---
