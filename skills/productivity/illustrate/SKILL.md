---
name: illustrate
description: "Explain the current topic visually. Use when the user asks to see how something works, compare states or options, or understand code structure or flow."
metadata:
  forks: "humanlayer/skills/plugins/show-me/skills/show-me"
---

Help the user understand the current topic of conversation visually.
Lead with the visual, keep prose brief, and pick the **smallest view** that makes the key point clear.

Use the conversation and relevant source to establish real names, paths, data, and ordering.
Label proposed structures and assumptions so the user can distinguish them from current behaviour.
Keep only the calls, files, props, states, and boundaries needed to answer the current question.

## Pick the shape

| What needs explaining | View |
| --- | --- |
| Logic or an algorithm | Pseudocode showing the relevant conditions and actions |
| Runtime control flow | Call tree, with nesting for calls and ordering for execution |
| User interface structure | Component tree annotated with the state and module boundaries that matter |
| File responsibility or a broad refactor | Shallow file tree with a short responsibility beside each relevant entry |
| Component interaction or data flow | Mermaid sequence or flow diagram |
| What changes in an existing shape | `diff` sketch of the component tree, file tree, call tree, or pseudocode |
| Mostly new code, context needed to show ownership or order, or a copyable target | Whole block in the appropriate code language |
| Visual layout, state comparison, or a concept too dense for an inline diagram | One focused HTML artifact; read [HTML.md](references/HTML.md) for this branch |

Use `text` fences for structural sketches whose annotations are not executable code:

```text
<SessionPage>                 apps/example/src/routes/session.tsx
  useSessionEvents()
  <SessionToolbar>
    <RunSkillButton>          packages/ui
```

A diff can show changes to any of these shapes:

```diff
 on(save)
-  write content
+  if content is unchanged
+    return cached result
+  write content
+  invalidate cache
```

## Deliver

Place each visual next to the short text it supports, in the user's language and with the topic's established terms.
Start with one view; add another only when it answers a distinct part of the question.
Respect the destination: use fenced text when Mermaid cannot render, and keep inline-only requests in the requested format.

Done when the visual answers the current question, its labels and relationships match the source or are marked as proposed, and the user can view it directly or open the linked artifact.
