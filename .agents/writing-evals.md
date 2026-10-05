# Writing evaluations

Test cases for the promoted skills, kept in each skill's own folder where `skill-creator` looks for them:

```
skills/<bucket>/<skill-name>/evals/evals.json
skills/<bucket>/<skill-name>/evals/files/   (only when an eval needs input files)
```

The format follows the `skill-creator` schema (`skill_name`, `evals[]` with `id`, `prompt`, `expected_output`, `files`, `expectations`), so its runner, grader, and viewer read these files unchanged. One field is added: `kind`.

```json
{
  "skill_name": "memorize",
  "evals": [
    {
      "id": 1,
      "kind": "trigger",
      "prompt": "From now on, always run the formatter before committing.",
      "expected_output": "The agent routes the rule to the project's instruction file.",
      "expectations": [
        "The memorize skill is invoked",
        "The rule is written to the nearest CLAUDE.md or AGENTS.md, not only to personal memory"
      ]
    }
  ]
}
```

## Kinds

Every skill carries at least three evals, one of each kind:

| Kind | The prompt | Passes when |
| --- | --- | --- |
| `trigger` | Reads like a real request that matches the description, and never names the skill | The skill fires from its description alone |
| `behavior` | Names the skill, or follows a trigger, and sets up the situation its steps handle | The expectations about its steps, outputs, and stops hold |
| `no-trigger` | A near miss: shares vocabulary with the skill but belongs elsewhere | The skill does not fire, and the expectations name what handles the request instead |

Add more of any kind where a skill has more branches, a known failure, or a step agents tend to skip.

## Writing an eval

- **Prompts are self-contained.** Describe the situation inside the prompt, or ship a fixture under `files/` and list it in `files` (paths relative to the skill folder, so `evals/files/<name>`). Never depend on the repository an eval is run from.
- **Expectations are observable.** Each states one thing a grader can confirm from the transcript or the resulting files: "the skill asks one question before writing", not "the agent understands the problem". Include at least two.
- **Cover the steps.** For a `behavior` eval, expectations track the skill's own steps and completion criteria, including each approval gate it must stop at.
- **Stay public.** Use invented names, projects, and content. The repository is public.
- **Run in scratch.** Skills with outward effects (publishing, pushing, installing) are evaluated in a throwaway repository with no real remote or credentials; the expectations check the proposed action, not a live one.

## Checks

`python3 scripts/check-skills.py` requires an `evals/evals.json` for every promoted skill and checks it: `skill_name` matches the directory, ids are unique integers, at least three evals cover all three kinds, every eval has a prompt, an expected output, and at least two expectations, and every listed file exists.

## Running them

Use the `skill-creator` skill: it spawns a with-skill run and a baseline run per eval, grades the expectations, and opens the viewer. It reads `evals/evals.json` in the skill folder as is. The `claude plugin eval` runner uses a different layout (one directory per case under the plugin's `evals/`) and does not read these files.
