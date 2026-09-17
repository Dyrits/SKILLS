---
name: setup-custom-skills
description: "Configure this repository for the workflow skills: its issue tracker (local markdown or remote), ticket-writing convention, triage role vocabulary, and domain documentation layout. Run once before first use of the tracker-consuming skills."
disable-model-invocation: true
---

# Setup Custom Skills

Scaffold the per-repository configuration that the workflow skills assume. Four decisions:

- **Issue tracker**: the system of record for published issues, either local markdown under `backlog/` or a remote tracker (GitHub, GitLab, Jira, or one you describe)
- **Ticket writing convention**: the built-in `to-tickets` format, or an existing project template or ticket-writing skill
- **Triage roles**: the strings this repository uses for the two category and four state roles
- **Domain documentation**: where `CONTEXT.md` and architecture decision records live, and the consumer rules for reading them

**Refinement is not a decision.** Whatever tracker a repository picks, it drafts in `.refinement/` and publishes only when the user asks. A remote tracker with its own refinement or analysis status changes nothing here: local drafting comes first, publication pushes the result. [refinement.md](./refinement.md) holds those conventions and every generated tracker file carries them.

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

## Process

### 1. Explore

Look at the current repository to understand its starting state. Read whatever exists; don't assume:

- `git remote -v` and `.git/config`: is there a remote, and which host?
- `AGENTS.md` and `CLAUDE.md` at the repository root: does either exist? Is there already an `## Agent skills` section in either?
- `CONTEXT.md` and `CONTEXT-MAP.md` at the repository root
- `documentation/architecture-decision-record/` and any `src/*/documentation/architecture-decision-record/` directories
- `documentation/agents/`: does this skill's prior output already exist?
- `backlog/` and `.refinement/`: existing tracker records and refinement workspaces
- Issue templates, contribution documentation, and available ticket-writing skills: is there an established ticket structure, language, or required metadata?
- Is the `triage` skill installed? (a `triage` skill folder alongside this one, or `triage` in your available skills.) This decides whether Section C runs at all.
- Monorepo signals: a `pnpm-workspace.yaml`, a `workspaces` field in `package.json`, or a populated `packages/*` with its own `src/`. These are present only in a genuinely large multi-package repository; their absence means single-context, which is almost every repository.

### 2. Present findings and ask

Summarise what's present and what's missing. Then take the sections in order. One section, one answer, then the next.

Lead each section with the recommended answer so the user can accept it in a word. Give a one-line explainer only when the choice genuinely branches; skip the section entirely when exploration already settled it (Section C when `triage` isn't installed, Section D when there's no monorepo).

**Section A: Issue tracker.**

> Explainer: the issue tracker is the system of record for published issues and specifications. `to-tickets`, `to-specifications`, `triage`, and `wayfinder` read from it and publish to it. It is where work goes once it leaves `.refinement/`.

Ask exactly one question, recommending the kind that exploration pointed at:

