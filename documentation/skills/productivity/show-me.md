## What it does

`show-me` explains the current topic with a diagram, code sketch, or focused HTML artifact.
It picks the **smallest view** that answers the question, keeping only the relationships and boundaries you need to see.

## When to reach for it

Type `/show-me`, or the agent reaches for it automatically when a task needs a visual explanation.
Use it during a discussion when you need to see the structure, sequence, or difference between options.

| Your question | What you might see |
| --- | --- |
| What calls what, and in what order? | A call tree or Mermaid sequence diagram |
| Which component or file owns this? | An annotated component or file tree |
| What changes? | A diff sketch of the relevant structure or logic |
| How do these states or layouts compare? | A diagram or an HTML artifact you can open |

## Common questions

**Will it always create an HTML file?**

It starts with an inline visual when that is enough.
HTML is for layouts, state comparisons, or concepts that need more room or interaction.
The agent opens the file when its tools support that and gives you a file link.

**How is it different from `wait-what` or `prototype`?**

- [wait-what](./wait-what.md) rephrases an explanation with the context you were missing.
- `show-me` draws the point being discussed.
- [prototype](../shaping/prototype.md) builds throwaway code to settle a design question through experimentation.

## It's working if

- You can see the answer in the visual without reading a long explanation.
- The names match the conversation or code, and proposed changes are labelled.
- A comparison makes the relevant difference visible.
- Any HTML artifact has a file link, and you know whether the agent previewed it.

## Where it fits

`show-me` is a reach-for-it-anytime standalone for understanding a topic visually.
[to-pull-request](../workflow/to-pull-request.md) also uses it to shape the summary visual in a request body.
[what-is-next](../getting-started/what-is-next.md) helps you choose where to go next.
