Derived from upstream `prototype`, verified at revision `d81f3a1` at `skills/engineering/prototype/SKILL.md`, `LOGIC.md`, and `UI.md`. The [upstream archive guide](../../../.upstream/README.md) explains how source remains available through repository ancestry.

## What it does

`prototype` builds a scoped experiment that answers one design question. The user requests or approves the experiment; it does not become application code merely because the demo works.

- A logic question produces a self-contained HTML demo with free-play actions and guided scenarios.
- A UI question produces structurally different variants with a route-based switcher.

The verdict and its evidence enter the relevant draft, agreed specifications, or working state under the shared document model. Experimental code stays clearly labeled and isolated from production.

## When to reach for it

Type `/prototype`, or the agent reaches for it when a task fits, subject to your approval of the scoped experiment. Use it when discussion cannot settle a concrete state-model or UI question. If the design is already agreed, use [implement](../workflow/implement.md). Living iteration directly evolves implementation without a mandatory prototype.

## Common questions

**Must useful prototype code be thrown away or rebuilt?**

No. Validated useful code can be integrated after authorized acceptance and production checks, including tests, error handling, and appearance or interaction acceptance where judgment is needed. Experimental controls and unselected variants stay outside production.

**Should I prototype the whole application?**

That is not a prototype. The skill asks which single question the experiment should answer and narrows to it, or tells you to run `/iterate` when you want the application itself. A whole application has no natural stopping point and can acquire production obligations before anyone checks readiness.

**How does the next session recover the experiment?**

Keep it as a primary source with a context pointer in the relevant work record. Preserve the question, verdict, evidence, and remaining acceptance rather than only a prose conclusion.

## It's working if

- The question is narrow enough to state in one sentence and appears in the demo.
- A domain expert can drive the logic demo or compare UI variants without reading code.
- The recorded verdict distinguishes experimental validation from production readiness.

## Where it fits

This is a standalone experiment and an optional, user-approved aid during [specify](../workflow/specify.md). [interview](../reference/interview.md) explores the question; [implement](../workflow/implement.md) builds the agreed result. [guide](../productivity/guide.md) maps the whole system.
