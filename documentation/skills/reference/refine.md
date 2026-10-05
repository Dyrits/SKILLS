Upstream skills: `grilling` and the former `grill-me` wrapper.

## What it does

`refine` interviews you about unresolved choices in a plan, decision, or idea. It asks a round of independent questions, recommends answers, and waits for your decisions before asking dependent questions.

It is a general interview discipline, not a software-document generator. The caller decides where to record agreements.

## When to reach for it

Type `/refine`, or an agent or another skill can reach for it when a task fits. Use it to stress-test a bounded question. Use [specify](../workflow/specify.md) when you want agreed software behavior recorded in a repository specification.

## Rounds and the frontier

The frontier contains choices whose prerequisites are settled. Questions that depend on another unanswered question wait until the next round. The agent researches discoverable facts itself; you decide the tradeoffs.

Settled decisions stay settled unless new evidence reopens them. The interview ends when the selected scope has no unresolved decisions and you confirm the shared understanding. That confirmation does not itself authorize implementation.

## Common questions

**Where did grilling and grill-me go?**
Both now lead to refine. The separate wrapper is gone; refine works with or without a software repository.

**It answered its own questions and started building. Is that intended?**
No. The agent may investigate facts, but unresolved decisions belong to you. Confirming understanding and approving implementation are separate acts.

**Must I decide the whole future product?**
No. Bound the session to the selected question. A long interview may mean that scope needs splitting.

## It's working if

- You can answer a numbered round without guessing at decisions that have not been made.
- The agent asks you about tradeoffs rather than facts it can look up.
- You see the remaining blockers and choose when understanding is complete.

## Where it fits

Refine is a reach-for-it-anytime standalone and an interview discipline. [Specify](../workflow/specify.md) calls it for unresolved software decisions; [graphify](../shaping/graphify.md) uses it to resolve bounded questions in a larger effort. [Guide](../productivity/guide.md) maps the available flows.
