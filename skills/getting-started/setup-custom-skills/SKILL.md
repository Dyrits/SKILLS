---
name: setup-custom-skills
description: "Configure this repository for the workflow skills: set up its issue tracker, optional local draft workspace, ticket-writing convention, triage label vocabulary, and domain documentation layout. Run once before first use of the tracker-consuming skills."
disable-model-invocation: true
---

# Setup Custom Skills

Scaffold the per-repository configuration that the workflow skills assume:

- **Issue tracker**: where issues live (GitHub by default; local markdown is also supported out of the box)
- **Local drafts**: whether refinement stays under `.scratch/<issue-key>/` until an explicit publish step
- **Ticket writing convention**: whether tickets use the built-in format or an existing project template or ticket-writing skill
- **Triage labels**: the strings used for the five canonical triage roles
- **Domain documentation**: where `CONTEXT.md` and architecture decision records live, and the consumer rules for reading them

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

## Process

### 1. Explore

Look at the current repository to understand its starting state. Read whatever exists; don't assume:

- `git remote -v` and `.git/config`: is this a GitHub repository? Which one?
- `AGENTS.md` and `CLAUDE.md` at the repository root: does either exist? Is there already an `## Agent skills` section in either?
- `CONTEXT.md` and `CONTEXT-MAP.md` at the repository root
- `documentation/architecture-decision-record/` and any `src/*/documentation/architecture-decision-record/` directories
- `documentation/agents/`: does this skill's prior output already exist?
- `.scratch/`: a sign that a local-markdown issue tracker convention is already in use
- Issue templates, contribution documentation, and available ticket-writing skills: is there an established ticket structure, language, or required metadata?
- Is the `triage` skill installed? (a `triage` skill folder alongside this one, or `triage` in your available skills.) This decides whether Section B runs at all.
- Monorepo signals: a `pnpm-workspace.yaml`, a `workspaces` field in `package.json`, or a populated `packages/*` with its own `src/`. These are present only in a genuinely large multi-package repository; their absence means single-context, which is almost every repository.

### 2. Present findings and ask

Summarise what's present and what's missing. Then take the sections in order. One section, one answer, then the next.

Lead each section with the recommended answer so the user can accept it in a word. Give a one-line explainer only when the choice genuinely branches; skip the section entirely when exploration already settled it (Section B when `triage` isn't installed, Section C when there's no monorepo).

**Section A: Issue tracker.**

> Explainer: The "issue tracker" is the system of record for this repository. Skills like `to-tickets`, `triage`, and `to-specifications` read from and publish to it. Local refinement drafts can still live under `.scratch/`; choosing Jira or GitHub does not rule that out.

Default posture: these skills were designed for GitHub. If a `git remote` points at GitHub, propose that. If a `git remote` points at GitLab (`gitlab.com` or a self-hosted host), propose GitLab. Otherwise (or if the user prefers), offer:

- **GitHub**: issues live in the repository's GitHub Issues (uses the `gh` CLI)
- **GitLab**: issues live in the repository's GitLab Issues (uses the [`glab`](https://gitlab.com/gitlab-org/cli) CLI)
- **Jira**: issues live in a Jira project (uses an available Jira MCP connector, CLI, or REST workflow)
- **Local markdown**: issues live as files under `.scratch/<feature>/` in this repository (good for solo projects or repositories without a remote)
- **Other** (Linear, Azure DevOps, etc.): ask the user to describe the workflow in one paragraph; the skill will record it as freeform prose

For Jira, inspect the tools available in the current harness before asking how access works. If a Jira connector, CLI, or documented API workflow is available, identify it and verify access with the smallest read-only operation the available tool supports after the user provides the project key. Record the verified method and project key. If no Jira access is available, record publishing as **manual**: the skills may prepare the exact Markdown locally, but must not claim they can read or update Jira.

Record the choice in `documentation/agents/issue-tracker.md`. The GitHub and GitLab templates carry a "PRs as a request surface" flag, defaulted **off**. Leave it off and don't raise it: a user who wants external PRs in the triage queue can flip the flag in the file later.

**Section A2: Local refinement drafts.** Skip this section when local markdown is the system of record, because the tracker itself is already local.

Ask exactly one question:

> Keep refinement drafts local until an explicit publish step? (recommended: **yes**)

On **yes**, add a "Local refinement drafts" section to `documentation/agents/issue-tracker.md` with these conventions:

