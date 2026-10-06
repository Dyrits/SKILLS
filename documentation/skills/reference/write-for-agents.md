Upstream source: `writing-for-agents`, verified in the `d81f3a1` tree, now `write-for-agents` in this fork.

## What it does

`write-for-agents` guides writing a skill, steering file, specification, runtime prompt, or other document an agent reads. It aims for predictable process across runs, not identical output.

It keeps requirements and approval boundaries intact while removing duplication, clarifying references, and making completion criteria checkable. This fork replaces the unconditional search for shorter wording with a conditional test: change text when there is an identifiable improvement, and leave it alone when there is not.

It was called `writing-great-skills` until v1.1. The rename reflects its wider scope. For skill-authoring work, it requires reading [Anthropic's skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) and the bundled [skill mechanics reference](../../../skills/reference/write-for-agents/SKILL-MECHANICS.md). The official page owns current frontmatter requirements; the local reference covers invocation conventions, splitting, and routers without copying those requirements.

## When to reach for it

Type `/write-for-agents`, or an agent or another skill can reach for it when you're creating or editing a skill, or modifying `AGENTS.md`.

Reach for it by hand for other agent-facing documents, specifications, tasks, and unattended prompts. The test is whether an agent reads the text. [specify](../workflow/specify.md) establishes agreed capability behavior; [document](./document.md) owns the project-document model. This reference governs how the instructions read, not what behavior the project should agree to.

## The two loads

The idea the whole reference turns on is a pair of budgets every document and pointer spends:

- **Context load**: the cost of always-loaded material on the agent's window: an `AGENTS.md` line, a skill description, anything sitting in context every turn whether or not it fires.
- **Cognitive load**: the cost on you, namely which documents exist and when to reach for each. You are the index. Not a cost to minimise: it is the price of human agency.

Once you think in these two loads, most authoring decisions (split or don't, inline or disclose, point or push) become the same trade made in different places.

## Key concepts

- **Context pointers** name reference material and state when to read it. Skill descriptions and references in `AGENTS.md` both need clear conditions.
- **Information hierarchy** separates common steps, in-file reference, and conditional reference loaded through a pointer. **Progressive disclosure** moves substantial conditional detail out of the main file.
- **Completion criteria** state both what counts as done and what coverage the work requires. Clear criteria come before experimenting with workflow splits.
- **Leading words** refer back to an idea without restating it. Use them for repeated ideas only when the requirements remain clear.
- **Pruning** checks relevance, duplication, and suspected no-ops while preserving obligations. Editorial judgment is distinguished from evidence obtained through comparative runs.

## Common questions

**Where did `/writing-great-skills` go?**
It is this skill, renamed upstream in v1.1. Its structure, leading words, and pruning apply to steering documents, specifications, tasks, and runtime prompts as well as skills. There is no alias; update saved references to the current name.

**"Writing for agents": so the agent does the writing?**
The name identifies the reader. A person or an agent can write the document, but its instructions are intended for an agent to follow. Include the task-specific context it needs instead of assuming it knows your project's constraints.

**Can't I just ask the agent to write it for me?**
Yes. This reference supplies criteria for drafting and reviewing the result: clear reading conditions, checkable completion criteria, and preserved requirements. A review may conclude that no change is needed.

**I asked an agent to trim a document and it cut the functionality.**
Shorter text is not proof of improvement. The skill requires preserving obligations, exceptions, approval boundaries, and recovery instructions. A no-op is a behavioral claim; without comparative runs, it remains an editorial judgment rather than a demonstrated result.

**How do I know when it's done?**
When the identified problems have been addressed without losing requirements. It does not require finding an edit in every document. Repository checks can establish format and link consistency, but they do not prove improved model behavior.

**Does `skill-creator` become a required dependency for every edit?**

No. It is an optional external dependency from `anthropics/skills`, invoked for requested skill evaluations or behavioral comparisons. It is not bundled by this collection. If it is missing, the agent provides its installation command and asks whether to install it or leave the comparison pending. Ordinary editing, including an explicit decision to defer evaluations, does not invoke it.

**Will the official guidance still be available when I install this skill elsewhere?**

The skill itself carries the link and the instruction to read it before creating or editing a skill or its description. It does not depend on this repository's `AGENTS.md`. If the page cannot be accessed, the agent must report that limitation.

**Should this live in `AGENTS.md` or somewhere else?**
Ask which load you want to pay. `AGENTS.md` loads into every session unconditionally; material behind a pointer costs only the pointer's own line until it fires. Anything that applies in one context out of ten is paying context load the nine other times.

**Do I need to rewrite my documents for each new model?**
Use observed failures to decide what needs attention. The same wording may behave differently across models, but a model change alone does not establish that an instruction needs rewriting.

**My skill only works on the exact task I built it from.**
The common route (do the work once, then have the agent write it up as a skill) over-indexes on that one run, and the exemplars come out too specific. Keep the run as evidence, then abstract deliberately: strip what belonged to that repository and those files, and write for the class of task.

**Should every batch create requirements, specifications, and tasks?**

No. [document](./document.md) owns the shared project-document rules. Existing requirements and agreed specifications still apply, but a small living-code batch can use backlog, work-in-progress, and the root changelog without creating new capability documents. Write instructions that preserve obligations while creating records only when useful; clarity is not a reason to duplicate the same agreement in several files.

**English isn't my first language. Do I lose the leading-word advantage?**
The technique does not require English. Use familiar, consistently defined terms in the document's language, and keep the explicit instruction if a shorter term would lose meaning.

## It's working if

- Revisions address identifiable problems without dropping requirements or approval boundaries.
- A leading word refers back to a clear definition rather than hiding an important requirement.
- The agent distinguishes editorial checks from measured behavioral results and can leave useful text unchanged.
- Reference that only one branch needs sits behind a pointer rather than in the main file.

## Where it fits

This is a standalone reference used within authoring tasks, not another delivery stage. [memorize](./memorize.md) loads it before filing a lesson in a steering file; [document](./document.md) owns shared project-document responsibilities. Requested skill evaluations use the external `skill-creator` workflow. When you're unsure which skill or flow fits a task, [guide](../productivity/guide.md) helps choose.
