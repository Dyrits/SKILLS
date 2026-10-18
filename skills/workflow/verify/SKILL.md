---
name: verify
description: "Prove that implemented work behaves as intended, by any means available (the running application, tests, browser, API, or command-line checks), and record a reproducible proof in the repository. Use when the user asks to verify or prove that a change works, or wants evidence before merging or shipping."
---

# Verify

A **proof** gives every claim the work makes evidence that a skeptical reviewer can rerun, and that would have come out differently had the work been wrong. Passing tests alone are not a proof: a check counts only when it observes the behavior and has been shown able to fail.

Verify observes; it does not fix. When a claim fails, record it and report it, leaving production code as it is.

Copy this checklist and track progress:

```
- [ ] 1. Claims listed
- [ ] 2. Evidence gathered
- [ ] 3. Every check shown able to fail
- [ ] 4. Regressions checked
- [ ] 5. Proof written
- [ ] 6. Proof reproduced
- [ ] 7. Cleaned up and reported
```

## 1. List the claims

Pin the work: the starting commit (the fixed point the user gives, or the merge-base with the default branch) and the end state, uncommitted changes included. Recover what the work is meant to do from the user's request, the agreement it came from (specifications, tasks, acceptance criteria, working state, found through `AGENTS.md`), and the commit messages and diff. Write each intended behavior as one claim with its source, adding the edge cases it covers and the existing behavior it must not break. Ask the user only when sources conflict or the intent cannot be recovered.

Done when every acceptance criterion and every behavior the diff changes maps to a claim.

## 2. Gather the evidence

For each claim, observe the behavior where a user meets it, with the strongest means the environment allows:

| Behavior | Evidence |
| --- | --- |
| Interface (web, desktop, mobile) | Drive the running application; capture screenshots, console and network logs |
| API or service | Real requests against the running service; capture request and response |
| Command-line tool or script | Run it; capture the exact command, exit code, and output |
| Data, migrations, files | Read the resulting state through the system's own interface |
| Logic with no reachable entry point | A test at its public interface |

Any tool will do: the project's test runner, browser automation (Playwright, a browser MCP server, Claude in Chrome), `curl`, the application's own command-line interface, a scratch script. Probe what is installed before choosing. When the strongest means is missing, use the next one and record what was unavailable. When no existing check observes a claim, write a test or script for it outside production code.

Appearance and feel need a human eye: capture screenshots or a recording and mark the claim **awaiting human judgment**, never proven.

## 3. Show every check can fail

A check that would pass on broken code proves nothing. For each claim, show at least one of:

- **Before and after**: run the check against the starting commit in a separate worktree (`git worktree add`), see it fail for the expected reason, then see it pass on the end state.
- **Mutation**: in a separate worktree of the end state (`git worktree add`, with uncommitted changes applied there), break the code the check covers (invert a condition, drop the call, return a constant) and see the check fail. Never mutate the user's checkout.

Afterwards confirm the user's checkout still matches its state before verification (`git status` and `git diff`). A claim whose check could not be shown to fail stays **unproven**, whatever the check printed.

## 4. Check for regressions

Run the project's full test suite, typecheck, lint, and build, as its scripts and `AGENTS.md` define them. Run any that fail against the starting commit too, so a failure the work did not cause is reported as pre-existing and a failure it did cause is never excused.

## 5. Write the proof

Fill in [proof-template.md](assets/proof-template.md). Save it where the project keeps verification records, as `AGENTS.md` names them, matching their naming and style. With no such home, save it as `documentation/verification/<YYYY-MM-DD>-<slug>.md`, put screenshots and logs in a sibling folder of the same name, and add one line to `AGENTS.md` saying what the records hold and when to read them. Never overwrite an existing proof; write a new one.

Give each claim one verdict: **proven** (observed, shown able to fail, reproduced), **failed**, **unproven** (no means available, or no check shown able to fail), or **awaiting human judgment**. The overall verdict is proven only when every claim is.

## 6. Reproduce the proof

Give the proof file alone to a fresh-context subagent that has not seen the implementation, and have it rerun every command and interaction and report where its results match or differ. Without subagents, rerun everything yourself from a clean shell. Record the reproduction in the proof; a claim that did not reproduce is not proven.

## 7. Clean up and report

Stop the processes you started and remove the worktrees you added. Leave the proof and any new tests or scripts uncommitted: the user commits them with the work, or asks you to.

Report the overall verdict, the count of claims per verdict, the proof's path, each claim that is not proven and why, and the new files left uncommitted.
