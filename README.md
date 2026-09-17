# Skills For Real Engineers

[![skills.sh](https://skills.sh/b/Dyrits/SKILLS)](https://skills.sh/Dyrits/SKILLS)

Agent skills for real engineering, maintained as an independent fork.

Developing real applications is hard. Approaches like GSD, BMAD, and Specification-Kit try to help by owning the process. But while doing so, they take away your control and make bugs in the process hard to resolve.

These skills are designed to be small, easy to adapt, and composable. They work with any model.

## Origin

This repository started from [Matt Pocock's AI Hero skills](https://aihero.dev/skills). It is now independently maintained and intentionally diverges from that source, so the source website does not document the behavior of this repository.

## Installation (30-second setup)

One way in: [skills.sh](https://skills.sh/Dyrits/SKILLS) copies editable skill files into your project, so you can hack on them and make them your own.

### 1. Get the skills

```bash
npx skills@latest add Dyrits/SKILLS
```

Pick the skills you want, and which coding agents to install them on. **The installer lets you choose which skills to take, so make sure `setup-custom-skills` is one of them.**

It writes the skills into your repository as ordinary files you own and can edit. Nothing updates behind your back; pull the latest changes when you want them with `npx skills update`.

### 2. Run `/setup-custom-skills`

In your agent, run it once per repository. It will:

- Ask where published issues live: local markdown under `backlog/`, or a remote tracker (GitHub, GitLab, Jira, or another workflow you describe)
- Ask whether tickets should follow an existing repository template or ticket-writing skill
- Ask what strings you use for the triage roles (`/triage` reads them)
- Ask where you want to save any documentation we create

Whichever tracker you pick, drafting happens in `.refinement/` and reaches the tracker only when you ask to publish.

### 3. Bam - you're ready to go.

## Why These Skills Exist

I built these skills as a way to fix common failure modes I see with Claude Code, Codex, and other coding agents.

### #1: The Agent Didn't Do What I Want

> "No-one knows exactly what they want"
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**The Problem**. The most common failure mode in software development is misalignment. You think the dev knows what you want. Then you see what they've built - and you realize it didn't understand you at all.

This is just the same in the AI age. There is a communication gap between you and the agent. The fix for this is a **grilling session** - getting the agent to ask you detailed questions about what you're building.

**The Fix** is to use:

- [`/grill-me`](./skills/productivity/grill-me/SKILL.md) - for non-code uses
- [`/grill-with-documentation`](./skills/workflow/grill-with-documentation/SKILL.md) - same as [`/grill-me`](./skills/productivity/grill-me/SKILL.md), but adds more goodies (see below)

These are my most popular skills. They help you align with the agent before you get started, and think deeply about the change you're making. Use them _every_ time you want to make a change.

### #2: The Agent Is Way Too Verbose

> With a ubiquitous language, conversations among developers and expressions of the code are all derived from the same domain model.
>
> Eric Evans, [Domain-Driven-Design](https://www.amazon.co.uk/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215)

**The Problem**: At the start of a project, devs and the people they're building the software for (the domain experts) are usually speaking different languages.

I felt the same tension with my agents. Agents are usually dropped into a project and asked to figure out the jargon as they go. So they use 20 words where 1 will do.

**The Fix** for this is a shared language. It's a document that helps agents decode the jargon used in the project.

<details>
<summary>
Example
</summary>

Here's an example [`CONTEXT.md`](https://github.com/mattpocock/course-video-manager/blob/076a5a7a182db0fe1e62971dd7a68bcadf010f1c/CONTEXT.md), from my `course-video-manager` repository. Which one is easier to read?

- **BEFORE**: "There's a problem when a lesson inside a section of a course is made 'real' (i.e. given a spot in the file system)"
- **AFTER**: "There's a problem with the materialization cascade"

This concision pays off session after session.

</details>

This is built into [`/grill-with-documentation`](./skills/workflow/grill-with-documentation/SKILL.md). It's a grilling session, but that helps you build a shared language with the AI, and document hard-to-explain decisions in architecture decision records.

It's hard to explain how powerful this is. It might be the single coolest technique in this repository. Try it, and see.

> [!TIP]
> A shared language has many other benefits than reducing verbosity:
>
> - **Variables, functions and files are named consistently**, using the shared language
> - As a result, the **codebase is easier to navigate** for the agent
> - The agent also **spends fewer tokens on thinking**, because it has access to a more concise language

### #3: The Code Doesn't Work

> "Always take small, deliberate steps. The rate of feedback is your speed limit. Never take on a task that’s too big."
>
> David Thomas & Andrew Hunt, [The Pragmatic Programmer](https://www.amazon.co.uk/Pragmatic-Programmer-Anniversary-Journey-Mastery/dp/B0833F1T3V)

**The Problem**: Let's say that you and the agent are aligned on what to build. What happens when the agent _still_ produces crap?

It's time to look at your feedback loops. Without feedback on how the code it produces actually runs, the agent will be flying blind.

**The Fix**: You need the usual tranche of feedback loops: static types, browser access, and automated tests.

For automated tests, a red-green-refactor loop is critical. This is where the agent writes a failing test first, then fixes the test. This helps give the agent a consistent level of feedback that results in far better code.

I've built a **[`/test-driven-development`](./skills/workflow/test-driven-development/SKILL.md) skill** you can slot into any project. It encourages red-green-refactor and gives the agent plenty of guidance on what makes good and bad tests.

For debugging, I've also built a **[`/debug`](./skills/upkeep/debug/SKILL.md)** skill that wraps best debugging practices into a disciplined loop, gated phase by phase.

### #4: We Built A Ball Of Mud

> "Invest in the design of the system _every day_."
>
> Kent Beck, [Extreme Programming Explained](https://www.amazon.co.uk/Extreme-Programming-Explained-Embrace-Change/dp/0321278658)

> "The best modules are deep. They allow a lot of functionality to be accessed through a simple interface."
>
> John Ousterhout, [A Philosophy Of Software Design](https://www.amazon.co.uk/Philosophy-Software-Design-2nd/dp/173210221X)

**The Problem**: Most apps built with agents are complex and hard to change. Because agents can radically speed up coding, they also accelerate software entropy. Codebases get more complex at an unprecedented rate.

**The Fix** for this is a radical new approach to AI-powered development: caring about the design of the code.

This is built in to every layer of these skills:

- [`/to-specifications`](./skills/workflow/to-specifications/SKILL.md) quizzes you about which modules you're touching before creating a specification

And crucially, [`/improve-codebase-architecture`](./skills/upkeep/improve-codebase-architecture/SKILL.md) surveys a codebase for deepening opportunities and hands you the candidates. I recommend running it on your codebase once every few days. It is a survey, not a rescue: on a genuinely old codebase it will find real candidates, but it won't untangle the mud for you.

### Summary

Software engineering fundamentals matter more than ever. These skills are my best effort at condensing these fundamentals into repeatable practices, to help you ship the best apps of your career. Enjoy.

## Reference

These split on one axis: who can invoke them. **User-invoked** skills are reachable only when you type them (e.g. `/grill-me`); their job is to orchestrate. **Model-invoked** skills can be invoked by you _or_ reached for automatically by the agent when the task fits; they hold the reusable discipline. A user-invoked skill may invoke model-invoked skills, but never another user-invoked one.

### Getting Started

Set up once, then find your way around.

- **[setup-custom-skills](./skills/getting-started/setup-custom-skills/SKILL.md)**: Configure this repository for the workflow skills (issue tracker: local markdown or remote, ticket-writing convention, triage roles, domain documentation layout). Run once per repository.
- **[what-is-next](./skills/getting-started/what-is-next/SKILL.md)**: The router: which skill or flow fits your situation, or which boundary option (continue, clear, hand-off, compact) fits the moment.

### Workflow

The idea→ship spine, in order.

- **[grill-with-documentation](./skills/workflow/grill-with-documentation/SKILL.md)**: Grilling session that also builds your project's domain model, sharpening terminology and updating `CONTEXT.md` and architecture decision records inline.
- **[design-workflow](./skills/workflow/design-workflow/SKILL.md)**: Grilling session that turns the recurring loops in your work into implementable workflow specifications, using the current directory as a stateful workspace.
- **[to-specifications](./skills/workflow/to-specifications/SKILL.md)**: Turn the current conversation into a local draft specification, or publish it to the issue tracker when requested. No interview, just synthesizes what you've already discussed.
- **[to-tickets](./skills/workflow/to-tickets/SKILL.md)**: Break any plan, specification, or conversation into a set of tracer-bullet tickets, each declaring its blocking edges, written as text in a local file, or as native blocking links on a real tracker.
- **[implement](./skills/workflow/implement/SKILL.md)**: Build the work described by a specification or set of tickets, driving `/test-driven-development` at pre-agreed seams and closing out with `/code-review` before committing.
- **[implement-all](./skills/workflow/implement-all/SKILL.md)**: Implement a whole specification on one branch: works the tickets as a task graph, running implementer subagents across the ready frontier for concurrency, landing a single PR.
- **[test-driven-development](./skills/workflow/test-driven-development/SKILL.md)**: Test-driven development with a red-green-refactor loop. Builds features or fixes bugs one vertical slice at a time.
- **[code-review](./skills/workflow/code-review/SKILL.md)**: Two-axis review of the diff since a fixed point: **Standards** (does it follow the repository's coding standards, plus a Fowler smell baseline?) and **Specification** (does it faithfully implement the originating issue/specification?), run as parallel sub-agents so neither pollutes the other.

### Shaping

Explore an open question and produce a decision or answer that feeds the flow.

- **[wayfinder](./skills/shaping/wayfinder/SKILL.md)**: Plan a huge chunk of work, more than one agent session can hold, as a shared map of decision tickets on the issue tracker, and resolve them one at a time until the way to the destination is clear.
- **[research](./skills/shaping/research/SKILL.md)**: Investigate a question against high-trust primary sources and capture the findings as a cited Markdown file in the repository, run as a background agent.
- **[prototype](./skills/shaping/prototype/SKILL.md)**: Build a throwaway prototype to answer a design question, either a single shareable HTML file for state/logic questions, or several radically different UI variations toggleable from one route.

### Upkeep

Keep the codebase and issue list healthy; generates work for the flow.

- **[triage](./skills/upkeep/triage/SKILL.md)**: Move issues through a state machine of triage roles.
- **[debug](./skills/upkeep/debug/SKILL.md)**: Disciplined diagnosis loop for hard bugs and performance regressions: build a feedback loop that goes red on this bug → minimise → hypothesise → instrument → fix → regression-test.
- **[improve-codebase-architecture](./skills/upkeep/improve-codebase-architecture/SKILL.md)**: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- **[resolve-merge-conflicts](./skills/upkeep/resolve-merge-conflicts/SKILL.md)**: Work through an in-progress git merge or rebase conflict hunk by hunk, resolving by intent traced to each side's primary source, then finish the operation (never `--abort`).

### Productivity

Human-facing workflows you run, not about code.

- **[grill-me](./skills/productivity/grill-me/SKILL.md)**: Get relentlessly interviewed about a plan or design until every branch of the design tree is resolved.
- **[ask-someone-else](./skills/productivity/ask-someone-else/SKILL.md)**: Turn a decision you can't answer alone into a Markdown questionnaire for the one person who can, filled in async, or together over a meeting. It grills you about the send (who it's for, what you need back), not the subject.
- **[wait-what](./skills/productivity/wait-what/SKILL.md)**: Fire this the moment a message doesn't land. The agent re-pitches it with the context you were missing, in plain English, using your `CONTEXT.md` vocabulary.
- **[hand-off](./skills/productivity/hand-off/SKILL.md)**: Compact the current conversation into a versioned handoff document in `.agents/handoffs/`.
- **[take-over](./skills/productivity/take-over/SKILL.md)**: Resume work from the latest handoff in `.agents/handoffs/`, following the supersedes chain deeper only when needed.
- **[teach](./skills/productivity/teach/SKILL.md)**: Teach the user a new skill or concept over multiple sessions, using the current directory as a stateful teaching workspace.

### Reference

The reusable layer other skills invoke or cite.

- **[grilling](./skills/reference/grilling/SKILL.md)**: Interview the user relentlessly about a plan, decision, or idea until every branch of the design tree is resolved. The reusable interview primitive behind `grill-me`, `grill-with-documentation`, `triage`, `wayfinder` and `improve-codebase-architecture`.
- **[domain-modeling](./skills/reference/domain-modeling/SKILL.md)**: Actively build and sharpen a project's domain model: challenge terms against the glossary, stress-test with edge-case scenarios, and update `CONTEXT.md` and ADRs inline.
- **[codebase-design](./skills/reference/codebase-design/SKILL.md)**: Shared discipline and vocabulary for designing deep modules: a lot of behaviour behind a small interface, placed at a clean seam, testable through that interface.
- **[writing-for-agents](./skills/reference/writing-for-agents/SKILL.md)**: Writing documents for agents: skills, AGENTS.md/CLAUDE.md, and any doc an agent reaches by a pointer.
- **[wizard](./skills/reference/wizard/SKILL.md)**: Generate an interactive bash wizard that walks a human through steps only they can perform: provisioning infrastructure, setting up credentials or CI secrets, walking an unfamiliar third-party dashboard, or running a one-off migration or cutover.

### Experimental

These skills take externally visible actions on pull requests, merge requests, issues, or tickets. They are available for direct installation, but are not included in the plugin while their workflows are being proven.

- **[address-feedback](./skills/experimental/address-feedback/SKILL.md)**: Assess every substantive comment on a pull request, merge request, issue, or ticket; implement the approved change plan; then draft and post a reply to each comment.
- **[publish-message](./skills/experimental/publish-message/SKILL.md)**: Post a short comment to a GitHub or GitLab pull request or merge request, or a Jira issue, leading with the reason rather than restating the diff or ticket.
- **[publish-review](./skills/experimental/publish-review/SKILL.md)**: Publish a finished code review to the tracker as a summary comment and, on GitHub or GitLab, concretely fixable inline suggestions.
