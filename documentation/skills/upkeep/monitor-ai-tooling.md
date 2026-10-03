Fork-created skill, no upstream equivalent: added in commit `1394bed`, as recorded in [the retained skill provenance research](../../research/2026-10-03-retained-skill-provenance.md).

## What it does

`monitor-ai-tooling` writes an on-demand report on AI tooling usage, measured output reduction, quality signals, and gaps, built only from measurements that already exist locally.

Collection stays deterministic: it does not install tools, change configuration, or start recurring model analysis. Anything unmeasured stays **unknown**, and the report never invents a total savings figure.

## When to reach for it

Type `/monitor-ai-tooling`, optionally naming a project and period. It is user-invoked: the agent does not run it automatically.

| Your situation | Skill |
| --- | --- |
| Find out whether the configured tools are used and helping | This one |
| Install or change the tools, hooks, or measurement setup | [setup-ai-tooling](../getting-started/setup-ai-tooling.md) |
| Report how the skills behaved in a session | [improve-skills](improve-skills.md) |

## Prerequisites

It reads `documentation/agents/ai-tooling.md` if present, plus whatever measurement sources exist: tool analytics, saved verification results, or an export from your existing monitor. With nothing available it still produces a gaps report and says how `/setup-ai-tooling` or a future measurement period can fill them.

## Measurement discipline

The skill compares counters only across the same source, scope, schema, and counter lifetime, and accounts for resets, upgrades, and overlapping clients.

| Kind of evidence | How it is reported |
| --- | --- |
| Provider or monitor export | Actual token usage, with provider, model, window, and account scope |
| Command-output reduction (for example RTK) | Byte reduction; token figures are byte-based estimates, never provider counts |
| Local command observations | Duration, output bytes, exit status for that command only |
| Task comparisons | Only with the same task, scope, settings, and acceptance criteria |
| Published benchmarks | Labelled external, excluded from personal totals |

Shortened output is treated as a representation whose adequacy needs evidence. A protected-command bypass that is unverified is a quality finding even when output reduction looks good.

## Common questions

**No observations were found. Was the tool unused?**

Unknown. No data is not proof of no use; the report says so and names the measurement that would settle it.

**Can I add up the savings across tools?**

No. Percentages are not summed across tools, estimates are not added to provider totals, and a vendor's reduction rate is not applied to your allowance.

**Does it call a model or the network?**

It prefers local collection with no network requests and no additional model calls. A model-backed comparison is only proposed, with its expected cost, and waits for your request.

## It's working if

- A dated report appears under `.agents/tooling/reports/` (or your chosen destination) with a row for every configured tool.
- Every figure traces to a source with provenance, unit, period, and scope, or is marked unknown.
- Gaps and next measurements are specific, and the closing summary gives the report path.
- Nothing on your machine changed other than the report file.

## Where it fits

Periodic maintenance after [setup-ai-tooling](../getting-started/setup-ai-tooling.md): setup configures the tools, this checks whether they pay off. [improve-skills](improve-skills.md) is the neighbor for the skills themselves. [guide](../getting-started/guide.md) maps the wider flow.
