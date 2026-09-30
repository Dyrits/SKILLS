---
name: implement-all
description: "Implement the result of /to-specifications and /to-tickets in code."
disable-model-invocation: true
---

You have been provided a specification. This specification should have tickets associated with it, describing how to implement the specification.

Read `documentation/agents/issue-tracker.md` for the configured tracker workflow. If it is missing, tell the user to run `/setup-custom-skills`.

The goal is the entire specification implemented on a single **integration branch**, with every ticket resolved the way the issue tracker closes work.

The tickets are not a list of steps. They are a **task graph** with blocking relationships between them. This means there is always a **frontier** of tickets which are ready to be grabbed.

Communication to and from subagents should be sparse. Communicate primarily through **context pointers**: to the specification, tickets, research notes, and previous commits. Don't duplicate information already available via pointers.

**Implementer subagents** should be run in the background where possible for maximum concurrency.

## Steps

1. Read the specification and tickets to understand the task graph.

2. (optional) Use an **exploration subagent** to conduct any exploration required by the tickets - relevant codebase files or external documentation. Ensure the exploration subagent can save files - it should save its markdown notes in a directory outside the repository, accessible by all future subagents. This lets **implementer subagents** focus on implementation rather than exploration.

3. Create the integration branch. If the issue tracker closes work through pull or merge requests, or the user asks for one, open a draft request after the first merge in step 5, when the branch has commits ahead of the target branch. Mark it as closing the specification and tickets, using the configured tracker workflow, and call the Skill tool with `to-pull-request` for its body.

4. Use **implementer subagents** to implement each ticket, each in its own worktree on its own branch. Each implementer subagent:
   - confirms its worktree is based on the integration branch before starting, and rebases its own ticket branch onto it if needed;
   - calls the Skill tool with `test-driven-development` to build the ticket;
   - merges the integration branch tip into its own branch before reporting done.

5. Once an **implementer subagent** completes, merge its work to the integration branch with a **merger subagent**.

6. If this changes the **frontier** of available tickets, kick off more **implementer subagents** to work on the new tickets. This allows for maximum concurrency.

7. Once all tickets are complete, call the Skill tool with `code-review` on the integration branch. Fix all issues raised by the code review in a single **implementer subagent**.

8. If a draft request exists, mark it ready for review. Otherwise, resolve each ticket the way the issue tracker closes work, and report the integration branch.

9. Clean up all **implementer subagent** worktrees.
