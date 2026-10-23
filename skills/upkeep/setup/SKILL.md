---
name: setup
description: "Set up a repository, or an empty project, for AI-assisted work: task tracking and triage roles, commit-time formatting, linting and typechecking, guards that make agents ask before destructive Git commands, and AI development tools. Use when the user asks to set up or reconfigure a repository, or any one of those areas, such as pre-commit hooks, Git guardrails, or AI tooling."
metadata:
  forks: "mattpocock/skills/skills/engineering/setup-matt-pocock-skills mattpocock/skills/skills/misc/setup-pre-commit mattpocock/skills/skills/misc/git-guardrails-claude-code"
---

# Setup

Inspect the repository, offer the areas below with their current state, and set up the ones the user picks. Upstream command-line tools do the installing; this skill decides what to run and checks that it worked.

| Area | Sets up | Reference |
| --- | --- | --- |
| Workspace | Task tracker, ticket-writing convention, triage roles, domain contexts | [workspace.md](references/workspace.md) |
| Code checks | Formatter, linter, and typecheck run by a committed pre-commit hook; moves off older tooling on request | [code-checks.md](references/code-checks.md), plus the catalogue of each language found: [JavaScript and TypeScript](references/checks-javascript.md), [Python](references/checks-python.md), [Go](references/checks-go.md), [Rust](references/checks-rust.md) |
| Git guardrails | A human decision before Git commands that lose work or rewrite shared history, for each agent harness | [guardrails.md](references/guardrails.md) |
| AI tooling | Code index, documentation lookup, structural search, browser and tracker clients, and a measurement baseline | [ai-tooling.md](references/ai-tooling.md) |

Read an area's reference only once it is picked.

## Quiet commands

Installers and indexers print a lot. Run each install or configuration command with its output sent to a log outside the repository, and read the exit status and the log's last lines:

```bash
log="${TMPDIR:-/tmp}/setup-<tool>.log"; <command> >"$log" 2>&1; echo "exit $?"; tail -n 5 "$log"
```

Read the whole log only when the command failed. Use the commands the references list as written; read a tool's `--help` or documentation only after its listed command fails, and say in the report which entry needed it.

## Steps

### 1. Inspect

Run `python3 -I scripts/inspect-project.py <repository>` (add `--json` for structured output). It reports Git state, languages, package manager and scripts, formatter, linter, and typecheck configuration, older tooling and hook managers, the hooks directory, conventions candidates, `AGENTS.md` pointers, setup records under `.agents/`, and the tools on the path.

Then read the project's conventions: the document `AGENTS.md` names for conventions, or else the candidates the script lists (contribution guides, style guides) and `.editorconfig`. Note every rule a tool can carry (indentation, quotes, line width, import order, banned constructs).

When the user named one area, skip to step 3 for that area.

Completion: each area has a state (not set up, partly set up, set up), and the conventions' tool rules are noted, or their absence is.

### 2. Offer the areas

Show each area with its state and a recommendation, and ask in one round which to set up (use the harness's question tool when it has one, plain chat otherwise). Recommend an area that is not set up; recommend leaving a set-up area alone unless the user reported a problem with it.

An empty repository (no source files) has no stack yet. Ask which language and framework the project will use; take the answer as given, since choosing a stack is an architecture decision, not a setup one. Without an answer, offer workspace, Git guardrails, and AI tooling, and leave code checks for when code exists. Run `git init` first when there is no repository, after saying so.

Completion: the user has picked the areas, and the stack is known or explicitly absent.

### 3. Set up each picked area

Follow each picked area's reference in this order: workspace, code checks, Git guardrails, AI tooling. Code checks come before guardrails because both write to the hooks directory code checks may move.

Completion: every picked area's reference reached its own completion criterion, or stopped on a stated gap.

### 4. Report

One block per area: what was installed or written, what was reused, what was checked and how, and what stays open (a tool left disabled, a harness that could not be checked, a missing conventions document). Name every file written outside the repository.
