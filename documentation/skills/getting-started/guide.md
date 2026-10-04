Upstream source: `ask-matt`, verified in the `d81f3a1` tree. This fork renamed the router to `guide` and extended it to planned and just-in-time development. Previously named `what-is-next` in this fork; `guide` reads as a command (`/guide`) and as what it gives you.

## What it does

`guide` is the router over the skills in this repository. You describe the situation you are in (an idea you cannot start, a pile of incoming bug reports, a session that has run long), and it names the skill or the sequence of skills that fits, plus where the human decisions in that sequence sit.

It recommends and stops. It reads the relevant skill before making a consequential claim about its behavior, but does not start the recommended work. It is a maintained map of this repository's skills, not a scan of everything you have installed.

## When to reach for it

Type `/guide`, or an agent or another skill can reach for it when the task fits.

| Your situation | What the router gives back |
| --- | --- |
| A project whose AI tooling needs setup | [setup-ai-tooling](./setup-ai-tooling.md), also offered as an optional stage of [setup-ai-workspace](./setup-ai-workspace.md) |
| Tools are configured and you want evidence of their benefit | [monitor-ai-tooling](../upkeep/monitor-ai-tooling.md), reports from existing measurements |
| A task should run outside the original checkout | [work-in-tree](../version-control/work-in-tree.md), establishes isolation before editing |
| Committed work in a worktree needs to reach its original local branch | [sync-tree](../version-control/sync-tree.md), transfers locally rather than publishing upstream |
| Local branches need rebasing onto a target | [rebase](../version-control/rebase.md), verifies the result and asks separately before publication |
| Git has already stopped on conflicts | [resolve-merge-conflicts](../version-control/resolve-merge-conflicts.md), which resolves the current operation rather than starting a batch of rebases |
| Agents keep rebuilding the same helper or relearning the same lesson | [memorize](../reference/memorize.md), files lessons where the next agent will look and checks there first, including saved scripts |
| An idea, and no idea where to start | A choice between planned development, just-in-time development, and clarification without development |
| Bugs and requests arriving from other people | The [triage](../upkeep/triage.md) on-ramp, and why tickets you generated yourself don't belong on it |
| Two skills that look interchangeable | [refine](../reference/refine.md) clarifies a decision; [specify](../workflow/specify.md) records agreed capability behavior; [graphify](../shaping/graphify.md) maps a large effort's unresolved decisions |
| A long session and a decision about the context | A session boundary that preserves authoritative work state |
| An explanation you need to see | [illustrate](../productivity/illustrate.md) for a visual, or [re-explain](../productivity/re-explain.md) for a clearer explanation |
| A skill you have already picked | Nothing useful. Invoke that skill directly. |

## Prerequisites

The router names skills; it does not install them.
Everything it points at has to be installed for the recommendation to be actionable. The plugin ships every skill outside `deprecated/`, so installing the plugin or the whole set covers it.

For tracker-dependent work, the router asks you to run [setup-ai-workspace](./setup-ai-workspace.md) when tracker configuration is missing. Local just-in-time work does not require tracker setup merely to maintain its working documents.

## Flows, not skills

The useful idea is a **flow**, a path through skills that preserves agreements and progress. Choose the development workflow before choosing the next command:

| What you need | Route |
| --- | --- |
| Explicit planning and execution | [specify](../workflow/specify.md), [taskify](../workflow/taskify.md), [implement](../workflow/implement.md), then [review-and-refactor](../workflow/review-and-refactor.md). Skip task decomposition when a small approved scope does not need it. |
| Discover behavior while building a living application | [iterate](../workflow/iterate.md) clarifies, implements, and verifies one useful batch at a time. |
| Clarify a decision without starting development | [refine](../reference/refine.md). Its caller records useful results in the appropriate documents. |

`specify` asks only about unresolved decisions. A user-approved [prototype](../shaping/prototype.md) settles a question conversation cannot; its answer and evidence feed the specification. Useful validated code can be productionized after appropriate checks without a mandatory rebuild. [research](../shaping/research.md) resolves consequential unknown external facts.

