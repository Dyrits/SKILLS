# Evaluations

This folder holds the evaluation reports worth versioning. Raw responses, snapshots, detailed grades, and viewers stay in local workspaces.

Test cases live next to each skill, in `skills/<bucket>/<skill>/evals/`, in the format [`.agents/writing-evals.md`](../../.agents/writing-evals.md) defines. `python3 .agents/scripts/stage-eval-run.py` stages a skill's cases for a run and writes the grading sheet. Notes that predate this format, such as `waza.md`, stay as they are.

## Report format

Write one Markdown file per skill and per date, named `YYYY-MM-DD-<skill>.md`. Use the UTC date, and put only the date and the skill name in the title, with no time.

The date marks when the report was written. When the run dates are known, state them separately; do not infer them from the file date.

Open with the result and what it allows us to conclude. Then cover:

- The skill evaluated, its version or fingerprint (commit and path), and the models and tools used.
- The scenarios, the number of runs, and the results, as numerators over denominators.
- Failures, limits of the evidence, tests not run, and what is still open.
- Which results come from simulations, which from real reads, and which from offline tests.
- The commands to reproduce the run, and links to the versioned definitions.

Report a measurement that is unavailable as unavailable. A result from an existing setup does not validate a new installation. Real-world tests stay optional and follow the skill's own authorization protocol.

Keep earlier reports. Several evaluations of the same skill on the same day extend that day's report without deleting earlier results. A new date gets a new file. A factual correction is flagged inside the report it corrects.

A report must read without the local, unversioned artifacts. Leave out secrets, identities, log payloads, and business data; keep only the redacted results the conclusion needs.
