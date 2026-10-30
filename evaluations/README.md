# Evaluations

Evaluation suites for the skills, run with `claude plugin eval`, following [architecture decision record 0008](../documentation/architecture-decision-record/0008-resume-skill-evaluations.md). The plugin manifest points the command here through `experimental.evals`. Suites are optional; a skill with none is acceptable.

## Layout

One folder per bucket, one per skill, one per case: `evaluations/<bucket>/<skill>/<case>/`, holding `prompt.md` and `graders/*.md`. Only case folders hold a `prompt.md` or `case.yaml`. Each skill has a positive case (the skill should fire, plus one check on what it produced) and a near-miss negative case (the skill must not fire, scored in both arms).

Every run is one turn in an empty workspace. Interactive skills (`interview`, `prioritize`, `graphify`, and most of `workflow`) are graded on what their first turn should contain, not on a settled outcome. Context a skill would read from a repository or a session (review comments, a diff, a described session, a draft) is pasted into the prompt instead.

A case that needs files or Git state adds a `case.yaml` beside `prompt.md` whose `context.scaffold_script` names a `fixture.sh` in the case folder. `file_exists` sees only files Claude created, so Git outcomes are graded from the trace (`tool_used` on `Bash` commands) and from file contents (`regex` with `target: {source: file, path: ...}`).

A case's `allowed_tools` lists the tools it wants. Read-only tools are granted from that list; `Write`, `Edit`, `Bash`, `WebFetch`, and `WebSearch` are granted only by the operator's `--allow-tools`, and a run without the grant reports them as `not granted`.

## Running

An evaluation run is a paid action: each case runs three times with the plugin and three times without, plus judge calls. Start with a capped smoke run of one case:

```bash
claude plugin eval evaluations/shaping/interview/grills-a-plan/prompt.md --runs 1 --ablation none --max-cost-usd 1
```

A full bucket, with the tools the positive cases need:

```bash
claude plugin eval . --tag shaping --allow-tools Write Edit WebFetch WebSearch --max-cost-usd 20
```

The other buckets. `--scaffold` runs each case's own bash as you, outside the sandbox, and Git cases need a Git that does not go through `xcrun`, so on macOS put Homebrew Git first in `PATH`:

```bash
claude plugin eval . --tag workflow --allow-tools Write Edit Bash --max-cost-usd 50
PATH="/opt/homebrew/bin:$PATH" claude plugin eval . --tag upkeep --allow-tools Write Edit Bash --scaffold --max-cost-usd 35
claude plugin eval . --tag productivity --allow-tools Write Edit Bash --max-cost-usd 50
PATH="/opt/homebrew/bin:$PATH" claude plugin eval . --tag version-control --allow-tools Write Edit Bash --scaffold --max-cost-usd 20
```

Without `--allow-tools`, writing and web tools are removed from the run, and every `file_exists` grader fails for a reason that is not the skill's. Granting `Bash` needs the operating system sandbox (on Linux, bubblewrap and socat); without it every run with `Bash` scores 0. Results land in `evaluations/results/`, which Git ignores. Reports worth keeping go to [documentation/evaluations](../documentation/evaluations/README.md).

## Known limits

- `research` hands its work to a background agent. Whether the run waits for that agent, and whether files it writes count for `file_exists`, is unverified; the prompt asks the agent to wait for the notes.
- `prototype` covers the logic branch only: an empty workspace has no route for the UI branch to attach to.
- Gate-only cases: `architect`, `delineate`, `specify`, `engineer`, `taskify`, `iterate`, `design-workflow`, `teach`, and `walk-through` stop at their first question or proposal, so the documents they write after approval are not graded. `divide-and-conquer` and `swarm` stop at the routing or crew approval; dispatch and merging are not reached.
- Nothing is published: `publish-message` is graded on drafting and waiting for approval, never on posting or read-back.
- No repository context: `review-and-refactor` and `verify` only reach their first decision (ask for the fixed point, list the claims).
- `memorize` covers the project-convention route only; recall, the glossary, and a second run's idempotence are not covered.
- `hand-off` is told the handoff is shared, since an empty workspace has no `.gitignore` to decide it.
- Some negatives may fire a neighbouring skill; each `skill-not-fired` grader checks only its own skill.
- The `workflow` and `productivity` suites have not been run yet.
