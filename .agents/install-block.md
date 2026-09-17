# The canonical install block

One install story, one wording. `README.md` and every page under `documentation/` must say **this** and nothing else. Change it here first, then propagate.

The documented route is [skills.sh](https://skills.sh/Dyrits/SKILLS), which copies editable skill files into the project across Claude Code, Codex, and other Agent-Skills-standard harnesses. Use the whole-set form on `README.md`:

<canonical-block name="skills-sh-whole-set">

```bash
npx skills@latest add Dyrits/SKILLS
```

Pick the skills you want, and which coding agents to install them on. **The installer lets you choose which skills to take: make sure `setup-custom-skills` is one of them.**

</canonical-block>

…and the single-skill form wherever one skill is named on its own. Documentation pages do not repeat this block; installation stays in the top-level `README.md`. See [writing-documentation.md](./writing-documentation.md).

<canonical-block name="skills-sh-one-skill">

```bash
npx skills@latest add Dyrits/SKILLS --skill=<name>
```

```bash
npx skills@latest update <name>
```

</canonical-block>

`skills@latest` is the pinned spelling in both. Documentation pages do not carry their own copies of these commands because the top-level `README.md` is the single source of truth.

## Not the install story

`.claude-plugin/marketplace.json` makes the repository its own single-plugin marketplace (`/plugin marketplace add Dyrits/SKILLS`, then `/plugin install dyrits-skills@dyrits`). The plugin is a managed, read-only bundle you subscribe to rather than a fork you own, and installing both routes leaves the user with every skill twice. It is kept as a fallback for installing the repository directly (an unreleased commit, or a private copy) and is **not** documented to users; skills.sh is.
