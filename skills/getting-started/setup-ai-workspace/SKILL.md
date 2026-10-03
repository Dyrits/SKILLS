---
name: setup-ai-workspace
description: "Configure a repository for AI-assisted work: task tracking, ticket-writing conventions, triage roles, domain documentation, and the optional getting-started setups (tooling, commit hooks, Git guardrails, automatic handoff, delegation policy)."
disable-model-invocation: true
---

# Setup AI workspace

Configure the repository contracts that `specify`, `taskify`, `triage`, and `graphify` consume. Explore, recommend, confirm, then write inspectable configuration. This skill configures the project, not the installed skills.

Call the Skill tool with "document" before choosing document locations or writing configuration; its terms (authorized, obligation, lazy, pointer) and rules apply throughout. Generated templates point to that contract instead of copying it.

Four decisions belong here:

- The task tracker, local Markdown or a remote service.
- The ticket-writing convention, the built-in `taskify` format or an established project template or skill.
- The strings used for the two category and four intake-state roles.
- The domain documentation layout and consumer rules.

## 1. Explore

Read existing configuration and conventions before proposing changes:

- `git remote -v` and `.git/config`, to identify the host without assuming it is the tracker.
- Root `AGENTS.md` and `CLAUDE.md`, including any `## Agent skills` section.
- `documentation/agents/` and any verified tooling record.
- Root `CHANGELOG.md`, `documentation/requirements.md`, `documentation/backlog.md`, `documentation/work-in-progress.md`, and relevant feature documentation.
- Task templates, contribution documentation, and available ticket-writing skills.
- `GLOSSARY.md`, `GLOSSARY-MAP.md`, `GUIDELINES.md`, and relevant architecture decision records.
- Monorepo signals such as workspace configuration or independent packages.
- Whether `triage` is installed, which determines whether role configuration is needed.
- Which optional setups in section 4 are already present.

## 2. Present findings and ask

Summarize what already exists. Take the following sections in order, one question at a time, recommending an answer the user can accept briefly.

### A. Task tracker

Ask where tasks live. Recommend GitHub for a GitHub remote, GitLab for a GitLab remote, or local Markdown without a remote. A different tracker is an ordinary override.

- Local Markdown uses `documentation/<feature>/tasks/<task>.md` for task bodies.
- A remote tracker uses its native task records. Local task files, when useful, contain a title and link to the authoritative published task rather than a copied body.

Record the authoritative backlog location with the tracker choice. A local project uses `documentation/backlog.md`; a remote project uses the verified backlog or board URL and keeps only a local link in that file. Working state remains local for either tracker, with execution and resumption details rather than duplicated remote status. Preserve prior backlog history unless a migration is explicitly authorized.

Record the choice in `documentation/agents/issue-tracker.md`. Preserve this established configuration filename and literal CLI/API `issue` terminology.

For Jira or another tracker, inspect available connectors, command-line tools, and documented API workflows first. After the user provides the project identity, verify access with the smallest read-only operation. Record the verified method. If no access exists, mark it manual and prepare local Markdown without claiming to read or update the service.

Resolve the backlog URL from verified project information where possible; ask for the intended board or backlog when it cannot be determined. If tracker access is manual, record that limitation rather than inventing a URL or claiming live access. The GitHub and GitLab templates default external PR/MR intake off. Leave that flag off unless the user asks to change it.

### B. Ticket-writing convention

Ask whether to use the discovered convention. If none exists, recommend the built-in `taskify` format and ask whether the project has another template, installed skill, or short description.

Record:

- **Source:** Built-in `taskify`, a repository-relative document path, or a skill name and its durable template reference.
- **Applies to:** Local task bodies, published tasks, or both.
- **Rules:** Language and required metadata needed to interpret the source.

Keep the full template at its source. An external ticket-writing skill contributes structure and quality rules, not its creation workflow or publication authority. `taskify` still owns tracer-bullet decomposition, blocking edges, acceptance criteria, and publication approval.

