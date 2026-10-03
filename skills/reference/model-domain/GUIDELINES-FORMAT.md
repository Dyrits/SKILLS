# GUIDELINES.md Format

`GUIDELINES.md` holds the project's judgement-call rules: what its reviewers and architects apply and no tool can enforce. `review-and-refactor` and `improve-codebase-architecture` read it; `memorize` files new rules into it.

## Offer

Check `documentation/agents/domain.md` first. When it records `Guidelines: declined`, return to the caller without asking.
Otherwise ask whether to create `GUIDELINES.md` now. On yes, run the interview below; on no, record the decline (see Declining) and return.

## Interview

The calling skill passes a focus: **code** (review) or **architecture** (audit). Ask one question at a time, lead with a recommended answer, and take the user's rules in their own words.

- **Code**: naming, structure and file layout, error handling, testing style, patterns the team bans or prefers, what reviewers repeatedly flag.
- **Architecture**: layering and dependency direction, module layout, where seams belong, testing approach, what the team never wants coupled.

You may draft candidate rules from the codebase to speed this up. Present them one at a time, and keep each only once the user confirms it and gives its reason in their own words. For each rule, ask why it exists. A rule without a reason is the first to be misapplied.

## Structure

```md
# Guidelines

## {Topic}

- **{Rule}**: {the reason it exists, and the case it does not cover}
```

## Rules

- **Judgement calls only.** A rule a linter, formatter, hook, or CI job could check belongs in that tool. Offer to wire it there instead of writing it down.
- **Cache only what the agent cannot find by looking.** Skip anything already visible in configuration, scripts, or the directory layout.
- **One meaning, one place.** Link to architecture decision records and `GLOSSARY.md` instead of restating them.
- **Create lazily.** Write the file when the first rule is agreed, not as an empty scaffold.

## Declining

When the user declines, record `Guidelines: declined` under the Guidelines heading of `documentation/agents/domain.md` (skip when that file does not exist), so later runs do not ask again. Writing a rule later removes the line.
