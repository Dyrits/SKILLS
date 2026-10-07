Upstream source: `research`, verified in the `d81f3a1` tree.

## What it does

`research` answers a question by reading primary sources and leaves a cited Markdown file in the repository. Official documentation, source code, specifications, and first-party APIs qualify; a blog post's account of an API does not replace the API's own documentation.

It does not answer you in the conversation. The output is a file, written where the repository already keeps such notes, with a link on each claim. That is the point: a document you can react to, hand to another agent, or throw away, rather than an answer that vanishes when the session ends.

## When to reach for it

Type `/research`, or an agent can reach for it when a task turns into reading legwork.

Reach for it when the next step is *finding something out* from outside the working directory (how a third-party API behaves, what a specification actually says, whether a version claim holds), and you'd rather not stall your own thread doing the reading. What you need decides which skill:

| What you need | Reach for |
| --- | --- |
| An external fact a decision is waiting on | `research` |
| A decision made with you, by interview | [interview](../shaping/interview.md) |
| Agreed capability behavior that needs a durable local record | [specify](../workflow/specify.md) |
| To find out whether an approach works in your codebase | [prototype](./prototype.md) |
| A plan too big to hold in one session | [graphify](./graphify.md) |

The distinction is between **facts and agreements**. Research captures what a source says at a particular version or date. Refinement makes a decision with you, and specification records agreed behavior. Findings can inform an agreement, but are not approval to change it. Keep evidence useful to later readers and recheck facts whose source or version has changed.

## Delegated legwork

The defining move is that the reading runs as a **background agent**. You keep working; it goes off, follows each claim to its primary source, writes one Markdown file, and reports back. Research is legwork you delegate, not thinking you outsource: you get a document to grill, plan, or design against, and you still make the call.

The skill tells an agent that is already a subagent to do the research itself, so the background agent should not spawn another. The guard is an instruction, not a structural limit; the history is under the common questions.

Where the file lands is decided by the repository, not by the skill: it matches whatever convention already exists for notes, and if there is none it picks somewhere sensible and tells you where. It writes one file per run.

## Common questions

**It spawned a second research agent. Is that meant to happen?**

Not any more here. It was an open bug upstream, [issue #530](https://github.com/mattpocock/skills/issues/530). The skill tells its caller to spin up a background agent but does not restrict the agent type, so the agent it spawns is a `general-purpose` one that holds the `Agent` tool and the same instructions, and fires them again. One reporter measured a single research task costing roughly 450k tokens across three overlapping runs, with the duplicate finishing half an hour later entirely out of view. It reproduces outside Claude Code too; the same nesting was confirmed in Codex with GPT-5.6-sol. This fork carries the fix users patched in themselves: a line telling an agent that is already a subagent to do the work itself. It is instruction-level, not structural, so watch your background task list after invoking, and stop a duplicate if one appears.

The opposite failure exists as well: if your own global instructions forbid an agent from re-delegating work, the background agent will politely decline the task and the skill quietly does nothing.

**Where should the file live, and should I commit it?**

The skill puts the file where the repository already keeps notes and does not have an opinion beyond that. The community one is fairly settled: ADRs are kept, research files are not. The sharpest version of it, from a Discord thread on exactly this question: "ADRs yes. Everything else archive or delete after done. It otherwise becomes cruft of work and can poison future repository reads if you've drifted away from the specification/research." A research file records what was true on the day it was written, so a stale one is worse than none. On balance these artifacts don't really belong in git, and there is no canonical home for them: people use Obsidian, a separate knowledge repository, or the issue tracker instead.

**What counts as a "high-trust" primary source, and who decides?**

The agent selects sources. The skill names qualifying kinds but provides no allowlist or independent verification pass. An early objection asked how multiple research agents could avoid producing confident answers from poor sources. The citation on each claim is your practical check: follow several and confirm they reach the official documentation or actual source, at the relevant version, rather than someone else's summary.

**Does a later session reuse what an earlier run found?**

No. Nothing auto-loads a past research file; it is a document sitting in the repository until a human or a skill points at it. This was raised early as the strongest challenge to the design: "the value's the markdown becoming context the agent re-reads later, not the fetch itself. A write-once dead file is just a fancy search." The shipped skill does not solve it. In practice the file earns its keep by being fed into the next step deliberately: attach it to a specification, quote it into a grilling session, point a ticket at it.

**Why not just ask the agent to read the documentation?**

You can, and a two-line prompt saying exactly that was the practice this skill replaced. Two things the skill buys over the prompt: it runs in the background so your session keeps its context clean, and the primary-source constraint and the cited-file output come out the same way every time rather than however you happened to phrase it. Against a harness's own deep-research mode, the difference is the artifact and the source discipline, not the search. If a two-line prompt gets you what you need on a small question, use the two-line prompt.

**When does it stop reading?**

There is no stopping criterion in the skill, and this shows up as two complaints that look opposite but are the same gap: agents that go far too deep, and agents that cover a topic broadly while missing the one specific detail that mattered. One practitioner put it as "deep-research skills are a bit too deep sometimes. And telling an agent to research usually results in missing crucial details." Scoping is on you. A narrow, answerable question (one API, one behaviour, one version claim) comes back far better than "research X".

**`/graphify` created research tickets. Do I resolve those myself?**

No. Graphify's charting session starts a subagent for each research task, following Graphify's own copy of these research steps, and captures findings on a throwaway `research/<name>` branch with a context pointer from the task. Parallel research tasks are the exception to Graphify's one-decision-task-per-session rule because they are agent-driven. Historical upstream evidence reports a subagent opening a draft pull request from a branch never meant to merge ([issue #576](https://github.com/mattpocock/skills/issues/576)); that report is not a claim about the current fork. Deleting a findings branch can still break the task's context pointer.

## It's working if

- Your own session keeps going. If you are sitting watching it read, the delegation didn't happen.
- Exactly one new background task appears. A second one with a near-identical name is the nesting bug.
- One new Markdown file shows up, in the folder the repository already uses for notes, and the agent tells you the path.
- Claims carry citations to official documentation, specifications, or actual source files.
- Findings identify the relevant version and separate sourced facts from unresolved uncertainty.
- The file supplies the evidence needed for your decision without implying that research itself approved a change.

## Where it fits

`research` is a reach-for-it-anytime standalone that feeds [interview](../shaping/interview.md), [specify](../workflow/specify.md), and [graphify](./graphify.md) with cited facts. [iterate](../workflow/iterate.md) also uses it when an external unknown blocks an approved batch. [guide](../productivity/guide.md) maps the workflows.
