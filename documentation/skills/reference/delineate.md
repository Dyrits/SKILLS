Upstream source: `domain-modeling`, verified in the `d81f3a1` tree. This fork named it `model-domain`, then narrowed it to settling terms and renamed it `delineate`: the glossary and decision record formats moved to [document](./document.md), and code conventions to [codify](./codify.md).

## What it does

`delineate` settles what the project's words mean while you are designing: challenging a term that conflicts with the glossary, forcing a precise word where you used a vague one, and stress-testing a relationship with a concrete scenario until the boundaries are exact.

It is the **active** discipline, not the passive one. Reading the glossary to borrow its vocabulary is a one-line habit any skill can do; this skill is for when you are *changing* what a word means. That is what makes it interrupt. It has a resolved term written into the glossary at the moment it is resolved, through [document](./document.md), in the middle of the conversation, rather than producing a tidy glossary at the end, because the batched version is a summary of a session, and the inline version is the session's actual output.

## When to reach for it

Type `/delineate`, or an agent or another skill can reach for it when a task fits. If resolved domain terms never reach the glossary, invoke it explicitly. An unchanged glossary alone is not proof of failure: a session may settle no new term.

Reach for it when the *words* are the problem:

| The situation | The move |
| --- | --- |
| Two people mean different things by "cancellation" | `delineate`: pick the canonical term, list the other under `_Avoid_` |
| "Account" is doing three jobs in three files | `delineate`: split it into Customer and User |
| You just made a hard-to-reverse architectural choice | [interview](./interview.md) settles it, and [document](./document.md) records it when it clears the bar |
| You want to write down how code is written here | [codify](./codify.md) |
| The module's *shape* is the problem: where the seam goes, how deep the interface is | [design-modules](./design-modules.md) |
| You want the whole plan interrogated before you build | [specify](../workflow/specify.md), which resolves outstanding decisions and records agreed capability behavior |
| You want a term looked up, not changed | Nothing. Read the glossary. It is a file. |

## Prerequisites

None. The skill writes nothing itself: settled terms go through [document](./document.md), which owns where the glossary lives and its format. When several terms are open at once, it settles them in rounds through [interview](./interview.md). Nothing needs to exist before you start, and nothing is created speculatively.

## Cross-referencing, and where it stops

The move that makes the skill click: when you state how something works, it checks the code and surfaces the contradiction. *"Your code cancels entire Orders, but you just said partial cancellation is possible, which is right?"* The language and the code are made to agree, out loud, before either is changed.

The limit is worth knowing. It cross-references **code** and the committed glossary and decision records, and nothing else. It does not search your issue tracker, so a naming collision that was argued out and deliberately settled in a closed issue months ago gets surfaced as if it were new. There is [an open request](https://github.com/mattpocock/skills/issues/717) to fix this; until then, the workaround is to put the instruction in your own `.agents/domain.md`, which the skills already read.

## Common questions

**My glossary is 500 lines. 1,000. 3,000. What do I do?**
Check whether it has absorbed implementation detail and decisions that are not glossary material. Ask `/delineate` to separate those meanings: terms stay in the glossary, agreed behavior belongs in specifications, constraints in requirements, and unresolved proposals in drafts. Preserve obligations rather than deleting them to reduce length. Only split through a glossary map once the lean glossary genuinely covers distinct contexts; splitting a bloated file just gives you several bloated files.

**What happened to `CONTEXT.md` and `CONTEXT-MAP.md`?**

Upstream renamed the convention to `GLOSSARY.md` and `GLOSSARY-MAP.md`. This fork then moved both under `documentation/`, as `glossary.md` and `glossary-map.md`, owned by [document](./document.md) like every other shared project document ([architecture decision record 0004](../../architecture-decision-record/0004-skills-know-each-other-only-by-contract.md)).
Historical documents and pinned URLs keep the names used at the time.

**Where did `/ubiquitous-language` go?**
It was removed, and it was not deprecated. Its job moved into `delineate`, which maintains the glossary continuously rather than dumping one out of a single conversation. Vocabulary enforcement got more load-bearing, not less: it now runs underneath grilling, triage and mapping rather than as a separate pass you remember to do.

**How do I get a glossary for a codebase that has none?**
Ask `/delineate` explicitly to scaffold the glossary rather than waiting for terms to accumulate incidentally. An earlier report described 50+ questions for an existing repository. Bound the scope to one context and supply known terms first; settled meanings do not need another interview.

**Where did architecture decision records go?**
Out of this skill, as [issue #557](https://github.com/mattpocock/skills/issues/557) requested upstream. [interview](./interview.md) settles a decision with you, and [document](./document.md) records it when it clears the bar. A repository with its own record format states it in its steering documents.

**Does a glossary actually earn its keep? It is one more artifact to review, and it can go stale.**
Sometimes it does not, and it is worth being honest about where. DDD gets less useful the closer it gets to the implementation: the payoff is upstream, in naming and concept alignment, not in aggregates and layer ceremony. Synonym control matters at naming boundaries: module names, table names, status enums, issue titles, CLI commands. It matters much less in ordinary prose. There is also a live objection that domain terms compress communication *between humans* who already share them, and that an agent responds the same way to the plain-English description. On that reading, the glossary's value is keeping you and your reviewers aligned with what the agent is doing, not making the agent better. On a one-day build, skip it. And an unreviewed, agent-authored glossary is worse than none: it becomes confident-sounding lore that later sessions treat as truth.

**Can it turn my vague prompts into domain language for me?**
No, and there is no plan for a skill that does. A domain language you do not understand yourself becomes meaningless drivel once written down. This skill enforces precision once you have the understanding; it does not manufacture vocabulary you do not have. The related trap is using domain words without doing the modelling: right nouns over the wrong conceptual structure produce output that reads correct and is not.

## It's working if

- It stops you mid-sentence to ask which of two things you meant, instead of picking one and moving on.
- The glossary changes **during** the conversation, not in a burst at the end.
- New entries define what a thing *is* in one or two sentences and name the words you are giving up under `_Avoid_`.
- It quotes your code back at you when your code and your sentence disagree.
- The glossary gets shorter as often as it gets longer.

## Where it fits

`delineate` is a reference used by [specify](../workflow/specify.md), [iterate](../workflow/iterate.md), [graphify](../shaping/graphify.md), [triage](../upkeep/triage.md), and [improve-codebase-architecture](../upkeep/improve-codebase-architecture.md) when a term is fuzzy or disputed. [design-modules](./design-modules.md) supplies vocabulary for module shape rather than the problem domain. It calls [document](./document.md) to write the terms it settles. [guide](../productivity/guide.md) routes you when the next move is unclear.
