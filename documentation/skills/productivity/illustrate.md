Source: HumanLayer's [`show-me` skill](https://github.com/humanlayer/skills/tree/main/plugins/show-me/skills/show-me), adopted in commit `c9ed16e`, not from the `d81f3a1` upstream skill set, now named `illustrate` in this fork.

## What it does

`illustrate` explains the current topic with a diagram, code sketch, or focused HTML artifact.
It picks the **smallest view** that answers the question, keeping only the relationships and boundaries you need to see.
The fork renamed it to make its visual-explanation purpose clearer; its behaviour remains unchanged.

## When to reach for it

Type `/illustrate`, or an agent can reach for it when a task needs a visual explanation.
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

**How is it different from `re-explain` or `prototype`?**

- [re-explain](./re-explain.md) rephrases an explanation with the context you were missing.
- `illustrate` draws the point being discussed.
- [prototype](../shaping/prototype.md) builds an approved scoped experiment to settle a design question.

## It's working if

- You can see the answer in the visual without reading a long explanation.
- The names match the conversation or code, and proposed changes are labelled.
- A comparison makes the relevant difference visible.
- Any HTML artifact has a file link, and you know whether the agent previewed it.

## Where it fits

`illustrate` is a reach-for-it-anytime standalone for understanding a topic visually.
[draft-merge-request](../version-control/draft-merge-request.md) also uses it to shape the summary visual in a request body.
[guide](./guide.md) helps you choose where to go next.
