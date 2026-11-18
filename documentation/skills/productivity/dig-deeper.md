Source: Tarektouati's [`keep-digging` skill](https://github.com/Tarektouati/skills/tree/main/keep-digging), adopted in this fork, not from the `d81f3a1` upstream skill set. It describes the five-whys learning mode Tibo Sottiaux explained on The Pragmatic Engineer. This fork renamed it `dig-deeper`, because the name echoes what you say after a surface answer and the skill stops at bedrock rather than after a count of five; the old names `keep-digging` and `ask-why` are not aliases. It keeps the technique and adds a source or assumption flag to every layer.

## What it does

`dig-deeper` explains how or why something works by asking why of its own answer, one layer at a time, until the next why would only repeat a definition. The agent shows every layer, grounds each in a file, a document, or a configuration, and ends with one sentence naming the root.

The aim is understanding, not diagnosis. It is the five whys aimed at "how does this work", not at "what broke".

## When to reach for it

Type `/dig-deeper`, or an agent can reach for it when the task fits. Use it when a one-line answer would leave you without real understanding: onboarding to unfamiliar code, a library with depth underneath, or a change an agent just made that you cannot yet explain. Phrases such as "five whys this" or "don't stop at the surface" fit too.

It answers a trivial fact directly, without a chain. For a failing behavior you want fixed, use [debug](../upkeep/debug.md). For understanding built over several sessions, use [teach](./teach.md). For an explanation that did not land, use [re-explain](./re-explain.md).

## Bedrock, not a count

Five layers is a guide. The chain stops at bedrock: a hardware limit, an external contract, a documented tradeoff, or a stated principle. It stops sooner when bedrock arrives sooner and continues when a layer still has a source-backed why. A layer the agent cannot source is marked as an assumption, with what would confirm it, and the chain ends there. A short chain with a flagged gap is more useful than a plausible invented one.

## Common questions

**Is this the incident postmortem five whys?**

No. That technique stops at the one cause of a failure. This one builds understanding of a mechanism, so the useful result is the whole chain.

**Why does every layer cite a source?**

A chain of plausible but unchecked whys reads well and can be wrong at every step. A cited layer lets you verify it; an assumption flag tells you where not to trust it.

**Why not just summarize the root?**

The layers are how you learn. The closing sentence is what to remember, and the chain is how you got there.

## It's working if

- Layer 1 is a fact about your code or system, with a file or document cited, not a textbook explanation.
- Each layer is more fundamental than the one before.
- The chain ends at bedrock or at an assumption flag, not at an arbitrary fifth layer.
- The final sentence names a root you could repeat to a colleague.

## Where it fits

`dig-deeper` is a reach-for-it-anytime standalone inside any conversation. [illustrate](./illustrate.md) shows the same subject visually; [re-explain](./re-explain.md) repairs an explanation after it failed.
