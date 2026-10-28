---
description: A one-off rename in a pasted snippet must not run the codify skill.
tags: [upkeep, codify]
max_turns: 5
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

Rename getUser to fetchUser in this snippet and show me the result:

```js
function getUser(id) { return db.get(id); }
const u = getUser(1);
```
