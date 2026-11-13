# Services for unattended agents

Adapted from the surveys in the `software-factory` skill of [mattpocock/skills](https://github.com/mattpocock/skills) at `5863806` (MIT), written there in 2026-10.

Read this when a design from [unattended-agents.md](unattended-agents.md) must choose a product for a slot. The types and questions below change slowly. Product names, prices, limits, preview status, and plan gating change fast, so use the product names only to get oriented, then research the current options in primary sources: the API and webhook reference, the limits or quotas page, the pricing page, the security or networking docs, and the changelog. Mark any claim about a vendor with the date you checked it.

## Ticket tracker

The human interface of the factory. Pick a type by who files and schedules work.

| Type | Pick it when | Examples |
| --- | --- | --- |
| Git-host tracker | the team is small, already lives on the git host, or the repository is public. The host's CI is the orchestrator with no glue, and labels are the dependable router. | GitHub Issues, GitLab Issues, Forgejo |
| Agent-native development tracker | product, support, or design staff schedule work, or the team wants polished triage views. Statuses are first-class, so "moved to Ready" is a clean trigger, and agents appear as assignable users. | Linear, Jira, Shortcut, YouTrack |
| Open-source development tracker | data must stay in-house, or the user wants to read and patch the tracker's source. | Plane, Huly, OpenProject |
| General work tool | a non-engineering team already lives there, or tickets are mostly content, ops, or research. Forms are the strength, and every factory invents its own schema. | Notion, Asana, ClickUp, Trello |
| Repository-native tracker | one developer drives agents locally and wants the plan in git. A push is the only trigger, and outside filing is a commit, so graduate to a git-host tracker once others file. | Beads, Backlog.md |
| Built from scratch | the tracker is the product itself, or no off-the-shelf model fits. Every trait below becomes code to maintain. | own app |

Questions that decide the slot:

- **Triggers**: which changes (created, labeled, status moved, assigned, commented, mentioned) emit a webhook the orchestrator can turn into a run, and how fast and how granular?
- **Routing**: which labels, statuses, or fields tell a run its kind?
- **Thread**: can a person answer an agent in comments, and does that reply trigger the next run?
- **Identity**: is there an API plus a bot identity, and does the bot cost a seat?
- **Native agents**: can a ticket be assigned to an agent, on which plan, metered how, and does it read the ticket at assignment or the whole thread?
- **Outside filing**: how does a customer or ticket source create tickets, and which plan unlocks it?
- **Hosting**: SaaS only, or self-hosted, and under which licence?

## Git host

- **All-in-one platform** (GitHub, GitLab): one product fills git host, ticket tracker, orchestrator, and runner, with the richest trigger catalogue. Pick it when the factory starts small or the user wants one bill and one login.
- **Suite git host** (Bitbucket with Jira, Azure DevOps, AWS CodeCommit): the tracker is a sibling product, so the orchestrator joins two event streams. Pick it when the organization already runs the suite.
- **Self-hosted git host** (Forgejo, Gitea, GitLab self-managed, GitHub Enterprise Server): pick it when code must stay on-premises or per-seat cost or API throttling matters. The user owns upgrades, backups, and uptime for every slot it fills.
- **Review-first or decentralized host** (Gerrit, Tangled): pick it when the team already reviews per patchset. Most factory tooling assumes pull requests, so expect to build more glue.
- **Agent-native host** and **git storage for runs**: early types built for high commit throughput or per-run scratch repositories. Pilot one on a mirror of a single repository and keep a full git host as the fallback.

Questions that decide the slot:

1. Which events (pull request opened, push, review submitted, label added, check finished) reach the orchestrator as webhooks, and are deliveries signed?
2. Can a run act as a dedicated bot identity? That keeps runs attributable, lets an automated review approve a pull request another identity authored, and decides whether a run's own pushes trigger the next run.
3. Are required checks, required approvals, and branch protection available on the user's plan and repository visibility, and can a bot sit on a bypass list?
4. What API budget do all runs share, per what unit (installation, token, user, workspace)?
5. Which other slots does the same product fill?

## Runner

Runner types differ in who owns the agent loop and who owns the machine. Choice is per run: a cheap CI runner for review and a microVM for implementation is a normal design.

| Type | Agent loop | Machine | Pick it when |
| --- | --- | --- | --- |
| CI runner | yours, inside the CI job | CI vendor's, or yours | the git host is GitHub or GitLab and every trigger is a git host event or a clock. The workflow file is the orchestrator and the run page is the observability platform. Hosted runners are disposable by construction. Self-hosted ones need an ephemeral mode (one pod per job). |
| MicroVM API | yours | provider's | the factory has its own orchestrator and wants many short parallel runs. Compare maximum run length, the concurrency cap, and whether time spent waiting on the model is billed. |
| Bundled agent platform | vendor's | vendor's | the user wants the fewest moving parts and accepts that vendor's agent. Confirm its triggers cover the user's ticket tracker. |
| Bring-your-own worker | vendor's | yours | the user wants a bundled agent but runs must reach a private network or keep data on the user's machines. Disposability is the user's job. |
| Own server or containers | yours | yours | runs are long, steady, or heavy, or a server already hosts the orchestrator. Use `docker run --rm` or a Kubernetes Job that deletes itself. |

Questions that decide the slot:

1. How does the orchestrator start a run (workflow trigger, SDK call, mention, HTTP call, queue claimed by a worker)?
2. What are the maximum run length and the concurrency cap, per plan, and what happens at the cap?
3. What is the cost shape (per minute, per second of CPU and memory, active CPU only, per run, per seat, flat), and are model tokens inside the price?
4. How is disposability achieved, and can the design restrict persistence features to caches?
5. What can a run reach (private network, outbound allowlist), and who else can read its secrets?
6. Which other slots does it fill?

## Orchestrator

No survey exists. The orchestrator is the CI engine of the git host in an all-on-one design, and the user's own server and queue otherwise. Decide it from the questions every task must answer in [unattended-agents.md](unattended-agents.md), above all what stops two runs doing the same work: a concurrency group in CI, or a lock keyed by ticket in an own server.

## Observability platform

Choose by what the person needs to see inside a run: its log, its agent trace (each model call and tool call as a span), or that trace joined to the rest of the system. When a run should act on what the platform sees, make the platform a ticket source: a monitor files the ticket, and a run reads it.

| Type | Pick it when |
| --- | --- |
| None (the runner or orchestrator page shows enough) | few runs a day and one person watching. Most factories start here and leave it when they need search across runs, a cost rollup per run, or longer retention. |
| LLM and agent tracing platform | people ask "why did the agent do that?" across many runs, or token spend needs a per-run rollup. Open-source options keep transcripts in-house. |
| General monitoring backend | the team already pays for one, or runs must join the application's own traces. |
| LLM gateway with request logging | the user wants per-run spend caps or one key vault, or the harness exports nothing itself. It sees model calls only, so tool calls stay invisible. |

Runners reach a platform through five hooks. Name the hook alongside the product.

- **Harness export**: the agent harness emits OpenTelemetry itself (Claude Code, the Claude Agent SDK, and Codex CLI each have settings for it; prompts and tool output are opt-in).
- **Platform push**: the model platform sends traces for you.
- **SDK wrapper**: one call in the runner's code.
- **Hook plugin**: a hook reads the session transcript at each stop and ships it.
- **Gateway**: the runner's model base URL points at a logging proxy.

Questions that decide the slot:

1. Does the runner or orchestrator already show enough? A yes means a deliberate none.
2. Which hook does the harness support, which does the product accept, and do tool calls arrive as spans?
3. Is it self-hostable, under which licence and tier?
4. What is the billing unit, and what is the cost per run, given one span per tool call?
5. How many days does each tier retain data, against how far back a person looks when a run fails?

## Gotchas to verify before relying on them

- **The built-in GitHub Actions token ends chains.** Events caused by the default `GITHUB_TOKEN` start no new workflow runs (except `workflow_dispatch` and `repository_dispatch`), so a run that labels or comments with it silently stops the next run. Give runs a GitHub App identity from the start.
- **Gates often sit behind a paid plan.** Rulesets on private repositories, approval rules, and enforced merge checks depend on plan tier on several hosts.
- **Rate limits are per identity**, and a bot's type changes them. A GitHub App installation had a higher hourly limit than `GITHUB_TOKEN` as of 2026-10.
- **Native agents may read the ticket only at assignment.** Put later context on the pull request.
- **Agent webhooks expect a fast acknowledgement.** The orchestrator acknowledges at once and starts the run afterward.
- **Work tools may batch webhooks** and deliver them a minute or two late. A factory that needs prompt runs triggers on property changes or picks another type.
- **Suite trackers mean two event streams** that the orchestrator joins itself.
