## What it does

`setup-custom-skills` configures five conventions for one repository: the system-of-record issue tracker, whether refinement drafts stay local until publication, the ticket-writing convention, the triage-label vocabulary, and the domain documentation layout. It records the answers as markdown files under `documentation/agents/`.

Those files are the only thing that varies between repositories. The skills themselves are identical everywhere; they read `documentation/agents/issue-tracker.md` at run time and do what it says. That is why the set is not tied to GitHub, and why no skill file ever needs editing to point it somewhere else. Invoking it with "link the skills to a custom issue tracker" works with anything you can connect to programmatically, with zero changes to the skills.

It is a prompt-driven skill, not a deterministic script. It reads your `git remote`, your existing `CLAUDE.md`, your existing `CONTEXT.md`, proposes what it found, and waits for you to confirm before writing anything.

## When to reach for it

You invoke this by typing `/setup-custom-skills`; the agent won't reach for it on its own. It is deliberately marked non-invokable, so no other skill can fire it for you.

Reach for it once per repository, before the first use of any other engineering skill. If [triage](../upkeep/triage.md), [to-specifications](../workflow/to-specifications.md), [to-tickets](../workflow/to-tickets.md) or [wayfinder](../shaping/wayfinder.md) start guessing where your issues go, or apply labels your tracker doesn't have, they have not been set up here yet. A repository already halfway through a project is a fine place to run it; the skill reads what is already there and no earlier work is wasted.

## Prerequisites

It writes into the repository you run it in:

| It writes | Where |
| --- | --- |
| `issue-tracker.md` | `documentation/agents/` |
| `domain.md` | `documentation/agents/` |
| `triage-labels.md` | `documentation/agents/`, only when the `triage` skill is installed |
| An `## Agent skills` block | whichever of `CLAUDE.md` / `AGENTS.md` already exists |

All of it is committed markdown. There is no user-level or global mode: the config lives in the repository, so every repository gets its own copy.

## The five decisions

It leads each section with the recommended answer, and skips whatever exploration already settled. Most runs are two confirmations and done.

