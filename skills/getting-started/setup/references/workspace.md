# Workspace

Configure the repository contracts that planning and intake workflows read: the task tracker, the ticket-writing convention, and the triage roles. Explore, recommend, confirm, then write inspectable configuration. This area configures the project, not the installed skills.

The project documents and their rules are in [project-documents.md](project-documents.md); read it before choosing document locations or writing configuration. Its terms (authorized, obligation, lazy, pointer) apply throughout.

Four decisions belong to this area:

- The task tracker, local Markdown or a remote service.
- The ticket-writing convention, the built-in `taskify` format or an established project template or skill.
- The strings used for the two category and four intake-state roles.
- Whether the domain needs several contexts.

## 1. Explore

The inspection already gave the remotes, the `AGENTS.md` pointers, and the setup records. Read, in addition:

- Root `AGENTS.md`, including any `## Agent skills` section, and the existing `.agents/issue-tracker.md` and `.agents/triage-roles.md`.
- The project documents `AGENTS.md` names, as [project-documents.md](project-documents.md) describes: the requirements, backlog, working state, changelog, outline, glossary, conventions, relevant decision records, and relevant capability documents.
- Task templates, contribution documentation, and available ticket-writing skills.
- Monorepo signals such as workspace configuration or independent packages.
- Whether `triage` is installed, which determines whether role configuration is needed.

## 2. Ask

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

A single-context repository needs nothing now: its glossary and decision records are created when the first term or decision is settled. When monorepo signals suggest several domain contexts, ask whether the domain has several. On yes, each context keeps its glossary and decision records in a `documentation/` folder beside its code, and the system outline lists the contexts and links each glossary; create those when the first term is settled, not now, and say so in the report.

If the conventions file is missing, say so in the report; writing conventions is separate work.

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

Write the block following [agent-instructions.md](agent-instructions.md), and show the user every line added to `AGENTS.md`. Lines for the project documents are added by whichever skill creates each one, not here.

Seed `.agents/issue-tracker.md` from the selected template:

- [issue-tracker-local.md](../assets/issue-tracker-local.md)
- [issue-tracker-github.md](../assets/issue-tracker-github.md)
- [issue-tracker-gitlab.md](../assets/issue-tracker-gitlab.md)
- [issue-tracker-jira.md](../assets/issue-tracker-jira.md)

For another tracker, use the same sections with the user's verified access and conventions. Append [refinement.md](../assets/refinement.md), which says where the project documents live and when remote writes need authorization.

Write [triage-roles.md](../assets/triage-roles.md) when applicable. Create only configuration needed now, not empty capability trees or speculative documents.

## 4. Done

Completion: the files are written and shown to the user. For the report: the files written, what each configures, and any gap found during exploration, such as a missing conventions file. The user can edit `.agents/*.md` directly later. Existing history remains in place, and installed skill files are not changed.
