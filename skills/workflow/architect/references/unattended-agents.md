# Unattended agents

Adapted from the `software-factory` skill in [mattpocock/skills](https://github.com/mattpocock/skills) at `5863806` (MIT).

Read this when the system runs coding agents without a person at the keyboard, started by tickets, pull requests, or a clock, and the architecture must decide how. Call such a system a **factory**: agents turn tickets, pull requests, and schedules into merged code on infrastructure the user chooses.

## Terms

Use these words in the architecture document and the interview, so every question about a factory means one thing.

- **Task**: a kind of work the factory does, defined once and run many times (review, explore, implement, ratchet). A task works on a ticket, a pull request, or the whole codebase. A CI vendor's "workflow" and "job" are where a task is wired up, not the task.
- **Trigger**: the event that starts a run: a change in the ticket tracker or git host, a clock in the orchestrator, or another run.
- **Run**: one execution of a task on one runner, from trigger to finish, treated as a black box. A run never waits for a person. It ends, and the person's later change to the ticket tracker or git host triggers a new run.
- **Runner**: the disposable machine a run executes on. Nothing on it survives the run, even when the machine is long-lived. A run remembers earlier runs only through the ticket tracker, the git host, and the orchestrator.
- **Ticket tracker**: where tickets live and the factory's human interface. People schedule work by filing tickets and talk to agents in comments.
- **Ticket source**: anything outside the factory that files tickets: a feedback button, a monitor, an error tracker, an inbox.
- **Git host**: where branches, pull requests, and reviews live.
- **Orchestrator**: the component that receives triggers, starts runs on runners, and records which runs are queued, in flight, or finished.
- **Observability platform**: where runners send logs, traces, and status so a person can see what happened inside a run. Optional, and a run never decides on it until something writes its finding into the ticket tracker or git host.

## Shape of the design

A design has two halves: the **services** (ticket tracker, git host, orchestrator, runner, observability platform), each a slot filled with a product, and the **tasks** whose runs move work through them. One product can fill several slots. A design is finished when every slot names a product (the observability platform may be a deliberate none) and every task and ticket source has an answer to every question below.

Buy the services and build the tasks: the tasks carry the user's design, and the services are generic. Favor an off-the-shelf ticket tracker, since people already know it and outside users are easy to let in.

To choose a product for a slot, read [unattended-agents-services.md](unattended-agents-services.md).

Three designs, side by side:

| Service | All on GitHub | Linear tickets | Own tracker |
| --- | --- | --- | --- |
| Ticket tracker | GitHub Issues | Linear | own app |
| Ticket source | feedback button | feedback button, monitor | feedback button, monitor |
| Git host | GitHub | GitHub | GitHub |
| Orchestrator | GitHub Actions | own server and database | own app |
| Runner | Actions runner | Actions, E2B, Daytona, or a VPS | own app, or sandboxes |
| Observability platform | none (Actions run pages suffice) | an LLM tracing platform | own app |

## Start slow

Every trigger speeds the factory up, and a factory with no brakes produces unreviewed output faster than anyone can read it. Three brakes:

- **Automated checks**: deterministic gates (types, lint, tests) that every run passes.
- **Automated review**: a separate run that reads the diff cold against the codebase's standards and the ticket, when there is one.
- **Human review**: a person reads the pull request before it merges. What they catch becomes new automated checks and sharper automated review.

Add one automated trigger at a time, throttled at first (one bug report in ten, a clock once a day), with human review on every pull request. Open the throttle as the brakes earn trust. Cap every loop of runs at a few tries before a person steps in.

## Questions for every task

1. What triggers it?
2. What does it do, and which services does it read and write?
3. What does it trigger next?
4. Where does a person re-enter?
5. What stops two runs doing the same work?

For each ticket source: what stops it filing the same ticket twice?

## Example tasks

Start from the user's problem, not the factory. Each task below names the problem it solves, and most factories begin as one and grow by chaining the next.

| Problem | Task | Trigger | Does | Triggers next |
| --- | --- | --- | --- | --- |
| Untriaged tickets pile up | Explore | a ticket is created or labeled | checks the ticket's claims against the code, reproducing them where it can; sorts it (easy call, needs a person, not a bug); leaves findings on the ticket; never pushes | implement for easy calls; otherwise the ticket is labeled as waiting for a person |
| Ready tickets wait | Implement | a ticket is labeled ready | builds until the automated checks pass; opens a draft pull request | automated review |
| Pull requests wait for review | Automated review | a pull request opens with no automated review yet, or a person labels it | reviews the diff against the standards and the ticket | rework on a fail; on a pass it ends and the pull request waits for a person |
| Failed reviews sit unfixed | Rework | an automated review fails | fixes only what the review named, and pushes | automated review; after a set number of fails, the pull request is labeled as waiting for a person |
| Specs are too big for one run | Decompose | a spec ticket is labeled | splits it into tickets that record their dependencies | implement, which picks the next ticket whose dependencies are closed and triggers itself until none is left |
| A stricter check is being adopted | Ratchet | a daily clock | takes one file off the exception list, fixes it until the stricter check passes, opens a pull request | automated review; the migration ends when the list is empty |
| The factory's own runs fail | Fix | the orchestrator reports a failed run | files the failing log as a ticket and attempts a fix when it is fixable | automated review; a failure in a fix run triggers nothing, and the fix always gets human review because it changes the factory |
| The codebase drifts | Architecture | a nightly clock | scans recent changes for refactoring candidates and files one ticket | nothing; a person picks a candidate and labels it |
| The same mistakes recur | Retro | a pull request merges, throttled to one in ten | reads the pull request, its ticket, reviews, and run logs; proposes changes to the factory's instructions as a pull request | automated review |

Two problems are solved by ticket sources instead of tasks. A feedback button files each report with the explore label already on it. A monitor (slow queries, error rates) files one ticket per problem, comments on the open ticket when it sees the same problem again, and reopens it after a fix merges if the problem persists.