| Decision | What it proposes | When it actually asks |
| --- | --- | --- |
| **Issue tracker** | the one matching your `git remote` | always: this is the one real choice |
| **Local drafts** | keep refinement under `.refinement/<issue-key>/` until an explicit publish step | for every tracker, including local markdown |
| **Ticket writing** | use an existing issue template or ticket skill when one is found, with the built-in format as fallback | always, after it inspects the repository and available skills |
| **Triage labels** | keep the five canonical names (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`) | only if the `triage` skill is installed |
| **Domain documentation** | single-context: one `CONTEXT.md` plus `documentation/architecture-decision-record/` at the root | only if it spots monorepo signals, and then it offers a multi-context `CONTEXT-MAP.md` |

The tracker options:

| Option | Where issues live | Needs |
| --- | --- | --- |
| **GitHub** | the repository's GitHub Issues | the `gh` CLI |
| **GitLab** | the repository's GitLab Issues | the `glab` CLI |
| **Jira** | the configured Jira project | a verified Jira MCP connector, CLI, REST workflow, or manual publication |
| **Local markdown** | files under `backlog/<feature>/` in this repository | nothing: no remote at all |
| **Other** | wherever you say | one paragraph from you describing the workflow |

GitHub, GitLab, Jira, and local markdown ship as templates. The local tracker keeps its published records in committed `backlog/` files. Any tracker can have a separate `.refinement/` workspace for working material; choosing local markdown does not publish every local document.

For Jira, setup records the project key and verifies the smallest available read operation before describing access as automated. A Jira MCP connector is one supported access method, but it is not implied or installed by choosing Jira. Without verified access, the configuration uses manual publication and the agent prepares exact Markdown for the user to paste.

## Ticket writing conventions

Setup looks for repository issue templates, contribution guidance, and installed ticket-writing skills. It recommends what it finds, but adopting that convention is a choice. The resulting `documentation/agents/issue-tracker.md` points to the source instead of copying it, so a team template remains the single source of truth.

For example, a Jira team can select `create-jira-ticket` and its template reference. `to-tickets` then uses the skill's French ticket structure and quality rules while retaining its own tracer-bullet breakdown, blocking edges, review step, and explicit publication boundary. The built-in template remains available for any run.

## Draft before publish

For every tracker, setup asks whether working material should stay in `.refinement/` until an explicit publish step. The recommended answer is yes. A sourced draft lives at `.refinement/<issue-key>/specification.md`, carries the issue key and URL or local ticket path, and may have draft implementation tickets under `.refinement/<issue-key>/issues/`.

The tracker remains the system of record. Reading it does not cross the publication boundary; creating or updating its records does, including files under `backlog/`. `to-specifications` and `to-tickets` save drafts by default when refinement is configured. Explicit publication promotes selected artifacts and links to the authoritative record, while supporting notes stay in refinement.

"Other" is not a stub either. It is the reason Linear, Azure DevOps and Beads work: you describe the workflow, the skill records your prose in `documentation/agents/issue-tracker.md`, and the downstream skills follow the prose. Jira now has its own template, including MCP, CLI, REST, and manual access modes.

## Common questions

**Does an issue link make a playtest note part of the backlog?**

No. Interviews, exploratory catalogues, and working playtest notes belong in `.refinement/`; published issues and specifications belong in the tracker. Keep supporting material needed to understand a published issue in version control.

**Do I have to use GitHub?**

No. GitHub, GitLab and local markdown under `backlog/` all ship as ready-made templates, and anything else works through the "other" path. This is the most-repeated question in the record, in roughly these words: *"hard locked to github"*, *"can I use GitLab / Jira"*, *"what about Azure DevOps"*. The answer every time is that the tracker is a setup answer, not a skill property.

**Do I need to re-run it after updating the skills?**

Asked directly after v1.1, Matt said yes. The skill's own closing message is softer: it tells you re-running is only needed to switch trackers or start over. Both are defensible and the reason for the gap is real: the seed templates change between versions, so a `documentation/agents/issue-tracker.md` written by an older release can go stale against the skills now reading it. If a downstream skill starts doing something the documentation describes differently, re-running is the cheap fix.

**It wrote to `CLAUDE.md`, but I'm on Codex.**

Known gap, still open. The file-selection rule is "edit `CLAUDE.md` if it exists, else `AGENTS.md`": it checks which file exists, not which harness is running. A repository with a `CLAUDE.md` left over from Claude Code will get its `## Agent skills` block somewhere Codex never reads. Two workarounds are in circulation: move the block to `AGENTS.md` by hand, or keep `AGENTS.md` canonical and make `CLAUDE.md` a one-line pointer at it. If neither file exists, the skill asks you which to create rather than picking, which has confused people who expected it to just decide.

**It didn't create my triage labels.**

It doesn't. `documentation/agents/triage-labels.md` is a *mapping*: it tells `/triage` which strings in your tracker correspond to the five canonical roles. It does not run `gh label create`. On a fresh GitHub repository the labels genuinely do not exist yet, and this has been filed as a bug more than once. Two follow-ons:

- If your tracker already uses the canonical names, the mapping is an identity table and there is nothing to configure. That is the intended common case, not a missing step.
- [wayfinder](../shaping/wayfinder.md)'s `wayfinder:map` and `wayfinder:<type>` labels are not created here either, and `gh issue create --label <missing>` fails outright rather than creating the label. Create them by hand before the first wayfinder run on a GitHub repository.

**Can I configure the other skills' behaviour here (grilling cadence, question format, tone)?**

Only ticket-writing conventions belong here because they are part of the tracker contract consumed by `to-tickets`. Broader preferences such as grilling cadence and conversational tone belong in your `CLAUDE.md` or `AGENTS.md` as plain instructions, which every skill already reads.

**Can I keep the config in `~/.claude` instead of committing it to every repository?**

Not today. There is an open request for exactly this from someone running the skills across many repositories, and no user-level mode exists. Every repository carries its own `documentation/agents/`.

**Isn't it strange to have a skill that configures the other skills?**

One long-standing complaint says yes, in these words: *"having a skill to set up the other skill does not feel right to me: that means the LLM is configuring its own skills."* The trade is real and acknowledged: the alternative to a setup step is duplicating tracker instructions into every skill that touches issues. The output is inspectable, editable markdown, which is the mitigation: you can read every file it wrote and change it by hand, and day-to-day tweaks are exactly that, not another run.

## It's working if

- `documentation/agents/issue-tracker.md` and `documentation/agents/domain.md` exist, plus `triage-labels.md` if `triage` is installed.
- An `## Agent skills` section appears in the instruction file your harness actually reads, with a one-line summary pointing at each of those files.
- The tracker it proposed matches the remote you really use, and the label strings match labels that really exist in your tracker.
- `documentation/agents/issue-tracker.md` names the ticket template or skill the team chose, with the built-in `to-tickets` format available as fallback.
- Afterwards, `/to-specifications` and `/to-tickets` know whether to keep drafts local or publish them, and `/triage` applies labels rather than inventing them.
- Nothing in the skill files themselves changed. If setup edited a `SKILL.md`, something went wrong.

## Where it fits

`setup-custom-skills` is the **run-once setup** for the engineering flow, the precondition everything else assumes rather than a step in the chain. Its neighbours are its readers: [triage](../upkeep/triage.md), which applies the label vocabulary written here; [to-specifications](../workflow/to-specifications.md) and [to-tickets](../workflow/to-tickets.md), which save drafts or publish according to the boundary written here; and [wayfinder](../shaping/wayfinder.md), which reads the "Wayfinding operations" section of the same tracker file to know how maps and child tickets are stored. The domain documentation layout it records is the one [domain-modeling](../reference/domain-modeling.md) fills in later: it creates `CONTEXT.md` and architecture decision records lazily, when a term or decision actually gets resolved, so an empty repository after setup is the expected state. For which skill to reach for next, [what-is-next](./what-is-next.md) routes the whole set.
