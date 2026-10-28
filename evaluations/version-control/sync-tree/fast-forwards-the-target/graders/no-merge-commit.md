---
type: regex
target:
  source: file
  path: .git/logs/HEAD
pattern: 'commit \(merge\)'
flags: m
match: not_contains
---
