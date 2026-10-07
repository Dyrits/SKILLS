Upstream source: `domain-modeling`, verified in the `d81f3a1` tree. This fork named it `model-domain`, narrowed it to settling terms as `delineate`, then widened it into the system's functional outline ([architecture decision record 0006](../../architecture-decision-record/0006-describe-systems-and-capabilities-functionally-and-technically.md)). Decision records moved to [architect](./architect.md) and [engineer](./engineer.md), and code conventions to [codify](../setup/codify.md).

## What it does

`delineate` describes the system from the functional side: what it is for, who uses it, the domain contexts it divides into, the capabilities it offers, the requirements imposed on it from outside the code, and the words everyone uses for all of that. It names no technology or structure; that is [architect](./architect.md)'s side of the same level.

It still interrupts when a word is the problem. Challenging a term that conflicts with the glossary, forcing a precise word where a vague one was used, and testing a meaning against a concrete scenario are one branch of the skill, and the settled term is written into the glossary the moment it is settled, not in a batch at the end.

## When to reach for it

Type `/delineate`, or an agent can reach for it when a task fits. Reach for it when:

| The situation | The move |
| --- | --- |
| You are starting a system, or nobody has written down what it is for | `delineate`, outline branch |
| The system's requirements (uptime, compliance, budget, data location) live only in people's heads | `delineate`, outline branch |
| Two people mean different things by "cancellation" | `delineate`, term branch: pick the canonical term, list the other under `_Avoid_` |
| "Account" is doing three jobs in three files | `delineate`, term branch: split it into Customer and User |
| You need the stack or the system's structure decided | [architect](./architect.md) |
| One capability's behavior needs agreeing | [specify](./specify.md) |
| You want a term looked up, not changed | Nothing. Read the glossary. |

## What it writes

| Document | Holds |
| --- | --- |
| `documentation/outline.md` | Purpose, actors, contexts and their relationships, the capability map |
| `documentation/requirements.md` | System-wide obligations, each with its source, and its number and check when measurable |
| The glossary | Domain terms only. One context keeps `documentation/glossary.md`; several keep one glossary beside each context's code, linked from the domain outline |

Every requirement goes here, functional or not: an uptime target is imposed from outside the code just as a business rule is. [architect](./architect.md) then says how the system meets it. The capability map lists what the system does or is agreed to do; priorities and candidates stay in the backlog.

## Cross-referencing, and where it stops

When you state how something works, it checks the code and surfaces the contradiction: *"Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?"* The language and the code are made to agree, out loud, before either changes.

It cross-references the code and the committed documents, and nothing else. It does not search your issue tracker, so a naming collision settled in a closed issue months ago can come back as if it were new. Until that changes, put the instruction in your own `AGENTS.md`.

## Common questions

**Why does a skill about words now write requirements and a capability map?**
Because they are the same level of description. Deciding where one context ends and another begins is deciding where a word changes meaning, and the capability map is written in those words. The functional picture of the system needed one owner, and the glossary was already its densest part.

**Do I have to run it before `/architect` or `/specify`?**
No. Each skill reads what exists and asks for the minimum it lacks. Running `delineate` first means the later skills ask fewer questions and use the same words.

**My glossary is 500 lines. 1,000. 3,000. What do I do?**
Check whether it has absorbed implementation detail and decisions. Ask `/delineate` to clean it up: terms stay, agreed behavior goes to the capability's specifications, obligations to the requirements, and nothing moves without your approval. Split it into contexts only once the lean glossary genuinely covers distinct ones; splitting a bloated file gives you several bloated files.

**What happened to `CONTEXT.md`, `CONTEXT-MAP.md`, and the glossary map?**
Upstream renamed the convention to `GLOSSARY.md` and `GLOSSARY-MAP.md`. This fork moved the glossary under `documentation/`, and the domain outline now lists the contexts and links their glossaries, so a separate map is no longer needed. Historical documents keep the names used at the time.

**Where did architecture decision records go?**
To the technical side: [architect](./architect.md) records system-level decisions and [engineer](./engineer.md) capability-level ones. A choice between two words is settled here; the `_Why_` line in a glossary entry records why a term won when that is easy to reverse.

**Does a glossary actually earn its keep?**
Sometimes not. The payoff is in naming and concept alignment at boundaries (module names, table names, status enums, issue titles), not in ordinary prose. On a one-day build, skip it. An unreviewed, agent-written glossary is worse than none: it becomes confident lore later sessions treat as truth.

**Can it turn my vague prompts into domain language for me?**
No. A domain language you do not understand yourself becomes meaningless once written down. It enforces precision once you have the understanding; it does not manufacture vocabulary you do not have.

## It's working if

- The domain outline names no technology, and every requirement names who imposes it.
- A newcomer can read `documentation/outline.md` and say what the system is for and which capabilities it has.
- It stops you mid-sentence to ask which of two things you meant, instead of picking one and moving on.
- The glossary changes during the conversation, and gets shorter as often as it gets longer.
- It quotes your code back at you when your code and your sentence disagree.
- `AGENTS.md` and the root `README.md` each gain one line for every kind of document it creates for the first time, and no duplicate when one exists.

## Where it fits

`delineate` is the functional half of the system level, usually run before [architect](./architect.md) and revisited when the business changes. [specify](./specify.md) and [engineer](./engineer.md) work one capability at a time on the same model. [guide](../productivity/guide.md) maps the whole flow.
