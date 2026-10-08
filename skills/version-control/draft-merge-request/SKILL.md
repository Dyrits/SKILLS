---
name: draft-merge-request
description: "Write the body of a pull request or merge request: a summary visual, before/after evidence, and the merge danger. Use when opening one, when writing or rewriting its description, or when a reviewer needs to see what a change does without reading the diff."
metadata:
  forks: "mattpocock/skills/skills/engineering/pr"
---

Use this template for the body:

```markdown
## Summary

<call tree, component tree, file tree, pseudocode, diff sketch, or Mermaid diagram>

## Evidence

- **Before:** <screenshot, output, or failing test run>
  **After:** <screenshot, output, or passing test run>

## Merge danger

**Door:** <one-way or two-way>

<optional: what makes it that>

**Blast radius:** <one-word scope>

<optional: what a bad merge reaches>
```

Everything here applies unchanged to a merge request on GitLab.

Skip preambles and keep prose brief. Write it in the language its primary source already uses, the ticket or specification the change came from, with the project's domain terms from the glossary `AGENTS.md` points to.

## Summary

Why the change exists comes from its primary source. The diff decides which **shape** shows it, never what it was for.

Choose and render the Summary visual following [SUMMARY-VISUAL.md](SUMMARY-VISUAL.md), using the primary source for intent and the diff for structure.
Render it inline in Markdown, so it shows in the pull or merge request body.

## Evidence

Concrete proof the change works, as a before and after pair.

A screenshot is the best evidence there is, wherever the change is visual and the environment can produce one. Execution comes next: a test run, console output, the exact test that went from failing to passing, sketched as pseudocode rather than pasted in full.

## Merge danger

**Door** is whether the merge is reversible. You walk back through a two-way door; a one-way door you do not. A change that is cheap to roll back is low risk, and one carrying a destructive action or a hard-to-reverse decision is not.

**Blast radius** is how far a bad merge reaches. Name it in one word, then say what it touches if the one word hides something: layout shift, breakage for consumers, mobile responsiveness, a migration that runs on deploy.
