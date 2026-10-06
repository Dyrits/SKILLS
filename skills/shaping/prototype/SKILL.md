---
name: prototype
description: Build a scoped experimental prototype to answer a user-requested or approved design question about logic, state, or UI. Use when the user asks to try an idea before committing to it, or to see a state model or interface variants.
metadata:
  forks: "mattpocock/skills/skills/engineering/prototype"
---

# Prototype

A prototype is **experimental code that answers a question**. The question decides the shape. Proceed only when the user requests or approves the scoped experiment, including during specify. Living iteration directly evolves the implementation; it does not require a prototype by default.

**Calls:** `document`. If a called skill is not installed, tell the user its name and install command, `npx skills@latest add Dyrits/SKILLS --skill=<name>`, then carry out that step from its stated intent and report the step as done without the skill. Without `document`, wait until the user installs it or tells you to proceed: this skill's rules use its terms. **Hands over to:** `/iterate`. When one is not installed, give the user its install command, `npx skills@latest add Dyrits/SKILLS --skill=<name>`, along with the instruction to run it.

Call the Skill tool with "document" for shared project-document ownership. Record unresolved proposals separately from agreed behavior. Capture the question, verdict, evidence, and remaining acceptance in the feature's draft or specifications as appropriate, and in working state. Record completed agreements in the root `CHANGELOG.md`, stating that the prototype's code still needs production validation.

## Pick a branch

Identify which question is being answered, using the user's prompt, the surrounding code, or by asking if the user is around:

- **"Does this logic / state model feel right?"** → [LOGIC.md](LOGIC.md). Build a single shareable HTML file (free-play buttons plus tabbed guided walkthroughs) that pushes the state machine through cases that are hard to reason about on paper, and that a non-developer can drive.
- **"What should this look like?"** → [UI.md](UI.md). Generate several radically different UI variations on a single route, switchable via a URL search param and a floating bottom bar.

A request to build a whole application is not a prototype. Ask which single question the experiment should answer and narrow to it; when the user wants the application itself, tell the user to run `/iterate`.

The two branches produce very different artifacts, so getting this wrong wastes the whole prototype. If the question is genuinely ambiguous and the user isn't reachable, default to whichever branch better matches the surrounding code (a backend module → logic; a page or component → UI) and state the assumption at the top of the prototype.

## Rules that apply to both

1. **Experimental from day one, and clearly marked as such.** Keep the experiment isolated from application behavior and production delivery. Locate it near the relevant module or page when useful, and name it clearly as a prototype. For experimental UI routes, follow the project's routing conventions.
2. **Trivial to run.** A UI prototype starts from one command in the project's task runner: `pnpm <name>`, `python <path>`, `bun <path>`, etc. A logic demo is a single HTML file the user double-clicks. Either way, no thinking required to start it.
3. **No persistence by default.** State lives in memory. Persistence is the thing the prototype is _checking_, not something it should depend on. If the question explicitly involves a database, hit a scratch DB or a local file with a clear "PROTOTYPE, wipe me" name.
4. **Skip the polish.** No tests, no error handling beyond what makes the prototype _runnable_, no abstractions. The point is to learn something fast.
5. **Surface the state.** After every action (logic) or on every variant switch (UI), print or render the full relevant state so the user can see what changed.
6. **Capture it when done.** Preserve the experiment as a primary source with a context pointer in the relevant work record. Keep unselected experiments outside production. Validated useful code may be integrated without mandatory rebuilding, but only after authorized acceptance and the application's production checks, including tests, error handling, appearance and interaction acceptance where judgment is needed. Remove experimental controls and labels from integrated code. A successful experiment alone establishes no production-readiness claim.
