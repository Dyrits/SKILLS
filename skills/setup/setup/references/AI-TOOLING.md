# AI tooling

Install and wire free AI development tools for the project and the agent clients on the machine, check each one, and record a baseline later measurements can compare against. Reuse working integrations; leave an unverified adapter or filter disabled and say so.

## Contents

- Catalogue
- Steps: choose, install and wire, check, protect output (RTK), record the baseline
- Choosing by task

## Catalogue

Verified: 2026-10-10, against each tool's official page, except where a row says otherwise. Install output goes through the quiet commands.

| Tool | Present when | Install | Wire into agents | Check |
| --- | --- | --- | --- | --- |
| CodeGraph | `codegraph` on the path; `.codegraph/` in the project | `npm i -g @colbymchenry/codegraph` | `codegraph install --yes` (add `--location=local` for this project only; `codegraph install --print-config <client>` previews without writing) | `codegraph init` when there is no index, then `codegraph status`, then `codegraph explore <known symbol>` returns source matching the file |
| Context7 | A Context7 MCP connection in the client, or `ctx7` | Runs through `npx` (Node 18 or later) | `npx ctx7 setup --claude` or `--opencode` (signs in through the browser and creates a free key: the user completes it). Other clients: the MCP server `https://mcp.context7.com/mcp`, through the client's MCP configuration | `npx ctx7 library <dependency> <topic>` returns an ID, and `npx ctx7 docs <ID> <topic>` returns documentation for the installed version |
| ast-grep | `ast-grep` on the path | `brew install ast-grep` or `npm i -g @ast-grep/cli` | None | `ast-grep --pattern '<pattern>' --lang <language> <path>` finds a known match and skips a known non-match |
| Playwright CLI | `playwright-cli` on the path | `npm install -g @playwright/cli@latest` | `playwright-cli install --skills` | `playwright-cli open https://example.com`, then `playwright-cli snapshot` |
| Chrome DevTools MCP | The server in the client's MCP configuration | Runs through `npx` | Add the server command `npx -y chrome-devtools-mcp@latest` (`--headless`; `--slim` for basic tasks) through the client's MCP configuration | A read-only page load returns a snapshot or trace |
| RTK | `rtk --version` and `rtk gain` both work (another package shares the name) | `brew install rtk`; when `rtk gain` fails, `cargo install --git https://github.com/rtk-ai/rtk` | `rtk init -g` (Claude Code), `rtk init -g --codex`, `rtk init -g --opencode`, `rtk init -g --gemini`; `--hook-only` skips its instruction file | `rtk init --show`, then the protected-output checks below. `rtk init -g --uninstall` removes it |
| GitHub CLI, GitLab CLI | `gh` or `glab` on the path | The platform's package manager (`brew install gh`, `brew install glab`); not checked on 2026-10-10 | None | `gh auth status` or `glab auth status` |

Serena is optional and has no entry: read its documentation only when a navigation gap calls for it.

## Steps

### 1. Choose

Work from the inspection's `on_path` and `codegraph_index` lines. Run `python3 -I scripts/detect-harnesses.py --project .` for the agent clients, add the one you are running in if it is missing, and ask the user to confirm the list. A binary, a project index, and a connected client are separate states: check each.

Recommend from [Choosing by task](#choosing-by-task). Use free tools and free tiers; ask before anything that needs payment or a new account. Show the project changes, the global changes, and the check commands together, and ask only what the request has not settled. An explicit request for project and missing global setup covers routine installation within that scope.

Completion: every candidate has a decision, its current state, and a wiring path per client or a stated gap.

### 2. Install and wire

Run the catalogue commands for the chosen tools and clients. Skip any step whose "present when" already holds. Merge into existing settings, keep unrelated entries, and make a rerun change nothing. Use an existing project automation target (a Makefile or package script) where it does the same job, and keep index initialization conditional there so an existing index is preserved.

Completion: every chosen tool is installed and wired, or stopped with its failing command and log tail.

### 3. Check

Run each chosen tool's check through each client it was wired into. Published benchmark figures are not this project's savings.

Completion: every tool and client pair has passed its check, or is left disabled with the reason.

### 4. Protect output (RTK only)

RTK rewrites command output. Before enabling automatic rewrites, protect the output review and diagnosis depend on: `git diff`, `git show`, file reads, text and structural searches, and the project's test, build, and diagnostic commands, including their real invocations (`git -C`, package-manager wrappers, project scripts). Add them under `exclude_commands` in the `[hooks]` table of RTK's `config.toml`, merged into the existing list.

An exclusion alone proves nothing. Through the installed adapter, compare against the original command: a large patch with context, a rename, and a deliberately failing command with distinctive standard error and a nonzero exit status. Output and exit status must survive. When the adapter cannot guarantee that, leave broad rewriting disabled and use explicit `rtk` commands for chosen summaries. Keep RTK's tracking on, and leave the user's own token monitor in place.

Completion: every protected command returns the original output and exit status through the adapter, or rewriting stays off.

### 5. Record the baseline

Write the project's tooling record (at `.agents/ai-tooling.md` unless `AGENTS.md` already names one elsewhere, adopting a record already at that path rather than overwriting it). When you create it, add one line to the nearest `AGENTS.md` saying what it records and when to read it, following [AGENT-INSTRUCTIONS.md](AGENT-INSTRUCTIONS.md). The record holds:

- Setup time, tools and versions, project or global scope, and wiring status per client.
- Checks run and their results, known gaps, protected commands, and bypasses.
- Local measurement sources (their schema or version, time range, project attribution), baseline counter values, and retention limits.
- Representative read-only tasks with correctness criteria, duration, and output bytes where measured; unknown values stay unknown.
- A checked session recovery method per client (transcript location or resume command), which must work after the plan allowance runs out, without a new handoff.

Commit the record only after removing credentials and personal session paths; keep measurement history and diagnostic logs local and out of version control.

Completion: the record points to real measurement sources, and each client's recovery is checked or marked unavailable.

For the report, keep command-output reduction, task token counts, and provider allowance as separate quantities, and claim equal task quality only where the comparison checked the same correctness criteria.

## Choosing by task

- **CodeGraph** for supported source projects; reuse working language servers alongside it.
- **Context7** for dependency documentation, when not already connected.
- **ast-grep** when a real query needs a call shape, argument structure, or enclosing node that symbol navigation cannot answer. Code rewrites with it need a separate request.
- **Browser**: none for static pages and plain HTTP. Playwright CLI for driving pages (navigation, forms, logins, screenshots, traces); it adds no tool schema to the agent's context. Chrome DevTools MCP for diagnosing pages (console, network, performance traces); Chrome only, and its tool definitions add context. Attaching it to a running browser exposes that profile, so confirm the scope first. Both only when the project has both kinds of work.
- **Tracker CLI** for the project's tracker, checked with a read-only command; setup publishes nothing to the tracker.
- **RTK** only through the protected-output step.
