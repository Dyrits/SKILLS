## What it does

`to-specifications` turns the conversation you have just had into a **specification**. It keeps the result in the configured local refinement workspace as a draft, or publishes it to the system-of-record tracker when you explicitly request publication.

It does not interview you. By the time you reach for it the deciding is already done, so it synthesises what is known (from the thread, from the codebase, from your `CONTEXT.md` and ADRs) rather than opening a fresh round of questions. The specification is a record of decisions already made, not a place where new ones get made.

## When to reach for it

You invoke this by typing `/to-specifications`; the agent won't reach for it on its own.

Reach for it when the build is too big for one agent session and has to survive being split across several. That is the whole trigger:

| Where you are | What to run |
| --- | --- |
| You haven't decided anything yet | [grill-with-documentation](./grill-with-documentation.md) first |
| Decided, and the work fits one context window | [implement](./implement.md): skip the specification |
| Decided, and the work spans several sessions | `/to-specifications`, then [to-tickets](./to-tickets.md) |
| A [wayfinder](../shaping/wayfinder.md) map has cleared | `/to-specifications #<map_issue>` |

## Prerequisites

`to-specifications` needs [setup-custom-skills](../getting-started/setup-custom-skills.md) to configure the tracker, publication boundary, and triage-label vocabulary. With local refinement enabled, a sourced draft lives at `.scratch/<issue-key>/specification.md`; the remote issue remains unchanged until you explicitly ask to publish.

## The specification is a decision record

The specification exists because context windows end. Everything you settled while grilling (the shape of the solution, the choices you argued through, what you deliberately refused) is in one conversation that is about to be cleared. The specification is what survives that.

So it does not validate anything, and it does not decide anything. It captures what was decided, in your project's own vocabulary, so that a fresh session can pick the work up without you re-explaining it. Anything the specification asserts that you never actually said is a defect.

## Seams before prose

Before it writes a word, `to-specifications` sketches the **seams** the feature will be tested at, and checks them with you. It prefers seams that already exist to new ones, and takes the highest seam it can: the ideal number across a change is one.

Those agreed seams then travel. [test-driven-development](./test-driven-development.md) works only at pre-agreed seams, and [code-review](./code-review.md) reviews the diff against the specification, so a seam nobody agreed to shows up as a review finding. The binding is indirect: it runs through this document, which is exactly why the seam conversation is worth taking seriously here rather than deferring it to implementation.

## Common questions

**Where did `/to-prd` and `/to-spec` go?**
They are earlier names for this skill. `to-prd` became `to-spec`, then `to-spec` became `to-specifications` so the public name no longer abbreviates its output. The earlier slugs have no aliases; reinstall under the current name. The pair is now *specification* and *tickets*: the specification is the destination and the decisions that fix it, while the tickets are the execution steps that get there. If you pivot, delete the unfinished tickets and keep the specification.

**Why does the specification get the `ready-for-agent` label? I don't want an agent implementing off it.**
The label means "no further triage needed": the document is complete enough for an agent to work from. It is an input designation, not a work order. But if you run AFK agents that poll for `ready-for-agent`, that distinction isn't visible to them, and they will happily try to build the whole specification in one run instead of picking up the ticket slices. This is the most-reported rough edge on the skill. Until it changes, exclude the parent specification explicitly in your AFK agent's prompt, or strip the label once `/to-tickets` has run.

**Why not go straight from grilling to `/to-tickets` and skip the specification?**
Often you should; the specification earns its step only on multi-session work. Where it pays is that the tickets are disposable and the specification isn't: each ticket is sized for one fresh context window and gets deleted or closed, while the specification stays as the one place the reasoning behind them lives. On a single-session change that buys you nothing, and you have paid an extra synthesis step where the model can drift. Go grilling → `/implement`.

**I just finished a wayfinder map. What do I feed it?**
The main map issue: `/to-specifications #<map_issue>`, not the individual decision tickets. [wayfinder](../shaping/wayfinder.md) produces decisions rather than deliverables, scattered across a map; `to-specifications` is the step that collapses them into one buildable document. Looping the map straight into `/implement` throws that collapse away.

**Is the specification for me to review, or is it just for the agent?**
Mostly for the agent, and it reads that way: complete, dense, reference-heavy. The parts worth your eyes are the seams and the out-of-scope section, because those are the two places a wrong decision is cheapest to catch and most expensive to discover later. Reading the whole thing end to end is a real complaint people have, and there is no summary mode: the honest answer is that if the specification surprises you, the grilling was too shallow, not the specification too long.

**Do I keep the specification frozen once tickets start, or let the agent rewrite it?**
Nothing keeps it in sync, so in practice it is a snapshot of what you knew at that moment, and it goes stale the first time implementation teaches you something. Treat it as throwaway once the work ships. The artifacts meant to outlive it are your `CONTEXT.md` and your ADRs; if something learned during implementation deserves to last, it belongs there, not in an edited specification.

**My work is a refactor or a module boundary, not a feature. Does the template fit?**
Less well, and this is a known limitation. The template leans hard on user stories, which is the wrong shape for architectural work: you end up writing stories nobody asked for around decisions that are really about interfaces and invariants. Lean on the implementation-decisions and testing-decisions sections instead, and let the durable architectural calls land as ADRs via [grill-with-documentation](./grill-with-documentation.md) rather than trying to make the specification carry them.

**Will it check the tracker for related work, or cite the ADRs it's respecting?**
No to both. It reads and respects the ADRs covering the area it touches, but it doesn't link them, and it doesn't search the tracker for overlapping issues before drafting, so a specification can quietly duplicate work someone already filed. Search the tracker yourself first if the area is busy.

**`/to-tickets` couldn't read my specification: it kept truncating.**
Very large specifications can outgrow what a tracker issue will serve back cleanly, and there is no local copy to fall back on. The fix is context hygiene: don't clear or compact between `/to-specifications` and `/to-tickets`. Run them in the same window and the specification never has to be re-fetched at all.

## It's working if

- It starts writing rather than asking you a fresh round of questions.
- It puts the seams to you before it writes, and proposes as few as it can get away with.
- It comes back in your project's nouns, not generic product-management boilerplate.
- Every decision in it is one you can remember making. Nothing was invented to fill a section.
- The out-of-scope section has real things in it: the things you refused are usually the most useful lines on the page.
- A local draft reports its path and leaves the remote tracker unchanged; a published specification appears only after an explicit publish request.

## Where it fits

`to-specifications` is a step in the main build chain, and only on the multi-session branch of it:

```txt
grill-with-documentation → to-specifications → to-tickets → implement → code-review
```

Its neighbours upstream are [grill-with-documentation](./grill-with-documentation.md), which does the deciding this skill only records, and [wayfinder](../shaping/wayfinder.md), whose finished map merges onto the chain right here. Downstream, [to-tickets](./to-tickets.md) cuts the specification into tracer-bullet tickets for [implement](./implement.md) to build. When you're unsure which skill or flow fits, [what-is-next](../getting-started/what-is-next.md) routes you.
