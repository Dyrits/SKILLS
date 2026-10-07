Upstream skills: `grilling` and the former `grill-me` wrapper, first named `refine` in this fork.

## What it does

`interview` interviews you about unresolved choices in a plan, decision, or idea. It asks a round of independent questions, recommends answers, and waits for your decisions before asking dependent questions.

It is a general interview discipline, not a software-document generator. The caller decides where to record agreements.

## When to reach for it

Type `/interview`, or an agent can reach for it when a task fits. Use it to stress-test a bounded question. Use [specify](../workflow/specify.md) when you want agreed software behavior recorded in a repository specification.

## Rounds and the frontier

The frontier contains choices whose prerequisites are settled. Questions that depend on another unanswered question wait until the next round. The agent researches discoverable facts itself; you decide the tradeoffs.

Settled decisions stay settled unless new evidence reopens them. The interview ends when the selected scope has no unresolved decisions and you confirm the shared understanding. That confirmation does not itself authorize implementation.

## Common questions

**Where did grilling, grill-me, and refine go?**
All three now lead to `interview`. The separate wrapper is gone, and `refine` was renamed after the mechanism it uses. It works with or without a software repository.

**It answered its own questions and started building. Is that intended?**
No. The agent may investigate facts, but unresolved decisions belong to you. Confirming understanding and approving implementation are separate acts.

**Must I decide the whole future product?**
No. Bound the session to the selected question. A long interview may mean that scope needs splitting.

## It's working if

- You can answer a numbered round without guessing at decisions that have not been made.
- The agent asks you about tradeoffs rather than facts it can look up.
- You see the remaining blockers and choose when understanding is complete.

## Where it fits

Interview is a reach-for-it-anytime standalone and an interview discipline. [Specify](../workflow/specify.md), [delineate](../workflow/delineate.md), [architect](../workflow/architect.md), and [engineer](../workflow/engineer.md) carry their own copy of its method for unresolved decisions; [graphify](../shaping/graphify.md) uses it to resolve bounded questions in a larger effort; [codify](../setup/codify.md) uses it to settle code conventions. [Guide](../productivity/guide.md) maps the available flows.
