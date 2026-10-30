---
description: Pasted review notes should be split into referenced points with dispositions and a plan awaiting approval, before any edit.
tags: [workflow, address-feedback]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
---

My teammate left these notes on my retry helper. Can you work through them? I have not changed anything yet.

```python
def retry(fn, attempts=3):
    for i in range(attempts):
        try:
            return fn()
        except Exception:
            time.sleep(2 ** i)
    raise RuntimeError("failed")
```

Notes from Sam:
- Catching bare Exception hides programming errors, only retry on the network errors we expect.
- Please add jitter to the sleep so clients do not retry in lockstep.
- Also, please remove the sleep entirely, tests take too long.
- Overall this looks good, thanks for picking it up.
