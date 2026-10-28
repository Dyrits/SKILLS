---
type: regex
target:
  source: file
  path: config.ini
pattern: '^(<<<<<<<|=======|>>>>>>>|timeout\s*=)'
flags: m
match: not_contains
---
