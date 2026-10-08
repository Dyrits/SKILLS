---
name: swarm
description: "Divide one task into independent pieces and run them in parallel on fast, low-cost subagents the user selects, then merge and spot-check their reports. Use when the user asks for a swarm or to fan work out across many cheap agents: sweeping, auditing, summarising, or applying independent changes across many items."
---

# Swarm

Run one task as many small, independent **pieces**, each on its own fast, low-cost **worker** subagent, and merge the **reports** here. A swarm has no task graph, branches, or review phase: dependent work runs as **waves**, a second swarm that starts from the first one's reports.

Pieces can differ from each other and can read or edit. Run subagents in the background, all pieces of a wave in one message.

## 1. Split

Cut the task into pieces that each finish without steering and without reading another piece's output. A piece that costs more to brief than to do stays here.

A piece that edits **owns** a set of files, and no file has two owners. A file two pieces need goes to one of them, or to a later wave.

Completion: every part of the task sits in exactly one piece or is marked kept here, and no file is owned twice.

## 2. Choose the crew

Read the agents and models the delegation tool offers in this session and trust them over the names below. With no delegation tool, do the task here and say so.

Suggest the cheapest tier that does each piece reliably; when the "Delegation and model routing" rule is installed in your steering file, it governs. Otherwise:

- **Light** (Haiku, Luna): small, deterministic, well-scoped, verifiable pieces. The default suggestion.
- **Balanced** (Sonnet, Terra): pieces that need judgment or touch several files.
- Anything above Balanced is a sign the piece is not swarm-sized: keep it here or split it.

Show a table: piece, inputs, owned files (edits only), suggested agent and model. Below it, state the worker count and that each reloads its own context, so cost grows with the count; quote measured costs only. The user selects the agents and may amend the pieces. Wait for that answer, except when the request already names the agents or model: read-only pieces then dispatch at once, and edit pieces still wait for a yes on the piece list.

Completion: the user selected an agent for every piece, or the request named them.

## 3. Brief and dispatch

Each worker's brief is self-contained and holds:

- the goal of its piece, with the relevant words of the user's request verbatim;
- its inputs by path;
- its owned files, with the rule that it writes only those and stops to report if it needs another;
- the report shape: `status` (done, partial, or failed), findings or changed files, evidence for each claim, and anything it could not do;
- the rule not to spawn agents.

Completion: every piece of the wave is running.

## 4. Merge

Combine the reports without redoing the work. A failed or unusable report is not retried automatically: report it and let the user choose to rerun it on a stronger agent, redo it here, or drop it.

When a piece needs another's result, run a second wave through steps 1 to 3. If pieces still block each other after two waves, finish the rest here.

## 5. Verify

- Edits: confirm every changed file belongs to its piece's owner, then run the project's checks once over the whole result.
- Read-only: check at least one claim from each report against its source, more where reports disagree or surprise you.

Completion: every result is labelled verified or unverified.

## 6. Report

State the merged result, what is verified and what is not, the agent and model behind each piece, and each failure with its disposition.
