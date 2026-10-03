# Issue tracker: GitHub

Published tasks for this repository live as GitHub issues. Repository `documentation/<feature>/specifications.md` remains the canonical living specification; remote records link to or summarize it. Use the `gh` CLI for remote operations.

Backlog: <verified GitHub backlog or project-board URL>

The remote backlog owns candidate outcomes, priorities, and deferrals. Local `documentation/backlog.md` links to it; `documentation/work-in-progress.md` remains local for execution and resumption. Apply the authority and publication rules supplied by the `document` skill.

## Conventions

- **Create an issue**: `gh issue create --title "..." --body "..."`. Use a heredoc for multi-line bodies.
- **Read an issue**: `gh issue view <number> --comments`, filtering comments by `jq` and also fetching labels.
- **List issues**: `gh issue list --state open --json number,title,body,labels,comments --jq '[.[] | {number, title, body, labels: [.labels[].name], comments: [.comments[].body]}]'` with appropriate `--label` and `--state` filters.
- **Comment on an issue**: `gh issue comment <number> --body "..."`
- **Apply / remove labels**: `gh issue edit <number> --add-label "..."` / `--remove-label "..."`
- **Close**: `gh issue close <number> --comment "..."`

Infer the repository from `git remote -v`; `gh` does this automatically when run inside a clone.

## Ticket writing convention

- **Source:** Built-in `taskify`
- **Applies to:** Local task bodies and published tasks
- **Rules:** Use the built-in task template unless the user selects another configured convention for the run.

## Pull requests as a triage surface

**PRs as a request surface: no.** _(Set to `yes` if this repository treats external PRs as feature requests; `/triage` reads this flag.)_

When set to `yes`, PRs run through the same labels and states as issues, using the `gh pr` equivalents:

- **Read a PR**: `gh pr view <number> --comments` and `gh pr diff <number>` for the diff.
- **List external PRs for triage**: `gh pr list --state open --json number,title,body,labels,author,authorAssociation,comments` then keep only `authorAssociation` of `CONTRIBUTOR`, `FIRST_TIME_CONTRIBUTOR`, or `NONE` (drop `OWNER`/`MEMBER`/`COLLABORATOR`).
- **Comment / label / close**: `gh pr comment`, `gh pr edit --add-label`/`--remove-label`, `gh pr close`.

GitHub shares one number space across issues and PRs, so a bare `#42` may be either: resolve with `gh pr view 42` and fall back to `gh issue view 42`.

## When a skill says "publish to the issue tracker"

Create or update a GitHub issue only on an explicit user request. Local document upkeep does not authorize remote writes. When useful, keep a title/link reference under `documentation/<feature>/tasks/` instead of copying the published task body.

## When a skill says "fetch the relevant task"

Run `gh issue view <number> --comments`.

## Wayfinding operations

Used by `/graphify`. The map is a single GitHub issue with child issues as decision tasks.

- **Map**: a single issue labelled `graphify:map`, holding the Notes / Decisions-so-far / Fog body. `gh issue create --label graphify:map`.
- **Child task**: an issue linked to the map as a GitHub sub-issue (`gh api` on the sub-issues endpoint). Where sub-issues aren't enabled, add the child to a task list in the map body and put `Part of #<map>` at the top of the child body. Labels: `graphify:<type>` (`research`/`prototype`/`refine`/`task`). Once claimed, the task is assigned to the driving developer.
- **Blocking**: GitHub's **native issue dependencies**, the canonical, UI-visible representation. Add an edge with `gh api --method POST repos/<owner>/<repo>/issues/<child>/dependencies/blocked_by -F issue_id=<blocker-db-id>`, where `<blocker-db-id>` is the blocker's numeric **database id** (`gh api repos/<owner>/<repo>/issues/<n> --jq .id`, _not_ the `#number` or `node_id`). GitHub reports `issue_dependencies_summary.blocked_by` (open blockers only, the live gate). Where dependencies aren't available, fall back to a `Blocked by: #<n>, #<n>` line at the top of the child body. A task is unblocked when every blocker is closed.
- **Frontier query**: list the map's open children (`gh issue list --state open`, scoped to the map's sub-issues / task list), drop any with an open blocker (`issue_dependencies_summary.blocked_by > 0`, or an open issue in the `Blocked by` line) or an assignee; first in map order wins.
- **Claim**: `gh issue edit <n> --add-assignee @me`, the session's first write.
- **Resolve**: `gh issue comment <n> --body "<answer>"`, then `gh issue close <n>`, then append a context pointer (gist + link) to the map's Decisions-so-far.
