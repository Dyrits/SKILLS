# Summary visual

Adapted from the `illustrate` skill, limited to inline visuals that render in a pull or merge request body.

Pick the **smallest view** that makes the key point clear. Use the primary source and the diff to establish real names, paths, data, and ordering. Keep only the calls, files, props, states, and boundaries the reviewer needs. Label proposed structures and assumptions so they are not mistaken for current behaviour.

## Pick the shape

| What needs explaining | View |
| --- | --- |
| Logic or an algorithm | Pseudocode showing the relevant conditions and actions |
| Runtime control flow | Call tree, with nesting for calls and ordering for execution |
| User interface structure | Component tree annotated with the state and module boundaries that matter |
| File responsibility or a broad refactor | Shallow file tree with a short responsibility beside each relevant entry |
| Component interaction or data flow | Mermaid sequence or flow diagram |
| What changes in an existing shape | `diff` sketch of the component tree, file tree, call tree, or pseudocode |

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

Start with one view; add another only when it answers a distinct part of the change. Use a fenced text sketch instead of Mermaid when the code host cannot render Mermaid.

Done when the visual shows what the change does, and its labels and relationships match the diff or are marked as proposed.
