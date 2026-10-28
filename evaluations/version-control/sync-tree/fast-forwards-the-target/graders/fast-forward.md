---
type: regex
target:
  source: file
  path: .git/logs/refs/heads/main
pattern: 'Fast-forward|update-ref|merge'
flags: m
---
