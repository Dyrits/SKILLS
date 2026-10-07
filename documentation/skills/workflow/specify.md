Upstream skills: `grill-with-docs` and `to-spec`, earlier named `to-prd`, combined here as `specify`.

## What it does

`specify` turns a selected capability into a living repository specification of its observable behavior, edge cases, and acceptance. It inspects what is already known and interviews you only about decisions that remain unresolved.

It stays on the side users and other systems can see, including external contracts such as a public API. How the code delivers it (modules, internal interfaces, the data model) belongs to [engineer](./engineer.md), the technical half of the capability level ([architecture decision record 0006](../../architecture-decision-record/0006-describe-systems-and-capabilities-functionally-and-technically.md)).

The specification stays canonical in the repository. A remote issue can link to or summarize it, but does not become another specification.

## When to reach for it

Type `/specify`, or an agent can reach for it when the task fits. Use it when the work needs explicit agreed behavior before delivery. If a small change is already clear, [iterate](../workflow/iterate.md) can work directly from active project state without generating a specification.

## The selected scope

Specify accounts for applicable global and capability requirements and completes the selected scope. It does not demand every future product decision. Unresolved proposals stay separate from agreed behavior, and consequential conflicts come back to you.

A disputed term is settled on the spot and written to the glossary; system-wide outlining is [delineate](./delineate.md)'s job.

When a question needs a prototype, it proposes that separate exploration and keeps the question open until its evidence is in. Useful validated prototype code can later be integrated after production validation; there is no mandatory discard-and-rebuild step.

## Common questions

**Do I need separate interviewing and synthesis commands?**
No. Specify combines the former grill-with-documentation and to-specifications steps. It synthesizes directly when decisions are settled.

**Do I need a tracker before writing a specification?**
No. The repository is the specification's source of truth. Publishing or changing a remote record requires explicit approval.

**Does specify always produce tasks?**
No. Choose [taskify](taskify.md) only when decomposition is useful. Small delivery batches can proceed without tasks.

**Where did the design section go?**
To [engineer](./engineer.md), which writes `blueprint.md` beside the specifications. Agreeing behavior no longer waits on technical choices, and the design can change without reopening the agreement.

**What does it do when it finishes?**
It reports the canonical paths, covered requirements, agreements, blockers, and validation still needed. It does not start or suggest another skill; the documents it leaves are what the next step reads.

## It's working if

- The agreed behavior and acceptance cover the selected scope and link applicable requirements.
- The specification names no module, class, or table; technical ideas raised along the way are noted for the blueprint.
- Settled decisions are reused, and missing decisions are visible rather than assumed.
- You can distinguish unresolved proposals from authorized agreements.
- The canonical specification is readable in the repository even without tracker access.
- `AGENTS.md` and the root `README.md` each gain one line for every kind of document it creates for the first time, and no duplicate when one exists.

## Where it fits

Specify is the functional half of the capability level, usually followed by [engineer](./engineer.md), then [taskify](taskify.md) or [implement](implement.md). It reads the system-level documents [delineate](./delineate.md) and [architect](./architect.md) write when they exist. [Guide](../productivity/guide.md) maps these paths.
