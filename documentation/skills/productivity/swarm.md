Fork-added skill: it has no upstream equivalent.

## What it does

`swarm` divides one task into independent pieces and runs them in parallel on fast, low-cost subagents that you select, then merges their reports and spot-checks them. The pieces can be different tasks, and they can read or edit: a sweep across many files, a batch of unrelated small fixes, bulk summaries, an audit.

Its defining constraint is that nothing depends on anything else. There is no task graph, no branch, no worktree, and no review phase. A piece that edits owns a set of files, and no file has two owners. A piece that needs another piece's result waits for a second wave, a fresh swarm that starts from the first one's reports.

## When to reach for it

Type `/swarm`, or ask an agent to fan work out across many cheap agents. The agent proposes the pieces and a suggested agent for each, usually the Light tier. You pick the agents and may amend the pieces before anything runs. If your request already names the agents or the model, read-only pieces start at once, and edit pieces still wait for a yes on the piece list.

[divide-and-conquer](../workflow/divide-and-conquer.md) is the heavier alternative. It builds an authorized task graph with blocking dependencies, one worktree per task, an integration branch, and one review. Use it when tasks depend on each other or need merging. Use `swarm` when the pieces are independent and the cost of that machinery would exceed the work.

## How a run goes

| Step | What happens |
| --- | --- |
| Split | The agent cuts the task into independent pieces and gives each editing piece its own files. A piece that costs more to brief than to do stays in your session. |
| Choose the crew | The agent shows a table of pieces, suggested agents and the worker count. You select the agents. |
| Brief and dispatch | Each worker gets a self-contained brief and a fixed report shape. It runs in the background and may not spawn agents. |
| Merge | The agent combines the reports without redoing the work. If a piece fails, you decide what happens to it. |
| Verify | After edits, the agent compares changed files with each piece's owned files and runs the project's checks once. For read-only work, it checks at least one claim per report against its source. |
| Report | The agent states the merged result, what is verified, and the agent and model behind each piece. |

## Common questions

**Which models does it use?**
The ones your delegation tool offers, starting from the Light tier and moving to Balanced only for pieces that need judgment. You make the final pick. When the delegation and model routing rule from [setup-delegation-policy](../getting-started/setup-delegation-policy.md) is installed, it governs the tiers.

**What happens when a worker fails?**
The skill never escalates on its own, since that would spend more than you approved. It reports the failure and asks: rerun on a stronger agent, redo it in your session, or drop it.

**Can two workers edit the same file?**
No. Each file has one owner. A file two pieces need goes to one of them or to a later wave, and a worker that needs a file it does not own stops and says so.

**How much does it cost?**
Every worker reloads its own context, so cost grows with the number of pieces. The proposal shows the count before dispatch, and the agent quotes measured costs only.

**Does it review the code?**
It checks that edits stayed within their owners and runs the project's checks once. A full review of a branch is outside its scope.

## It's working if

- You chose the agents before any worker started, or you had named them yourself.
- Each worker's report has a status, evidence for each claim, and what it could not do.
- The final report labels every result verified or unverified and names the agent behind each piece.
- No file was edited by two workers.

## Where it fits

A standalone discipline you can reach for at any point in a session, not a step of the delivery flow. [divide-and-conquer](../workflow/divide-and-conquer.md) covers dependent implementation work.
