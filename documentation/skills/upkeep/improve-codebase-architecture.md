Upstream source: `improve-codebase-architecture`, verified in the `d81f3a1` tree.

## What it does

`improve-codebase-architecture` surveys a codebase for **deepening opportunities**: places where a shallow module (an interface nearly as complex as the thing it hides) could become a deep one. It writes them up as a self-contained HTML report, and then grills you through whichever one you pick.

It never changes the code. The whole run produces one HTML report in `documentation/architecture-audit/` in the repository and a conversation; the refactor itself happens later, in a separate session, through the normal build flow. That is what makes it a survey rather than a refactoring tool, and it is why the skill is worth running on a codebase you are not ready to touch yet.

Two filters keep the report from becoming generic cleanup advice. Every candidate has to pass the **deletion test**: would removing this module concentrate complexity behind a smaller interface, or just spread it across callers? Only the "concentrates" cases earn a card. And unless you point it at a specific area, it reads recent commit history first and biases the scan toward paths that are actively changing, on the grounds that a deepening in code nobody touches is a refactor you will never cash in.

## When to reach for it

Type `/improve-codebase-architecture`, or an agent or another skill can reach for it when the task fits.

It sits outside the build loop: it is not a step in the main loop but something you run periodically to queue up more work to improve the codebase. The four situations it gets used in:

| Situation | How it is used |
| --- | --- |
| Routine upkeep | Run it every few days, or whenever a spare moment appears, to stop structure rotting between features. |
| Before a big build | Point it at the specification: "how can we make this change easy?" This is the most effective prompt for it. |
| Brownfield audit | Run it on a large, unstructured or vibe-coded repository to find out what shape it is actually in. |
| Legacy test work | Use it to find the missing seams first, before writing tests against untestable code. |

Where it is confusable with siblings:

- For designing one module you have already chosen, use [design-modules](../reference/design-modules.md): that is the bench, this is the survey that finds what to put on it.
- For a whole effort too big to hold in one session, use [graphify](../shaping/graphify.md).
- For "this specific thing is broken," use [debug](./debug.md). It hands back here when the real finding is that there is no good seam to lock the bug down.

## Prerequisites

None to run it. When `CONVENTIONS.md` is missing it asks whether to create one. If you accept, [model-domain](../reference/model-domain.md) interviews you about your architecture conventions and rules first; declining is recorded in `.agents/domain.md` and skips it. It reads `GLOSSARY.md` and any ADRs in `documentation/architecture-decision-record/` if they exist, and speaks in your domain's own nouns when they do: a candidate reads as "deepen the Order intake module," not "refactor the FooBarHandler."

The report goes to `documentation/architecture-audit/architecture-audit-<timestamp>.html`, one file per run. Refinement can also sharpen terms in `GLOSSARY.md` and offer an architecture decision record for a consequential rejection. That offer is conditional: rejecting a candidate does not automatically merit a permanent decision record.

## Depth, and the report that hunts for it

The skill turns on one idea: **depth**. A deep module puts a lot of behaviour behind a small, stable interface. A shallow one leaks its implementation through an interface nearly as wide as the code beneath it. The report hunts for shallowness in three forms: pure functions extracted only for testability while the real bugs live in how they are called (no **locality**), modules leaking across their **seams**, and a concept you cannot understand without opening five files. It closes with a proposal for the deepening that fixes it.

Each candidate is a card: the files involved, the friction, a plain-English solution, the benefit stated in terms of **locality** and **leverage**, a before/after diagram, and a strength badge.

| Badge | What it means for you |
| --- | --- |
| `Strong` | The deletion test passes clearly and the friction is real. Take these seriously. |
| `Worth exploring` | Plausible deepening, but the payoff depends on where the code is going next. |
| `Speculative` | Surfaced for completeness. Most of these are safe to ignore. |

The report ends with a **Top recommendation** (the one it would tackle first), and then the skill stops and asks which candidate you want to explore. Nothing has been decided at that point, and no code has moved.

## What happens after you pick one

Picking a candidate starts [refine](../reference/refine.md) over its constraints, seam, surviving tests, and interface. The output is a decision, not a diff. Record agreed behavior through [specify](../workflow/specify.md), then use [taskify](../workflow/taskify.md) when decomposition is useful before [implement](../workflow/implement.md). A small approved living-code batch can instead enter [iterate](../workflow/iterate.md), respecting existing requirements and specifications.

## Common questions

**It grilled me for an hour about one idea instead of showing me options. Can I turn that off?**

