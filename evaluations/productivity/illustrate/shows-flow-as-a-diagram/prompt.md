---
description: A request to see how code flows should lead with a diagram or call tree, with brief prose.
tags: [productivity, illustrate]
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Show me how a request moves through this Express setup, I can't follow the order:

```js
app.use(cors());
app.use(express.json());
app.use('/api', authMiddleware);
app.get('/api/orders', rateLimit, listOrders);
app.use(errorHandler);
```
