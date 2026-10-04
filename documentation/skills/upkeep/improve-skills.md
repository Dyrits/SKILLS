Upstream source: `retro`, verified in the `d81f3a1` tree. This fork first renamed it `improve-agent-environment`, then renamed it `improve-skills` and changed its target: it now reports on the skills themselves instead of recommending changes to the project's environment.

## What it does

`improve-skills` holds a retrospective on a session with you, then opens an issue on [Dyrits/SKILLS](https://github.com/Dyrits/SKILLS) describing how the skills behaved. Together you establish four things: what went right, what went wrong, whether the skills were used correctly or used at all, and whether the outcome is the one you expected.

Its defining constraint is that the agent's reading of the session is only a starting point. Every finding is put to you, confirmed or corrected, and kept apart from suspected causes before anything is written. Nothing is published until you approve the exact issue text.

## When to reach for it

Type `/improve-skills`, or an agent or another skill can reach for it when the task fits. Run it after a session, optionally naming the session to review and what you expected from it.

| Situation | Action |
| --- | --- |
| A skill fired when it should not have, or never fired | Run `/improve-skills` |
| The agent followed a skill but the outcome missed what you wanted | Run `/improve-skills` |
| A session went well and you want to record what to keep | Run `/improve-skills` |
| The agent keeps missing a convention of your own project | [memorize](../reference/memorize.md) files it in the project; you can also just tell the agent |
| Code architecture or module seams need review | Use [improve-codebase-architecture](./improve-codebase-architecture.md) instead |
| A specific defect needs root-cause diagnosis | Use [debug](./debug.md) instead |

## Where each finding goes

| Finding | Home |
| --- | --- |
| A skill problem: a wrong or missing trigger, an unclear or missing step, conflicting skills, a stale route in `guide`, a missing skill | The issue on the skills repository |
| A lesson about your project: a convention, a command, a review rule | Filed in the project through [memorize](../reference/memorize.md). A mechanical violation gets a proposed lint rule, hook, or CI job instead of a written rule. |
| Agent behavior no skill could have steered | Reported to you, left out of the issue |

What went right goes into the issue too, so a later fix does not break behavior worth keeping.

## Common questions

**What happened to `.agents/feedbacks/`?**

The [iterate](../workflow/iterate.md) workflow used to write correction records there, and nothing read them. Corrections to a project's own conventions now go straight to [memorize](../reference/memorize.md). The folder now holds only approved issues that could not be posted, which `improve-skills` offers to open on its next run with GitHub access.

**Will my project's details end up in a public issue?**

The repository is public, so the draft leaves out private paths, code, names, and secrets and describes your project generically. You see the exact text before it is posted.

**What if an issue already covers the problem?**

The agent checks open issues first and drafts a comment on the matching one instead of a duplicate.

**What if GitHub is not reachable from the session?**

It tries a connected GitHub server, then the `gh` command, then the GitHub API with a token already configured in the environment or stored by git's credential helper. Git alone cannot open an issue. When none of them works, the approved issue is saved in `.agents/feedbacks/`, in the skills checkout when the skill was loaded from one, and the next run that reaches GitHub offers to post it.

**What happened to `/improve-agent-environment`?**

It became `improve-skills`. Its narrower checks on your own project (steering files, missing guardrails, tool cost) now arrive through the project-lesson path above rather than as a ranked list of environment changes.

## It's working if

- Every finding in the issue points to a moment in the session and was confirmed by you.
- The issue names each skill involved, how it was reached, and whether it behaved as intended.
- Project lessons were filed locally and do not appear in the issue.
- The issue contains nothing that identifies your private project, and its URL is reported once posted, or you are told where its feedback record was saved.

## Where it fits

`improve-skills` is periodic maintenance after a session in either development workflow. Run it before clearing the session, or point a new session at the log. [memorize](../reference/memorize.md) handles corrections during the session; this skill handles what the skills themselves got wrong. Fixing a reported problem happens in a separate session on this repository, following [write-for-agents](../reference/write-for-agents.md). [guide](../getting-started/guide.md) maps the whole set.
