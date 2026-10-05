Upstream source: `retro`, verified in the `24fe0ef` tree. This fork first renamed `retro` to `improve-agent-environment`, then narrowed that skill into [improve-skills](./improve-skills.md); `improve-environment` restores upstream's environment retrospective as its own skill, with the confirmation and completion steps `improve-skills` added.

## What it does

`improve-environment` looks back over a session, finds each moment of friction (a long search, a mistake, a retry, an expensive tool call, missing information), and changes the project's **environment** so the next run avoids it. The environment is everything around the code that shapes how an agent works: checks, hooks, CI, steering files, `CONVENTIONS.md`, tools, and access.

It changes the environment, not the code. The bug the agent shipped stays a bug for [debug](./debug.md); this skill asks what about the repository let it happen, and proposes the check, pointer, or rule that stops it next time. Nothing changes until you accept a candidate.

## When to reach for it

Type `/improve-environment`, or an agent or another skill can reach for it when the task fits: when you ask what would have prevented a mistake, why a session was harder than it should have been, or for an environment retrospective. It edits project files only for candidates you accept.

| Situation | Action |
| --- | --- |
| The agent searched too long, made a mistake a tool could catch, or lacked information | Run `/improve-environment` |
| A bug is fixed and you want to know what would have prevented it | Run `/improve-environment` in the same session |
| A skill fired wrongly, never fired, or misled the agent | Use [improve-skills](./improve-skills.md) instead |
| You want to record a convention or command during the session | [memorize](../reference/memorize.md) files it directly |
| The code's structure needs deepening | Use [improve-codebase-architecture](./improve-codebase-architecture.md) instead |

## Where the findings land

| What went wrong in the session | Fix it with |
| --- | --- |
| A long search for a file or fact | A navigation pointer from a file the agent already reads |
| A mistake a tool could have caught | A check: lint rule, type, test, pre-commit hook, or CI job, wiring an existing one first |
| Review missed a judgement-call mistake | A rule in `CONVENTIONS.md`, which [review-and-refactor](../workflow/review-and-refactor.md) reads |
| A large `AGENTS.md` or `CLAUDE.md` | Steering moved out into checks or `CONVENTIONS.md` |
| Steering lines that change nothing | Deleted as no-ops |
| A tool call expensive for what it returned | A streamlined or replaced tool |
| Information the agent could not reach | Wider access, such as a teed dev server log or read-only service access |

Two ideas decide the placement. Standards belong to the **reviewer**, which receives only a diff, not to the implementer, which carries the most context pressure. And a **mechanical** violation (a banned API, an import shape, a file location) gets a check that can fail, while only a genuine judgement call becomes prose. A repository with no guardrail at all is reported as a finding in its own right.

## Common questions

**Does it apply changes on its own?**

No. It presents the candidates in order of severity and applies only the ones you accept. A new check is run against the current code before it can block anything, and against the session's mistake when that can be reproduced.

**Won't it invent generic advice to fill its categories?**

That is the main criticism upstream's `retro` received: once a job is done, the agent forgets the middle of the session and fills the categories with best practice. Here every candidate must point to a moment of friction in the session, and every moment must end with a candidate, a skill finding, or a reason the environment could not have prevented it. Discard any candidate you cannot trace.

**Should I just add a line to `CLAUDE.md`?**

Usually not. A line there loads into every session and drifts as the code changes. A mechanical mistake gets a check; a judgement call goes to `CONVENTIONS.md` for the reviewer. `AGENTS.md` and `CLAUDE.md` are mostly for navigation pointers.

**Does it remove rules too?**

It deletes steering lines that change nothing and moves oversized steering out of `AGENTS.md`. It sees one session, so it cannot tell that a lint rule from last month has gone noisy; pruning checks stays your call.

**How does it divide work with `improve-skills` and `memorize`?**

Friction a skill caused goes to [improve-skills](./improve-skills.md), which reports it on this repository; each skill hands the other its findings. Written lessons (a pointer, a `CONVENTIONS.md` rule, a convention) are filed through [memorize](../reference/memorize.md), which owns where they live. `improve-environment` itself builds checks and changes tools and access.

**What if a skill it calls is not installed?**

It names the missing skill with its install command, carries out that step from its stated intent, and tells you the step ran without it. The skills involved are listed at the top of its [`SKILL.md`](../../../skills/upkeep/improve-environment/SKILL.md).

## It's working if

- Every candidate points to a specific moment in the session, not a generic best practice.
- Repeat mistakes turn into failing checks, and `AGENTS.md` gets shorter over time.
- An existing check that sat unwired shows up as the finding, rather than a proposal to build a new one.
- The next session on the same kind of task finds its way faster.

## Where it fits

`improve-environment` is periodic maintenance after a session in either development workflow, most useful after one that felt harder than it should have. Run it before clearing the session, or point a new session at the log. It follows [debug](./debug.md) when you want to know what would have prevented the bug, sits beside [improve-skills](./improve-skills.md) for problems in the skills themselves, and hands a repository with no guardrail to [setup-git-hooks](../setup/setup-git-hooks.md). [guide](../productivity/guide.md) maps the whole set.
