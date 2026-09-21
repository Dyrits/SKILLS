# Waza

Generated on 2026-09-21 with `waza` 0.38.7, one `waza check <skill>` run per skill directory under `skills/`, all 38 of them.

## Summary

| Metric | Result |
| --- | --- |
| Skills checked | 38 |
| Parse failures | 0 (`getting-started/what-is-next` failed initially; fixed during this pass) |
| Overall verdict "ready for submission" | 0 |
| Overall verdict "needs some work" | 38 |
| Compliance score Low / Medium / High | 37 / 1 (`reference/wizard`) / 0 |
| Spec compliance 9/9 | 12 |
| Within waza's 500-token limit | 10 |
| Over the token limit | 28 |
| Evaluation suite (`eval.yaml`) found | 0 |

Every skill that parsed returns "needs some work before submission". The recurring causes, in order of impact:

1. **Token budget.** 27 of 37 parsed skills exceed waza's hard limit of 500 tokens. The largest: `shaping/wayfinder` (2715), `reference/writing-for-agents` (2349), `getting-started/setup-custom-skills` (2323), `productivity/teach` (1946), `upkeep/debug` (2001).
2. **Unknown frontmatter fields** against the agentskills.io spec: `disable-model-invocation` in 21 skills (a deliberate convention here, see `.agents/invocation.md`) and `argument-hint` in 8 skills. One security advisory on top: `experimental/classify`, whose `argument-hint` value contains XML angle brackets.
3. **Compliance score Low.** waza wants explicit `USE FOR:` / `DO NOT USE FOR:` trigger sections and routing labels; these skills describe triggers in prose instead.
4. **No eval suites.** No skill in the repository has an `eval.yaml`, so none can be benchmarked with `waza run`.

## Parse failure, fixed

`getting-started/what-is-next` initially failed before any check ran:

```
parsing SKILL.md: parsing frontmatter: unmarshalling frontmatter: yaml: line 2: mapping values are not allowed in this context
```

Cause: the `description:` value was an unquoted scalar containing a colon plus space ("Figure out the next move: which skill or flow fits ..."), which is invalid YAML. The value is now double-quoted, matching the convention of the other skills whose descriptions contain colons. Re-running `waza check` after the fix gives the row below.

## Per-skill results

Tokens are measured against waza's default hard limit of 500. "Spec issues" lists the agentskills.io spec check failures only.

| Skill | Compliance | Spec checks | Tokens | Spec issues | Eval suite |
| --- | --- | --- | --- | --- | --- |
| experimental/address-feedback | Low | 8/9 | 1153 | unknown fields: `argument-hint`, `disable-model-invocation` | missing |
| experimental/classify | Low | 7/9 | 791 | unknown field `argument-hint`; security: angle brackets in `argument-hint` | missing |
| experimental/publish-message | Low | 8/9 | 1006 | unknown fields: `argument-hint`, `disable-model-invocation` | missing |
| experimental/publish-review | Low | 8/9 | 838 | unknown fields: `argument-hint`, `disable-model-invocation` | missing |
| experimental/setup-delegation-policy | Low | 8/9 | 1273 | unknown field `disable-model-invocation` | missing |
| getting-started/setup-auto-handoff | Low | 9/9 | 785 | none | missing |
| getting-started/setup-custom-skills | Low | 8/9 | 2323 | unknown field `disable-model-invocation` | missing |
| getting-started/setup-git-guardrails | Low | 9/9 | 1186 | none | missing |
| getting-started/setup-git-hooks | Low | 9/9 | 1624 | none | missing |
| getting-started/what-is-next | Low | 8/9 | 3489 | unknown field `disable-model-invocation` | missing |
| productivity/ask-someone-else | Low | 8/9 | 638 | unknown field `disable-model-invocation` | missing |
| productivity/grill-me | Low | 8/9 | 36 | unknown field `disable-model-invocation` | missing |
| productivity/hand-off | Low | 8/9 | 359 | unknown fields: `argument-hint`, `disable-model-invocation` | missing |
| productivity/take-over | Low | 8/9 | 470 | unknown fields: `argument-hint`, `disable-model-invocation` | missing |
| productivity/teach | Low | 8/9 | 1946 | unknown fields: `argument-hint`, `disable-model-invocation` | missing |
| productivity/wait-what | Low | 8/9 | 149 | unknown field `disable-model-invocation` | missing |
| reference/codebase-design | Low | 9/9 | 1349 | none | missing |
| reference/domain-modeling | Low | 9/9 | 804 | none | missing |
| reference/grilling | Low | 9/9 | 420 | none | missing |
| reference/wizard | Medium | 9/9 | 957 | none | missing |
| reference/writing-for-agents | Low | 9/9 | 2349 | none | missing |
| shaping/prototype | Low | 9/9 | 642 | none | missing |
| shaping/research | Low | 9/9 | 169 | none | missing |
| shaping/wayfinder | Low | 8/9 | 2715 | unknown field `disable-model-invocation` | missing |
| upkeep/debug | Low | 9/9 | 2001 | none | missing |
| upkeep/improve-agent-environment | Low | 8/9 | 973 | unknown field `disable-model-invocation` | missing |
| upkeep/improve-codebase-architecture | Low | 8/9 | 1334 | unknown field `disable-model-invocation` | missing |
| upkeep/resolve-merge-conflicts | Low | 9/9 | 204 | none | missing |
| upkeep/triage | Low | 8/9 | 1866 | unknown field `disable-model-invocation` | missing |
| workflow/code-review | Low | 9/9 | 1659 | none | missing |
| workflow/design-workflow | Low | 8/9 | 575 | unknown fields: `argument-hint`, `disable-model-invocation` | missing |
| workflow/grill-with-documentation | Low | 8/9 | 60 | unknown field `disable-model-invocation` | missing |
| workflow/implement-all | Low | 8/9 | 437 | unknown field `disable-model-invocation` | missing |
| workflow/implement | Low | 8/9 | 98 | unknown field `disable-model-invocation` | missing |
| workflow/test-driven-development | Low | 9/9 | 757 | none | missing |
| workflow/to-pull-request | Low | 9/9 | 1046 | none | missing |
| workflow/to-specifications | Low | 8/9 | 854 | unknown field `disable-model-invocation` | missing |
| workflow/to-tickets | Low | 8/9 | 1584 | unknown field `disable-model-invocation` | missing |

## How to read this

waza grades against the agentskills.io submission spec: allowed frontmatter fields only, a 500-token hard limit, explicit trigger sections, and an eval suite per skill. This repository deliberately deviates from some of that (`argument-hint`, `disable-model-invocation`, prose-style bodies without `USE FOR:` blocks, and reference skills that are intentionally longer than 500 tokens), so treat the Low scores as "distance from the agentskills.io submission bar" rather than a list of defects. The findings that do point at real problems:

- The `what-is-next` YAML parse error (waza could not read the file at all, and any tool parsing that frontmatter strictly hit the same wall). Fixed by quoting the `description` value.
- The angle-bracket security advisory on `classify`.
- Zero eval coverage: nothing in this repository can currently be regression-tested with `waza run`.

## Reproduce

```sh
for f in $(find skills -name SKILL.md | sort); do waza check "$(dirname "$f")"; done
```