`iterate` primarily maintains `documentation/backlog.md`, `documentation/work-in-progress.md`, and root `CHANGELOG.md`. A remote backlog is linked rather than copied; working state stays local for execution and resumption. It reads existing requirements and specifications without forcing new capability documents or tasks. When scope or competing outcomes prevent selecting an increment, [prioritize](../shaping/prioritize.md) recommends a bounded focus and asks for approval. One completed outcome does not authorize the next.

Both workflows share project-owned documents:

- Requirements hold global and optional additional capability constraints.
- `documentation/capabilities/<capability>/specifications.md` holds living agreed behavior and acceptance. `draft.md` holds unresolved proposals only.
- `documentation/capabilities/<capability>/tasks/` holds local task bodies. After explicit remote publication, a local task becomes a title and link to the authoritative remote task. Specifications stay canonical locally.
- Backlog holds candidates and deferrals, not authorization. Work-in-progress holds unfinished current work and recovery state.
- The single root changelog records meaningful agreements and verified deliveries. Types are `Documentation`, `Code`, or `Configuration`; events are `Agreement` or `Delivery`. The planned workflow writes full records; `iterate` writes light ones with the same heading and vocabulary.

Create these files when useful. Local upkeep is autonomous within authorized scope; when an obligation conflicts with the work, the agent asks you instead of relaxing it.

For publishing conclusions already reached, [publish-message](../productivity/publish-message.md) requires approval of the exact text and destination. [address-feedback](../workflow/address-feedback.md) assesses review feedback from any source. [draft-merge-request](../version-control/draft-merge-request.md) writes the request body, not the publication.

## On-ramps and supporting work

| Situation | Next move |
| --- | --- |
| A large effort has too many unresolved decisions | [graphify](../shaping/graphify.md) maps decisions; refinement, research, or approved experiments resolve them. |
| A recurring operational loop needs an implementable design | [design-workflow](../productivity/design-workflow.md). |
| An architectural seam causes friction | [improve-codebase-architecture](../upkeep/improve-codebase-architecture.md), then explore one selected candidate. |
| Another person has the missing answers | [ask-someone-else](../productivity/ask-someone-else.md), then bring the answers into refinement or specification. |
| An approved task graph needs concurrent implementation | [divide-and-conquer](../workflow/divide-and-conquer.md), instead of individual task sessions. |
| Behavior needs a red/green check | [test-first](../workflow/test-first.md), at an agreed seam. |
| A known failure needs diagnosis | [debug](../upkeep/debug.md), starting with a tight reproduction loop. |
| Learning is a continuing project | [teach](../productivity/teach.md), in a dedicated teaching workspace. |
| A recurring process has waiting, rework, or handoff friction | [optimize-process](../productivity/optimize-process.md), using evidence from actual cycles. |
| Domain terms are inconsistent | [model-domain](../reference/model-domain.md). |
| A module needs a deeper interface or useful seam | [design-modules](../reference/design-modules.md). |
| Project documents need maintenance | [document](../reference/document.md), preserving their separate responsibilities. |
| Skills or steering instructions need clearer agent-facing text | [write-for-agents](../reference/write-for-agents.md). |
| A manual dashboard, credentials, or cutover step blocks automation | [walk-through](../productivity/walk-through.md). |
| Writing needs filler and AI patterns removed | [unslop](../reference/unslop.md). |

Setup and outbound skills it also routes to:

- [setup-delegation-policy](./setup-delegation-policy.md) configures machine-wide delegation and model tiers.
- [setup-git-hooks](./setup-git-hooks.md) configures versioned commit checks.
- [setup-git-guardrails](./setup-git-guardrails.md) asks before destructive Git operations at supported enforcement points.
- [setup-auto-handoff](./setup-auto-handoff.md) gates supported compaction on a fresh handoff.
- [classify](../productivity/classify.md) sends approved safe-to-send text to a third-party classifier and retains uncertain results.

## The phase boundary

At a **session boundary**, keep authoritative work state current before changing context.

| Option | Take it when |
| --- | --- |
| Continue | The current context remains relevant to the next step. |
| Clear | The next task is self-contained and authoritative sources preserve what it needs. |
| [hand-off](../productivity/hand-off.md), then [take-over](../productivity/take-over.md) | Moving between sessions, workspaces, or agents needs session-specific context and source pointers. |
| Compact | You need the same session with less conversational detail; preserve unresolved agreements, running assignments, and recovery pointers first. |

