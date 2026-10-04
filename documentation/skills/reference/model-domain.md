Upstream source: `domain-modeling`, verified in the `d81f3a1` tree, renamed `model-domain` in this fork so the name reads as a command.

## What it does

`model-domain` builds and sharpens a project's **ubiquitous language** while you are designing: challenging a term that conflicts with the glossary, forcing a precise word where you used a vague one, and stress-testing a relationship with a concrete scenario until the boundaries are exact.

It is the **active** discipline, not the passive one. Reading `GLOSSARY.md` to borrow its vocabulary is a one-line habit any skill can do; this skill is for when you are *changing* the model. That is what makes it interrupt. It writes a resolved term into `GLOSSARY.md` at the moment it is resolved, in the middle of the conversation, rather than producing a tidy glossary at the end, because the batched version is a summary of a session, and the inline version is the session's actual output.

## When to reach for it

Type `/model-domain`, or an agent or another skill can reach for it when a task fits. Earlier reports found callers loading the interview discipline but skipping this reference. If resolved domain terms never reach the glossary, invoke it explicitly. An unchanged glossary alone is not proof of failure: a session may settle no new term.

Reach for it when the *words* are the problem:

| The situation | The move |
| --- | --- |
| Two people mean different things by "cancellation" | `model-domain`: pick the canonical term, list the other under `_Avoid_` |
| "Account" is doing three jobs in three files | `model-domain`: split it into Customer and User |
| You just made a hard-to-reverse architectural choice | `model-domain` offers an architecture decision record when the choice clears the bar |
| The module's *shape* is the problem: where the seam goes, how deep the interface is | [design-modules](./design-modules.md) |
| You want the whole plan interrogated before you build | [specify](../workflow/specify.md), which resolves outstanding decisions and records agreed capability behavior |
| You want a term looked up, not changed | Nothing. Read `GLOSSARY.md`. It is a file. |

## Prerequisites

None up front. The skill writes into three places and creates each lazily:

- **`GLOSSARY.md`** at the repository root, created by the first resolved term. In a repository with a `GLOSSARY-MAP.md` at the root, terms go into the per-context `GLOSSARY.md` the map points at instead.
- **`documentation/architecture-decision-record/`**, created by the first architecture decision record that clears the bar.
- **`GUIDELINES.md`** at the repository root, created when [review-and-refactor](../workflow/review-and-refactor.md), [improve-codebase-architecture](../upkeep/improve-codebase-architecture.md), or [setup-ai-workspace](../getting-started/setup-ai-workspace.md) offers to and you accept. The skill interviews you about code conventions one topic at a time (naming, types, error handling, side effects, comments, tests, dependencies), drafting candidates from how the code is already written, and keeps each only once you confirm it and give its reason. It writes only portable rules, ones that would still hold if the product changed; product behaviour, design decisions, and agent workflow are routed to requirements, an architecture decision record, or `AGENTS.md` instead. Declining is recorded in `documentation/agents/domain.md`.

Nothing needs to exist before you start, and nothing is created speculatively.

`GUIDELINES.md` is the odd one out: it is a different artifact from the glossary, holding rules rather than terms, and it shares the skill only because the interview belongs in one place.

## Two artifacts, two bars

The glossary and architecture decision record are held to different standards. The first defines terms; the second records a consequential choice.

| | `GLOSSARY.md` | `documentation/architecture-decision-record/NNNN-slug.md` |
| --- | --- | --- |
| Holds | Terms. What a thing **is**, in one or two sentences, with rejected synonyms under `_Avoid_` | One decision, in one to three sentences: context, choice, reason |
| Bar to write | A vague term became canonical | **All three**: hard to reverse, surprising without context, the result of a real trade-off |
| Written | Inline, the moment the term is settled | Offered, not assumed |
| Never holds | Implementation details, a specification, a scratch pad, general programming concepts | A diary of every choice made this session |

Miss any of those three tests and no architecture decision record is needed. An easily reversed decision, an unsurprising choice, or a choice with no real alternative does not earn a separate record.

The `GLOSSARY.md` rule is the one to actually hold onto, because it is the one that breaks in the field. **It is a glossary and nothing else.** Left unchecked, models treat "write to `GLOSSARY.md`" as permission to persist every answer you give, and the file turns into a running specification. This is the most-reported problem with the skill, across several models.

## Cross-referencing, and where it stops

The move that makes the skill click: when you state how something works, it checks the code and surfaces the contradiction. *"Your code cancels entire Orders, but you just said partial cancellation is possible, which is right?"* The language and the code are made to agree, out loud, before either is changed.

