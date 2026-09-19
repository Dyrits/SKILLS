# Experimental

These skills take real, externally visible actions: posting a comment on a pull request, a merge request, or an issue tracker, or sending your text to a third-party API. They're excluded from the plugin and the top-level `README.md` until they've proven themselves; they get no documentation pages, and they can change or disappear without warning.

Install one directly:

```bash
npx skills@latest add Dyrits/SKILLS --skill=<name>
```

- **[address-feedback](./address-feedback/SKILL.md)**: Assess every substantive comment on a pull request, merge request, issue, or ticket; implement the approved change plan; then draft and post a reply to each comment.
- **[publish-message](./publish-message/SKILL.md)**: Post a short, `[AI]`-prefixed comment to a GitHub/GitLab pull/merge request or a Jira issue, leading with the why rather than restating the diff or ticket.
- **[publish-review](./publish-review/SKILL.md)**: Publish a finished `/code-review` report to the tracker: judgement calls and cross-cutting findings as one `[AI]`-prefixed summary comment, concretely fixable findings as inline suggested changes on GitHub or GitLab.
- **[classify](./classify/SKILL.md)**: Classify text against your own labels with classifier.dev, a keyless HTTP API that returns a calibrated confidence per verdict: triage, filter or bucket many items without reading each one, or decide between named options.
- **[dispatch](./dispatch/SKILL.md)**: Bind a route recommendation (task type, complexity), normally supplied automatically by `setup-auto-route`'s hook, to the subagent that fits, brief it, and dispatch, so a classifier picks the agent and its pinned model rather than the agent's own judgement.
