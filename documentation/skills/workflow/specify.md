Upstream skills: `grill-with-docs` and `to-spec`, earlier named `to-prd`, combined here as `specify`.

## What it does

`specify` turns a selected software scope into a living repository specification of agreed behavior, design, and acceptance. It inspects what is already known and interviews you only about decisions that remain unresolved.

The specification stays canonical in the repository. A remote issue can link to or summarize it, but does not become another specification.

## When to reach for it

Type `/specify`, or an agent or another skill can reach for it when the task fits. Use it when the work needs explicit agreed behavior before delivery. If a small change is already clear, [iterate](../workflow/iterate.md) can work directly from active project state without generating a specification.

## The selected scope

Specify accounts for applicable global and capability requirements and completes the selected scope. It does not demand every future product decision. Unresolved proposals stay separate from agreed behavior, and consequential conflicts come back to you.

When a question needs a prototype, you approve that separate exploration. Useful validated prototype code can later be integrated after production validation; there is no mandatory discard-and-rebuild step.

## Common questions

**Do I need separate interviewing and synthesis commands?**
No. Specify combines the former grill-with-documentation and to-specifications steps. It synthesizes directly when decisions are settled.

**Do I need a tracker before writing a specification?**
No. The repository is the specification's source of truth. Publishing or changing a remote record requires explicit approval.

**Does specify always produce tasks?**
No. Choose [taskify](taskify.md) only when decomposition is useful. Small delivery batches can proceed without tasks.

**What if a skill it calls is not installed?**
It names the missing skill with its install command, carries out that step from its stated intent, and tells you the step ran without it. Without `document` it waits instead, because its rules use that skill's terms: install it, or tell it to proceed anyway. The skills involved are listed at the top of its [`SKILL.md`](../../../skills/workflow/specify/SKILL.md).

## It's working if

- The agreed behavior and acceptance cover the selected scope and link applicable constraints.
- Settled decisions are reused, and missing decisions are visible rather than assumed.
- You can distinguish unresolved proposals from authorized agreements.
- The canonical specification is readable in the repository even without tracker access.

## Where it fits

Specify is an optional chain step before [taskify](taskify.md) or [implement](implement.md). It uses [refine](../reference/refine.md) for unresolved choices and [document](../reference/document.md) for shared project records. [Guide](../productivity/guide.md) maps these paths.