- One workspace per source issue at `.scratch/<issue-key>/`, or `.scratch/<feature-slug>/` when no issue exists yet.
- The refined specification lives at `specification.md`; draft implementation tickets live under `issues/` as one file per ticket.
- A draft sourced from the tracker records its issue key and URL at the top of `specification.md`.
- Local files are working artifacts, while the configured tracker remains the system of record.
- Reading from the tracker is allowed through the verified access method. Updating it requires an explicit publish request from the user.

On **no**, record that specifications and tickets publish directly to the configured tracker.

**Section A3: Ticket writing convention.**

Present any convention discovered during exploration, then ask exactly one question:

> Use **<discovered convention>** when drafting tickets? (recommended: **yes**)

When no convention was found, recommend the built-in `to-tickets` format and ask whether the repository follows another template or ticket-writing skill. Accept a repository path, an installed skill, or a short description. Choosing a skill such as `create-jira-ticket` adopts its ticket structure, language, and quality rules without adopting its creation workflow or making that skill mandatory.

Add a "Ticket writing convention" section to `documentation/agents/issue-tracker.md` that records:

- **Source:** `Built-in to-tickets`, a repository-relative document path, or the skill name plus the durable reference path that contains its templates.
- **Applies to:** local drafts, published tickets, or both.
- **Rules:** only the decisions needed to interpret the source, such as ticket language or required tracker metadata. Keep the full template in its source instead of copying it here.

The built-in convention remains available as a fallback on every run. An external convention changes the shape of each ticket, while `to-tickets` continues to own tracer-bullet decomposition, blocking edges, acceptance criteria, and publication approval.

**Section B: Triage label vocabulary.** Skip this section entirely if the `triage` skill isn't installed (exploration told you), since an uninstalled skill needs no labels.

If it is installed, ask exactly one question:

> Do you want to keep the default triage labels? (recommended: **yes**)

The defaults are the two canonical category roles (`bug`, `enhancement`) and the five canonical state roles (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`), each label string equal to its role name. On **yes**, write them as-is. Only if the user says no, usually because their tracker already uses other names (e.g. `bug:triage` for `needs-triage`), collect the overrides so `triage` applies existing labels instead of creating duplicates. Only the label strings are customisable; the role set itself stays canonical, because `to-tickets` and `to-specifications` apply `ready-for-agent`.

**Section C: Domain documentation.** Default to **single-context** (one `CONTEXT.md` plus `documentation/architecture-decision-record/` at the repository root). This fits almost every repository; write it without asking.

Offer **multi-context** (a root `CONTEXT-MAP.md` pointing to per-context `CONTEXT.md` files) only when exploration found monorepo signals. Then confirm which layout they want.

### 3. Confirm and edit

Show the user a draft of:

- The `## Agent skills` block to add to whichever of `CLAUDE.md` / `AGENTS.md` is being edited (see step 4 for selection rules)
- The contents of `documentation/agents/issue-tracker.md`, `documentation/agents/domain.md`, and `documentation/agents/triage-labels.md` (the last only when `triage` is installed)

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

[one-line summary of the system-of-record tracker, local-draft publication boundary, and ticket-writing convention]. See `documentation/agents/issue-tracker.md`.

### Triage labels

[one-line summary of the label vocabulary]. See `documentation/agents/triage-labels.md`.

### Domain documentation

[one-line summary of layout: "single-context" or "multi-context"]. See `documentation/agents/domain.md`.
```

Include the `### Triage labels` sub-block, and write `documentation/agents/triage-labels.md`, only when `triage` is installed and Section B ran. When it isn't, both are omitted.

Then write the documentation files using the seed templates in this skill folder as a starting point:

- [issue-tracker-github.md](./issue-tracker-github.md): GitHub issue tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md): GitLab issue tracker
- [issue-tracker-jira.md](./issue-tracker-jira.md): Jira issue tracker
- [issue-tracker-local.md](./issue-tracker-local.md): local-markdown issue tracker
- [triage-labels.md](./triage-labels.md): label mapping (only if `triage` is installed)
- [domain.md](./domain.md): domain documentation consumer rules and layout

For "other" issue trackers, write `documentation/agents/issue-tracker.md` from scratch using the user's description. Append the local-refinement section selected in Section A2 to any remote-tracker template instead of replacing its system-of-record operations.

### 5. Done

Tell the user the setup is complete and which workflow skills will now read from these files. Mention they can edit `documentation/agents/*.md` directly later; re-running this skill is only necessary if they want to switch issue trackers or restart from scratch.
