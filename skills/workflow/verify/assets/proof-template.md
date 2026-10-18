# Proof: <what was verified>

- **Verdict:** <proven, failed, or not proven>
- **Work:** <starting commit>..<end commit, or "working tree on <commit>">
- **Agreement:** <where the claims came from>
- **Environment:** <operating system, runtime versions, services, how the application was started>
- **Date:** <YYYY-MM-DD>

## Claims

| # | Claim | Source | Verdict |
| --- | --- | --- | --- |
| C1 | <one observable behavior> | <request, specification, task, or diff> | <proven, failed, unproven, or awaiting human judgment> |

## Evidence

### C1: <claim>

- **Check:** <exact command, script path, or interaction steps>
- **Shown able to fail:** <before and after, or mutation: what was changed and how the check failed>
- **Result:** <output excerpt, exit code, or link to the screenshot or log>
- **Reproduced:** <by whom; match, or what differed>

## Regressions

| Check | Command | Starting commit | End state |
| --- | --- | --- | --- |
| <tests, typecheck, lint, build> | <command> | <pass, fail, or not run> | <pass, fail, or not run> |

## Not proven

<Each claim that is failed, unproven, or awaiting human judgment, with why and what would prove it. Write "None" when every claim is proven.>

## Reproduce

```sh
<commands that rerun every check from a clean checkout>
```

## New files

<Tests and scripts written for this proof, left uncommitted. Write "None" when there are none.>