The limit is worth knowing. It cross-references **code** and the committed `GLOSSARY.md`/ADRs, and nothing else. It does not search your issue tracker, so a naming collision that was argued out and deliberately settled in a closed issue months ago gets surfaced as if it were new. There is [an open request](https://github.com/mattpocock/skills/issues/717) to fix this; until then, the workaround is to put the instruction in your own `documentation/agents/domain.md`, which the skills already read.

## Common questions

**My `GLOSSARY.md` is 500 lines. 1,000. 3,000. What do I do?**
Check whether it has absorbed implementation detail and decisions that are not glossary material. Ask `/model-domain` to separate those meanings: terms stay in the glossary, agreed behavior belongs in specifications, constraints in requirements, and unresolved proposals in drafts. Preserve obligations rather than deleting them to reduce length. Only split through `GLOSSARY-MAP.md` once the lean glossary genuinely covers distinct contexts; splitting a bloated file just gives you several bloated files.

**What happened to `CONTEXT.md` and `CONTEXT-MAP.md`?**

Upstream renamed the convention to `GLOSSARY.md` and `GLOSSARY-MAP.md`, and this fork adopted that change.
The names now state what the files hold: domain terms, with a map when the project has several contexts.
For an existing project, move its glossary and map to the new names and update references in its steering files and domain configuration.
Historical documents and pinned URLs keep the names used at the time.

**Where did `/ubiquitous-language` go?**
It was removed, and it was not deprecated. Its job moved into `model-domain`, which maintains the whole model continuously rather than dumping a glossary out of one conversation. Vocabulary enforcement got more load-bearing, not less: it now runs underneath grilling, triage and mapping rather than as a separate pass you remember to do.

**How do I get a glossary for a codebase that has none?**
Ask `/model-domain` explicitly to scaffold the glossary rather than waiting for terms to accumulate incidentally. An earlier report described 50+ questions for an existing repository. Bound the scope to one context and supply known terms first; settled meanings do not need another interview.

**Can I keep the domain model and use my own architecture decision record format?**
The glossary and decision-record instructions ship together, so an established team format may conflict with the default. State the repository's authoritative convention explicitly in its steering documents, and surface any conflict instead of silently replacing old records. Separating the two disciplines was requested in [issue #557](https://github.com/mattpocock/skills/issues/557).

**Does a glossary actually earn its keep? It is one more artifact to review, and it can go stale.**
Sometimes it does not, and it is worth being honest about where. DDD gets less useful the closer it gets to the implementation: the payoff is upstream, in naming and concept alignment, not in aggregates and layer ceremony. Synonym control matters at naming boundaries: module names, table names, status enums, issue titles, CLI commands. It matters much less in ordinary prose. There is also a live objection that domain terms compress communication *between humans* who already share them, and that an agent responds the same way to the plain-English description. On that reading, the glossary's value is keeping you and your reviewers aligned with what the agent is doing, not making the agent better. On a one-day build, skip it. And an unreviewed, agent-authored glossary is worse than none: it becomes confident-sounding lore that later sessions treat as truth.

**Can it turn my vague prompts into domain language for me?**
No, and there is no plan for a skill that does. A domain language you do not understand yourself becomes meaningless drivel once written down. This skill enforces precision once you have the understanding; it does not manufacture vocabulary you do not have. The related trap is using domain words without doing the modelling: right nouns over the wrong conceptual structure produce output that reads correct and is not.

**My `GUIDELINES.md` reads like a specification. How do I fix it?**
Ask the skill to check it. Each rule is tested for portability: would it still hold if the product changed and only the stack and team stayed? Rules that describe what the product does move to requirements, design trade-offs to an architecture decision record, and verification or approval steps to `AGENTS.md`. A mixed rule splits, for example "visible text lives in data, in two languages" keeps "no user-facing string literals in rendering code" and moves the language pair to requirements. Nothing moves without your approval.

## It's working if

- It stops you mid-sentence to ask which of two things you meant, instead of picking one and moving on.
- `GLOSSARY.md` changes **during** the conversation, not in a burst at the end.
- It declines a decision record for something you could undo tomorrow and says which test failed.
- New entries define what a thing *is* in one or two sentences and name the words you are giving up under `_Avoid_`.
- It quotes your code back at you when your code and your sentence disagree.
- `GLOSSARY.md` gets shorter as often as it gets longer.
- Every `GUIDELINES.md` rule could be pasted into another project on the same stack and still make sense.

## Where it fits

`model-domain` is a reference used by [specify](../workflow/specify.md), [graphify](../shaping/graphify.md), and [triage](../upkeep/triage.md) when domain meaning needs sharpening. [design-modules](./design-modules.md) supplies vocabulary for module shape rather than the problem domain. [document](./document.md) keeps the resulting terms, decisions, constraints, and agreed behavior in their separate records. [guide](../getting-started/guide.md) routes you when the next move is unclear.
