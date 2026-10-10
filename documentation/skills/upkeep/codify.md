Fork-specific skill with no upstream equivalent. It took the code-conventions interview out of `model-domain` (itself forked from upstream `domain-modeling`), where conventions sat beside the glossary although they hold no domain terms ([architecture decision record 0004](../../architecture-decision-record/0004-skills-know-each-other-only-by-contract.md)).

## What it does

`codify` writes down how code is written in your project, as rules a reviewer can apply to any diff. It drafts each candidate from patterns already in the code (how errors are handled, how tests are named), asks you to confirm it and give its reason, and writes the confirmed rules to the conventions file, routing anything that is not a convention to its proper home. It can also audit an existing conventions file.

A convention is project-agnostic: it applies to this project but could be transposed to another one on the same stack, because it is not tied to the product or its domain. A rule about what the product does is a requirement, and anything a linter or CI job can check belongs in that tool's configuration; `codify` routes those away instead of writing them down.

## When to reach for it

Type `/codify`, or an agent can reach for it when a task fits. Reviews and architecture audits, such as [review-and-refactor](../workflow/review-and-refactor.md) and [improve-codebase-architecture](../upkeep/improve-codebase-architecture.md), report a missing conventions file instead of writing one; that report is the cue to run it.

| The situation | The move |
| --- | --- |
| Reviews keep arguing about the same style question | `codify` |
| You want an existing conventions file checked | `codify` audits it |
| A word means different things to different people | [delineate](../workflow/delineate.md) |
| A design choice needs settling | [interview](../shaping/interview.md) |

## Questions in rounds

The questions follow the [interview](../shaping/interview.md) method: a round at a time, each with a recommended answer taken from what the code already does. When the code is inconsistent, for example one function throws while its neighbours return results, you see both patterns and pick the rule. A candidate is kept only with your reason in your own words, because a rule without a reason is the first to be misapplied.

A run picks a focus: **code** (naming, types, error handling, side effects, comments, tests, dependencies) or **architecture** (layering, module layout, seams, coupling, testing per layer).

## Common questions

**My conventions file reads like a specification. How do I fix it?**
Ask `/codify` to check it. The file as a whole must survive being copied into an unrelated project on the same stack. Rules that describe what the product does move to requirements, design trade-offs to a decision record, and verification or approval steps to `AGENTS.md`. A mixed rule splits: "visible text lives in data, in two languages" keeps "no user-facing string literals in rendering code" and moves the language pair to requirements. Nothing moves without your approval.

**I asked for conventions directly. Why would it ask whether to create them?**
It does not. A direct request goes straight to the interview. The offer applies only when an agent reaches for it on its own during other work, such as a review that found no conventions.

**What if I say no when it is offered?**
Nothing is recorded, so the next time conventions come up it asks again. A review then runs without project conventions, on its built-in checks. Run as a subagent with no one to answer, it skips the question and reports that conventions are missing.

## It's working if

- Every rule comes with a reason you gave.
- The conventions file could be copied whole into another project on the same stack, and every rule would still apply.
- Product rules end up in requirements and mechanical checks in tool configuration, not in the conventions file.
- Reviews cite a convention instead of re-arguing it.

## Where it fits

`codify` is maintenance: run it once a repository has code, best after [architect](../workflow/architect.md) has chosen the stack, and again when conventions need checking. [setup](../getting-started/setup.md) reads the conventions it writes and carries their tool rules into the formatter and linter configuration. Reviews and audits read the conventions file it writes and report when it is missing. It carries its own copies of the [interview](../shaping/interview.md) method and of the formats for the conventions file and the other homes it routes rules to.