### C. Triage roles

Skip this section when `triage` is not installed. Otherwise ask whether to retain the default role strings:

- Category roles: `bug`, `enhancement`.
- State roles: `to-evaluate`, `on-hold`, `ready`, `not-planned`.

Only collect overrides if the user declines. The strings are configurable; the role set stays fixed because downstream skills consume it.

### D. Domain documentation

Default to one root `GLOSSARY.md` and `documentation/architecture-decision-record/` without asking. Offer a root `GLOSSARY-MAP.md` with per-context glossaries only when monorepo signals justify it.

If `GUIDELINES.md` exists, record `Guidelines: present`. Otherwise ask whether to create it through an interview, recommending yes when there is no standards document. On acceptance, call the Skill tool with "model-domain". On refusal, record `Guidelines: declined`.

## 3. Confirm and write

Show the proposed agent-instruction block and configuration contents before writing. Let the user adjust them.

Edit `CLAUDE.md` if it exists; otherwise edit `AGENTS.md` if it exists. If neither exists, ask which to create. Update an existing `## Agent skills` block in place and preserve surrounding user instructions.

```markdown
## Agent skills

### Task tracker

<one-line tracker summary; repository specifications are authoritative and remote publication is explicit>. See `documentation/agents/issue-tracker.md`.

### Triage roles

<one-line role-vocabulary summary>. See `documentation/agents/triage-roles.md`.

### Domain documentation

<single-context or multi-context summary>. See `documentation/agents/domain.md`.

### Project documents

Call the Skill tool with "document" before creating or updating project documents, to apply the shared authority, requirements, publication, resumption, and changelog rules.
```

Omit the triage block and file when triage is not installed.

Seed `documentation/agents/issue-tracker.md` from the selected template:

- [issue-tracker-local.md](issue-tracker-local.md)
- [issue-tracker-github.md](issue-tracker-github.md)
- [issue-tracker-gitlab.md](issue-tracker-gitlab.md)
- [issue-tracker-jira.md](issue-tracker-jira.md)

For another tracker, use the same sections with the user's verified access and conventions. Append [refinement.md](refinement.md), which delegates the shared document contract instead of installing a separate drafting tree.

Write [domain.md](domain.md), and [triage-roles.md](triage-roles.md) when applicable. Create only configuration needed now, not empty feature trees or speculative documents.

## 4. Optional setup

Offer the other getting-started setups together, once, as one multi-select question. Mark each as already present or missing from the exploration, and preselect any the request already named:

| Setup | Present when | Run by |
| --- | --- | --- |
| Development tooling | A verified tooling record exists | Skill tool, "setup-ai-tooling" |
| Commit hooks | `git config core.hooksPath` points at a committed hooks directory | Skill tool, "setup-git-hooks" |
| Git guardrails | A `block-dangerous-git.sh` hook is registered for the client | Skill tool, "setup-git-guardrails" |
| Automatic handoff | `.claude/settings.json` has a `PreCompact` hook gating on `.agents/handoffs/` | Skill tool, "setup-auto-handoff" |
| Delegation policy | The global steering files contain `## Delegation and model routing` | The human, `/setup-delegation-policy` |

Run the selected setups in table order, each to completion before the next, each owning its own questions, scope, and verification. Pass `setup-ai-tooling` the project, verified tracker access, known clients, and approved project/global scope. `setup-delegation-policy` is user-invoked and machine-wide: tell the user to run it rather than calling it.

When a selected skill is unavailable, finish the rest and tell the human how to install or run it later. Completion requires, for each selected setup, its verified result, a stated gap, or the user's decision to skip it.

## 5. Done

Report the files written, the setups run or skipped, and the workflow skills that consume them. The user can edit `documentation/agents/*.md` directly later. Confirm that future work uses the shared document tree, existing history remains in place, and installed skill files were not changed.