> Where do published issues live? (recommended: **<kind found during exploration>**)
>
> - **Local markdown**: files under `backlog/<feature-slug>/`, committed to this repository. Fits solo projects and repositories with no remote.
> - **Remote tracker**: GitHub Issues (`gh` CLI), GitLab Issues ([`glab`](https://gitlab.com/gitlab-org/cli) CLI), Jira (MCP connector, CLI, or REST), or another tracker (Linear, Azure DevOps, …) you describe in one paragraph.

Take the recommendation from the remote: GitHub host recommends GitHub, GitLab host (`gitlab.com` or self-hosted) recommends GitLab, no remote recommends local markdown. The user overrides freely; a GitHub remote plus a Jira project is an ordinary combination.

For Jira, inspect the tools available in the current harness before asking how access works. If a Jira connector, CLI, or documented API workflow is available, identify it and verify access with the smallest read-only operation the available tool supports after the user provides the project key. Record the verified method and project key. If no Jira access is available, record publishing as **manual**: the skills may prepare the exact Markdown locally, but must not claim they can read or update Jira.

Record the choice in `documentation/agents/issue-tracker.md`. The GitHub and GitLab templates carry a "PRs as a request surface" flag, defaulted **off**. Leave it off and don't raise it: a user who wants external PRs in the triage queue can flip the flag in the file later.

**Section B: Ticket writing convention.**

Present any convention discovered during exploration, then ask exactly one question:

> Use **<discovered convention>** when drafting tickets? (recommended: **yes**)

When no convention was found, recommend the built-in `to-tickets` format and ask whether the repository follows another template or ticket-writing skill. Accept a repository path, an installed skill, or a short description. Choosing a skill such as `create-jira-ticket` adopts its ticket structure, language, and quality rules without adopting its creation workflow or making that skill mandatory.

Fill the "Ticket writing convention" section of the tracker template with:

- **Source:** `Built-in to-tickets`, a repository-relative document path, or the skill name plus the durable reference path that contains its templates.
- **Applies to:** refinement drafts, published tickets, or both.
- **Rules:** only the decisions needed to interpret the source, such as ticket language or required tracker metadata. Keep the full template in its source instead of copying it here.

The built-in convention remains available as a fallback on every run. An external convention changes the shape of each ticket, while `to-tickets` continues to own tracer-bullet decomposition, blocking edges, acceptance criteria, and publication approval.

**Section C: Triage role vocabulary.** Skip this section entirely if the `triage` skill isn't installed (exploration told you), since an uninstalled skill needs no vocabulary.

If it is installed, ask exactly one question:

> Do you want to keep the default triage role strings? (recommended: **yes**)

The defaults are the two canonical category roles (`bug`, `enhancement`) and the four canonical state roles (`to-evaluate`, `on-hold`, `ready`, `not-planned`), each string equal to its role name. On **yes**, write them as-is. Only if the user says no, usually because their tracker already uses other names (e.g. `bug:triage` for `to-evaluate`), collect the overrides so `triage` reuses existing vocabulary instead of creating duplicates. Only the strings are customisable; the role set itself stays canonical, because `to-tickets` and `to-specifications` apply `ready`.

**Section D: Domain documentation.** Default to **single-context** (one `CONTEXT.md` plus `documentation/architecture-decision-record/` at the repository root). This fits almost every repository; write it without asking.

Offer **multi-context** (a root `CONTEXT-MAP.md` pointing to per-context `CONTEXT.md` files) only when exploration found monorepo signals. Then confirm which layout they want.

### 3. Confirm and edit

Show the user a draft of:

- The `## Agent skills` block to add to whichever of `CLAUDE.md` / `AGENTS.md` is being edited (see step 4 for selection rules)
- The contents of `documentation/agents/issue-tracker.md`, `documentation/agents/domain.md`, and `documentation/agents/triage-roles.md` (the last only when `triage` is installed)

Let them edit before writing.

### 4. Write

**Pick the file to edit:**

- If `CLAUDE.md` exists, edit it.
- Else if `AGENTS.md` exists, edit it.
- If neither exists, ask the user which one to create; don't pick for them.

Never create `AGENTS.md` when `CLAUDE.md` already exists (or vice versa); always edit the one that's already there.

If an `## Agent skills` block already exists in the chosen file, update its contents in-place rather than appending a duplicate. Don't overwrite user edits to the surrounding sections.

The block:

```markdown
## Agent skills

### Issue tracker

[one-line summary: the system-of-record tracker, and that drafting happens in `.refinement/` until an explicit publish]. See `documentation/agents/issue-tracker.md`.

### Triage roles

[one-line summary of the role vocabulary]. See `documentation/agents/triage-roles.md`.

### Domain documentation

[one-line summary of layout: "single-context" or "multi-context"]. See `documentation/agents/domain.md`.
```

Include the `### Triage roles` sub-block, and write `documentation/agents/triage-roles.md`, only when `triage` is installed and Section C ran. When it isn't, both are omitted.

Write `documentation/agents/issue-tracker.md` from the seed template matching the chosen tracker, then append [refinement.md](./refinement.md) verbatim, adjusting only its publication line to the tracker in use:

- [issue-tracker-local.md](./issue-tracker-local.md): local-markdown tracker
- [issue-tracker-github.md](./issue-tracker-github.md): GitHub
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md): GitLab
- [issue-tracker-jira.md](./issue-tracker-jira.md): Jira
- For any other remote tracker, write the system-of-record sections from the user's paragraph, following the shape of the templates above: conventions, ticket writing convention, what "publish to the issue tracker" means, what "fetch the relevant ticket" means, and wayfinding operations.

Then write the remaining files:

- [triage-roles.md](./triage-roles.md): role vocabulary (only if `triage` is installed)
- [domain.md](./domain.md): domain documentation consumer rules and layout

### 5. Done

Tell the user the setup is complete and which workflow skills will now read from these files. Mention they can edit `documentation/agents/*.md` directly later; re-running this skill is only necessary if they want to switch issue trackers or restart from scratch.