Yes: say so when you invoke it ("don't grill me, just show the report"). This is the loudest complaint the skill has. One user put it bluntly: they liked it as "a convenient way to get a thorough analysis of improvements," and after the grilling loop was added found it "borderline unusable," reporting sessions where it proposed a single solution and then asked "10's or 100's of questions." The design intent is that the report comes first and the grill only starts on a candidate you chose, but weaker models skip straight to interviewing you about the first idea they had. Reports in that thread vary sharply by model, and it is an open issue: the skill does not yet have a documented no-grill mode.

**The report opened as unstyled raw HTML with no diagrams. What happened?**

The report loads Tailwind and Mermaid from CDNs, so it needs network access when you open it, and it breaks silently when something blocks those scripts. The filed case was a security hook demanding SRI hashes: the agent added them, the CDN served different bytes to the browser than to the `curl` used to compute the hash, and the browser blocked the script. Offline and locked-down environments hit the same wall. The agent cannot see this, because it never renders the page. The workaround is to ask for inline CSS and hand-built SVG diagrams instead of the CDN scaffold. This is an open issue and a real rough edge.

**It gave me twelve candidates. Do I work through them in the same session or start a new one?**

Prefer one candidate per session. Several candidates mix survey evidence, refinement, and implementation context before you have selected a scope. Reports in `documentation/architecture-audit/` are historical surveys, not living specifications. Record the chosen outcome and evidence in the appropriate current documents; retain other candidates in backlog as deferrals, not automatic authorization. A planned change can use `/specify`; a small approved iterative batch need not manufacture a new specification.

**How should I prompt it?**

With the next thing you are building in mind. Where a big build is coming up, point it at the specification and ask "how can we make this change easy?" An unprompted run scans for hot spots on its own, which is fine for routine upkeep, but naming a direction is what makes the report actionable.

**Does it work on a large legacy codebase?**

Results vary. Users with out-of-control projects reported limited help, and one report on an eight-year legacy codebase described the model going in circles. Bound the survey to an actively changing area and a concrete source of friction. If domain terms are inconsistent, use [model-domain](../reference/model-domain.md) to establish shared vocabulary before comparing designs.

**How is this different from `/design-modules`?**

`/design-modules` is a reference, not a session driver. It supplies the vocabulary (module, interface, depth, seam, adapter, leverage, locality), and this skill borrows it. Pointing a fresh agent at `/design-modules` as the thing to "do" is a known failure: with no process of its own to follow, the agent invents one, re-explores code and runs for a very long time before asking you anything. Drive with this skill; consume that one.

**Will it ever tell me the codebase is fine?**

Rarely, and you should know that going in. The skill is built to output findings, so the framing pushes it toward producing candidates rather than concluding that nothing is wrong. The strength badges are the defence: a report where everything is `Speculative` is the skill telling you it found nothing, in the only way it knows how.

**Does it work in Codex or another harness?**

Partially. The exploration step names Claude Code's `Agent` tool with `subagent_type=Explore` directly, so a harness without that tool may skip the parallel exploration rather than substitute its own. The skill still runs; the scan is just less thorough. A harness-neutral rewrite has been proposed but is not merged.

**How do I actually implement deep modules in TypeScript?**

There is no good answer shipped with the skill. The recurring request is for a `TYPESCRIPT.md` giving concrete file and module layouts for the principles, and it does not exist. The skill will tell you where a deepening belongs and what should sit behind the seam; translating that into a package or directory structure is currently on you.

**What if a skill it calls is not installed?**
It names the missing skill with its install command, carries out that step from its stated intent, and tells you the step ran without it. The skills involved are listed at the top of its [`SKILL.md`](../../../skills/upkeep/improve-codebase-architecture/SKILL.md).

## It's working if

- The candidates name your domain's concepts, not invented class names: "the Order intake module," not "the FooBarHandler."
- The candidates cluster in files you have edited recently, not in dormant corners of the repository.
- No code changed during the run. The only new file is the HTML report in `documentation/architecture-audit/`.
- It stops after the report and asks which candidate you want, rather than continuing on its own.
- Each card explains the payoff as locality or leverage, and says which tests get simpler, not just "this is cleaner."
- A consequential rejection earns an offer to record the decision and reason, so later surveys can account for it.

## Where it fits

`improve-codebase-architecture` is periodic maintenance that generates candidate work rather than implementing it. [design-modules](../reference/design-modules.md) supplies depth-and-seam vocabulary; [refine](../reference/refine.md) explores the selected candidate; [model-domain](../reference/model-domain.md) records settled domain meanings and qualifying decisions. Approved work enters planned or just-in-time development without weakening existing obligations. [guide](../productivity/guide.md) maps both workflows.
