# Experimental

These skills are still being evaluated, including workflows for external publication, machine configuration, and AI tooling setup and monitoring.
They are excluded from the plugin and promoted listings, get no documentation pages, and are installed deliberately.
They can change or disappear without warning.

Install one directly:

```bash
npx skills@latest add Dyrits/SKILLS --skill=<name>
```

- **[address-feedback](./address-feedback/SKILL.md)**: Assess every substantive comment on a pull request, merge request, issue, or ticket; implement the approved change plan; then draft and post a reply to each comment.
- **[publish-message](./publish-message/SKILL.md)**: Publish a conclusion or review summary to GitHub, GitLab, or Jira, with optional inline suggestions on a pull or merge request, after the user approves the complete set and destination.
- **[classify](./classify/SKILL.md)**: Sort or tag text with classifier.dev, filter batches before reading them, and keep uncertain results for review; reports confidence or tag scores when available.
- **[setup-delegation-policy](./setup-delegation-policy/SKILL.md)**: Install the delegation and model routing rule (Light, Balanced, Heavy, Frontier tiers, with a per-harness model table) into the global steering files on this machine, and give every harness that binds models per agent one subagent per tier, so every session decides where a task runs and on which model tier.
- **[setup-ai-tooling](./setup-ai-tooling/SKILL.md)**: Configure free project and missing global tools, verify client integrations and complete review evidence, and record a measurement baseline within an explicit setup request.
- **[monitor-ai-tooling](./monitor-ai-tooling/SKILL.md)**: Report tooling usage, output reduction, quality findings, and measurement gaps from existing local data.
