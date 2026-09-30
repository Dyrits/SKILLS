# Measurement rules

## Units and attribution

| Evidence | What it establishes | Required qualification |
| --- | --- | --- |
| Provider or existing monitor export | Reported token usage or remaining allowance | Preserve provider, model, time window, cache categories, and account scope. |
| RTK analytics | Raw versus filtered command output, expressed as byte reduction or estimated tokens | RTK's token estimates use bytes divided by four; they are not provider token counts or subscription savings. |
| Local command observations | Duration, output bytes, exit status, and invocation count | Command output is only part of an agent's context; attribute the observation to the measured command. |
| Comparable agent task runs | Observed task token counts, runtime, and correctness outcomes | Both runs need the same task, scope, relevant client/model settings, and acceptance criteria. |
| External benchmark | A published result under the publisher's conditions | Label it external and keep it out of personal savings totals. |

If RTK reports estimated raw and filtered tokens, identify their byte-based estimator and avoid relabeling them as independently observed bytes.
Its quota estimate is a model of a plan budget, not a live allowance reading.
Follow [RTK's methodology](https://github.com/rtk-ai/rtk/blob/develop/docs/guide/resources/savings-explained.md) and the installed version's analytics schema.

## Calculations

For compatible raw and filtered output measurements, reduction is `(raw - filtered) / raw * 100` when raw is greater than zero.
Report zero-denominator ratios as unavailable and increases as increases.
For cumulative counters, use `current - baseline` only when both observations have the same scope and counter lifetime.
Negative deltas require a reset or source-change investigation; they are not negative usage.
Overlapping observations must be deduplicated or presented separately.
Do not add RTK estimates to provider token totals, sum percentages across tools, or apply a vendor's reduction rate to the user's allowance.
Retain enough precision to reproduce the calculation; round only the presentation.

## Quality and recovery

Treat shortened output as a representation whose adequacy needs evidence.
Check complete review diffs, original source, failure diagnostics, and exit status against the task's correctness criteria.
More raw-output recalls may indicate an overly aggressive filter or a harder task; inspect the accompanying evidence before attributing the cause.
Report stale indexes, missed known symbols, incorrect dependency versions, failed adapters, and failed recovery checks explicitly.
A successful setup check establishes integration functionality, not equivalent quality on all future tasks.
An exhausted subscription allowance and a full context window are separate events; report recovery coverage for each only where verified.

## Cheap follow-up measurements

Suggest local read-only command measurements before proposing model-backed comparisons.
When a comparison needs agent runs, state the task and expected additional allowance use and wait for the user's request.
Capture the same acceptance checks and settings for both runs; a single pair is preliminary evidence, not a general guarantee.
