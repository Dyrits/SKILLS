Fork-specific skill with no upstream equivalent. It took the code-conventions interview out of `model-domain` (itself forked from upstream `domain-modeling`), where conventions sat beside the glossary although they hold no domain terms ([architecture decision record 0004](../../architecture-decision-record/0004-skills-know-each-other-only-by-contract.md)).

## What it does

`codify` writes down how code is written in your project, as rules a reviewer can apply to any diff. It drafts each candidate from patterns already in the code (how errors are handled, how tests are named), asks you to confirm it and give its reason, and has the confirmed rules written to the conventions file through [document](./document.md). It can also audit an existing conventions file.

A convention is portable: copied into another project on the same stack, with an unrelated domain, it still applies. A rule about what the product does is a requirement, and anything a linter or CI job can check belongs in that tool's configuration; `codify` routes those away instead of writing them down.

## When to reach for it

Type `/codify`, or an agent or another skill can reach for it when a task fits. [review-and-refactor](../workflow/review-and-refactor.md) and [improve-codebase-architecture](../upkeep/improve-codebase-architecture.md) offer it when they find no conventions, and [setup-ai-workspace](../setup/setup-ai-workspace.md) offers it during setup.

| The situation | The move |
| --- | --- |
| Reviews keep arguing about the same style question | `codify` |
| You want an existing conventions file checked | `codify` audits it |
| A word means different things to different people | [delineate](./delineate.md) |
| A design choice needs settling | [interview](./interview.md) |

## Questions in rounds

The questions go through [interview](./interview.md): a round at a time, each with a recommended answer taken from what the code already does. When the code is inconsistent, for example one function throws while its neighbours return results, you see both patterns and pick the rule. A candidate is kept only with your reason in your own words, because a rule without a reason is the first to be misapplied.

A caller passes a focus: **code** (naming, types, error handling, side effects, comments, tests, dependencies) or **architecture** (layering, module layout, seams, coupling, testing per layer).

## Common questions

**My conventions file reads like a specification. How do I fix it?**
Ask `/codify` to check it. The file as a whole must survive being copied into an unrelated project on the same stack. Rules that describe what the product does move to requirements, design trade-offs to a decision record, and verification or approval steps to `AGENTS.md`. A mixed rule splits: "visible text lives in data, in two languages" keeps "no user-facing string literals in rendering code" and moves the language pair to requirements. Nothing moves without your approval.

**I asked for conventions directly. Why would it ask whether to create them?**
It does not. A direct request goes straight to the interview, even if an earlier run recorded `Conventions: declined`. The offer, and the memory of a decline, apply only when another skill raises conventions on its own.

**What if I say no when another skill offers it?**
The decline is recorded in `.agents/domain.md`, so later runs stop asking. Asking for conventions yourself still works.

## It's working if

- Every rule comes with a reason you gave.
- The conventions file could be copied whole into another project on the same stack, and every rule would still apply.
- Product rules end up in requirements and mechanical checks in tool configuration, not in the conventions file.
- Reviews cite a convention instead of re-arguing it.

## Where it fits

`codify` is a reference that [review-and-refactor](../workflow/review-and-refactor.md), [improve-codebase-architecture](../upkeep/improve-codebase-architecture.md), [setup-ai-workspace](../setup/setup-ai-workspace.md), and [iterate](../workflow/iterate.md) call when conventions are missing or need settling. It uses [interview](./interview.md) for the questions and [document](./document.md) for the file. [Guide](../productivity/guide.md) maps the surrounding flows.
