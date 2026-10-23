# Evaluations

Evaluation suites for the skills, run with `claude plugin eval`, following [architecture decision record 0008](../documentation/architecture-decision-record/0008-resume-skill-evaluations.md). The plugin manifest points the command here through `experimental.evals`. Suites are optional; a skill with none is acceptable.

## Layout

One folder per bucket, one per skill, one per case: `evaluations/<bucket>/<skill>/<case>/`, holding `prompt.md` and `graders/*.md`. Only case folders hold a `prompt.md` or `case.yaml`. Each skill has a positive case (the skill should fire, plus one check on what it produced) and a near-miss negative case (the skill must not fire, scored in both arms).

Every run is one turn in an empty workspace. Interactive skills (`interview`, `prioritize`, `graphify`) are graded on what their first turn should contain, not on a settled outcome.

## Running

An evaluation run is a paid action: each case runs three times with the plugin and three times without, plus judge calls. Start with a capped smoke run of one case:

```bash
claude plugin eval evaluations/shaping/interview/grills-a-plan/prompt.md --runs 1 --ablation none --max-cost-usd 1
```

A full bucket, with the tools the positive cases need:

```bash
claude plugin eval . --tag shaping --allow-tools Write Edit WebFetch WebSearch --max-cost-usd 20
```

Without `--allow-tools`, writing and web tools are removed from the run, and every `file_exists` grader fails for a reason that is not the skill's. Results land in `evaluations/results/`, which Git ignores. Reports worth keeping go to [documentation/evaluations](../documentation/evaluations/README.md).

## Known limits

- `research` hands its work to a background agent. Whether the run waits for that agent, and whether files it writes count for `file_exists`, is unverified; the prompt asks the agent to wait for the notes.
- `prototype` covers the logic branch only: an empty workspace has no route for the UI branch to attach to.
