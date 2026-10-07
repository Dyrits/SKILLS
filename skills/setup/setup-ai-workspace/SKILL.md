---
name: setup-ai-workspace
description: "Configure a repository for AI-assisted work: task tracking, ticket conventions, triage roles, code conventions, optional tooling setups. Use when the user asks to set up or reconfigure the AI workspace."
metadata:
  forks: "mattpocock/skills/skills/engineering/setup-matt-pocock-skills"
---

# Setup AI workspace

Configure the repository contracts that `specify`, `taskify`, `triage`, and `graphify` consume. Explore, recommend, confirm, then write inspectable configuration. This skill configures the project, not the installed skills.

**Calls:** `codify`, `document`, `memorize`, `setup-ai-tooling`, `setup-delegation-policy`, `setup-git-guardrails`, `setup-git-hooks`.

Call the Skill tool with "document" before choosing document locations or writing configuration; its terms (authorized, obligation, lazy, pointer) and rules apply throughout. Generated templates point to that contract instead of copying it.

Four decisions belong here:

- The task tracker, local Markdown or a remote service.
- The ticket-writing convention, the built-in `taskify` format or an established project template or skill.
- The strings used for the two category and four intake-state roles.
- Whether the domain needs several contexts, and whether to create code conventions now.

## 1. Explore

Read existing configuration and conventions before proposing changes:

- `git remote -v` and `.git/config`, to identify the host without assuming it is the tracker.
- Root `AGENTS.md`, including any `## Agent skills` section.
- `.agents/` and any verified tooling record.
- The project documents: call the Skill tool with "document" for their layout, then read the requirements, backlog, working state, changelog, glossary or glossary map, conventions, relevant decision records, and relevant capability documents.
- Task templates, contribution documentation, and available ticket-writing skills.
- Monorepo signals such as workspace configuration or independent packages.
- Whether `triage` is installed, which determines whether role configuration is needed.
- Which optional setups in section 4 are already present.

## 2. Present findings and ask

Summarize what already exists. Take the following sections in order, one question at a time, recommending an answer the user can accept briefly.

### A. Task tracker

Ask where tasks live. Recommend GitHub for a GitHub remote, GitLab for a GitLab remote, or local Markdown without a remote. A different tracker is an ordinary override.

- Local Markdown keeps task bodies in the capability task files.
- A remote tracker uses its native task records. Local task files, when useful, contain a title and link to the authoritative published task rather than a copied body.

Record the authoritative backlog location with the tracker choice. A local project uses the backlog document; a remote project uses the verified backlog or board URL and keeps only a local link in the backlog document. Working state remains local for either tracker, with execution and resumption details rather than duplicated remote status. Preserve prior backlog history unless a migration is explicitly authorized.

Record the choice in `.agents/issue-tracker.md`. Preserve this established configuration filename and literal CLI/API `issue` terminology.

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

A single-context repository needs nothing now: its glossary and decision records are created when the first term or decision is settled. When monorepo signals suggest several domain contexts, offer a glossary map with per-context glossaries; on acceptance, call the Skill tool with "document" to create the map.

If the conventions file is missing, ask whether to create it through an interview, recommending yes when there is no standards document. On acceptance, call the Skill tool with "codify", with the **code** focus.

## 3. Confirm and write

Show the proposed agent-instruction block and configuration contents before writing. Let the user adjust them.

Edit `AGENTS.md`, creating it when it does not exist. Update an existing `## Agent skills` block in place and preserve surrounding user instructions.

```markdown
## Agent skills

### Task tracker

<one-line tracker summary; repository specifications are authoritative and remote publication is explicit>. See `.agents/issue-tracker.md`.

### Triage roles

<one-line role-vocabulary summary>. See `.agents/triage-roles.md`.
```

Omit the triage block and file when triage is not installed.

Then call the Skill tool twice, for "document" and "memorize", so each adds its own pointer to `AGENTS.md`, and show the user the lines they added.

Seed `.agents/issue-tracker.md` from the selected template:

- [issue-tracker-local.md](issue-tracker-local.md)
- [issue-tracker-github.md](issue-tracker-github.md)
- [issue-tracker-gitlab.md](issue-tracker-gitlab.md)
- [issue-tracker-jira.md](issue-tracker-jira.md)

For another tracker, use the same sections with the user's verified access and conventions. Append [refinement.md](refinement.md), which delegates the shared document contract instead of installing a separate drafting tree.

Write [triage-roles.md](triage-roles.md) when applicable. Create only configuration needed now, not empty capability trees or speculative documents.

## 4. Optional setup

Offer the other setups together, once, as one multi-select question. Mark each as already present or missing from the exploration, and preselect any the request already named:

| Setup | Present when | Skill |
| --- | --- | --- |
| Development tooling | A verified tooling record exists | `setup-ai-tooling` |
| Commit hooks | `git config core.hooksPath` points at a committed hooks directory | `setup-git-hooks` |
| Git guardrails | A `confirm-dangerous-git.sh` hook is registered for the client | `setup-git-guardrails` |
| Delegation policy | The global steering files contain `## Delegation and model routing` | `setup-delegation-policy` |

Run the selected setups in table order by calling the Skill tool with "setup-ai-tooling", "setup-git-hooks", "setup-git-guardrails", or "setup-delegation-policy", one call per setup, each to completion before the next, each owning its own questions, scope, and verification. Pass `setup-ai-tooling` the project, verified tracker access, known clients, and approved project/global scope. `setup-delegation-policy` is machine-wide: call it through the Skill tool only after the user agrees to it.

When a selected skill is unavailable, finish the rest and tell the human how to install or run it later. Completion requires, for each selected setup, its verified result, a stated gap, or the user's decision to skip it.

## 5. Done

Report the files written, the setups run or skipped, and the workflow skills that consume them. The user can edit `.agents/*.md` directly later. Confirm that future work uses the shared document tree, existing history remains in place, and installed skill files were not changed.
