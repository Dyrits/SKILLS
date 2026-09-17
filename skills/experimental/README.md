# Experimental

These skills take real, externally visible actions: posting a comment on a pull request, a merge request, or an issue tracker. They're excluded from the plugin and the top-level `README.md` until they've proven themselves; they get no documentation pages, and they can change or disappear without warning.

Install one directly:

```bash
npx skills@latest add Dyrits/SKILLS --skill=<name>
```

- **[address-feedback](./address-feedback/SKILL.md)**: Assess every substantive comment on a pull request, merge request, issue, or ticket; implement the approved change plan; then draft and post a reply to each comment.
- **[publish-message](./publish-message/SKILL.md)**: Post a short, `[AI]`-prefixed comment to a GitHub/GitLab pull/merge request or a Jira issue, leading with the why rather than restating the diff or ticket.
- **[publish-review](./publish-review/SKILL.md)**: Publish a finished `/code-review` report to the tracker: judgement calls and cross-cutting findings as one `[AI]`-prefixed summary comment, concretely fixable findings as inline suggested changes on GitHub or GitLab.