Work-in-progress does not replace a session handoff. The handoff supplies context and pointers rather than copying every project document. Scoped independent work can be delegated without changing the parent session.

## Common questions

**Isn't there just a list of the skills in the right order?**

Planned development has an order, but it is not the only workflow. Use `specify`, optional `taskify`, `implement`, and review when explicit planning helps. Use `iterate` for approved living-code batches. The branches matter: existing agreements may settle the next step, or an experiment may still be needed. The router is maintained by hand, so compare consequential recommendations with the skill itself.

**It told me half the skills aren't installed.**

This is a reported harness failure. Skills may be omitted from the list visible to the model, which then mistakes that list for the installation inventory. Check `.claude-plugin/plugin.json` and your installed command list. An omitted model listing does not establish that a command is missing.

**It described a skill's behaviour, and the skill doesn't do that.**

Earlier reports found recommendations based only on summaries, including skipped planning work that undercounted tasks. The current router explicitly reads the relevant `SKILL.md` before a consequential behavioral claim. If that evidence is missing from the trace, ask it to verify. Advice outside the map, such as harness plan-mode choices, remains an inference unless supported separately.

**Why is it prose instead of a numbered checklist?**

A fair complaint, filed as an open issue arguing that most of the routing is deterministic and the narrative makes it hard to scan. Nothing stops you asking for the compressed form: "just give me the sequence" gets you the sequence. What the prose is carrying is the conditional half: the branches, where a human decision is expected, and where to clear or compact between steps. A flat checklist drops exactly that.

**Can it route over my own skills, or another author's?**

No. Three separate proposals have asked for a router that reads your local `skills/` directory and recommends from whatever is installed. `guide` is not that. It is a map of one set, maintained by hand, and it knows nothing about skills you wrote or installed from elsewhere.

**It told me to edit a SKILL.md.**

That advice is often correct and rarely durable. Someone asked it how to make [implement](../workflow/implement.md) close tickets, got told to add a line to the skill, and immediately spotted the problem: `npx skills update` overwrites the file, and the plugin install is read-only. Put standing behaviour in your own `CLAUDE.md` or `AGENTS.md`, or say it in the invocation. Prompt-level adaptations survive updates: pointing the flow at Linear instead of GitHub, or asking it which open tickets could run in parallel, are both things people do this way.

**It named a skill I don't have, or missed one I do.**

Check the changelog for a rename before assuming a skill is gone. Older planning commands now lead to [specify](../workflow/specify.md) and [taskify](../workflow/taskify.md); the general interview is [refine](../reference/refine.md), and the explanation repair is [re-explain](../productivity/re-explain.md). These are current names, not aliases. Promotion depends on a manifest entry, not a bucket move.

**Does choosing just-in-time work discard existing specifications?**

No. It changes how the next batch is selected and delivered, not its obligations. Applicable requirements and living specifications still govern. Work-in-progress can establish approved scope for a small batch without another specification; conflicting records must be surfaced rather than quietly rewritten.

**Are specifications snapshots of the original plan?**

No. They are living agreed behavior and acceptance. Drafts keep unresolved alternatives separate, and the root changelog preserves meaningful agreement and delivery history. A historical survey or research report can drift from the current agreement; use it as evidence, not as an override.

## It's working if

- It ends by naming what to type and stops there, instead of starting the work itself.
- The route it gives back mentions where to clear or compact context and where you are expected to review, not just a list of skill names.
- Where two skills are close, it says which one and why the other is wrong for you.
- Any claim it makes about another skill's behaviour shows up in the trace as it reading that skill's `SKILL.md`.
- You recognise your own situation in what it hands back, rather than the nearest generic scenario.

## Where it fits

`guide` is a standalone router over both development workflows and the supporting skills. It recommends and stops. [specify](../workflow/specify.md) starts planned development; [iterate](../workflow/iterate.md) runs just-in-time batches; [triage](../upkeep/triage.md) verifies work arriving from other people. [improve-skills](../upkeep/improve-skills.md) reviews how the skills behaved in a session and reports problems on this repository; [improve-environment](../upkeep/improve-environment.md) changes the project's environment after a session's friction.

It is a secondary source over the skills it describes. Where the router and a `SKILL.md` disagree, the `SKILL.md` is right.
