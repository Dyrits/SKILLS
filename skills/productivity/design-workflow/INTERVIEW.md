# Interview method

Interview the user until you reach a shared understanding of the selected scope. Map it as a **design tree**: every decision branches into the decisions that depend on it.

Work the tree in **rounds**. The **frontier** contains every unresolved decision whose prerequisites are settled. Ask the whole frontier, number each question, and give your recommended answer. Then wait for the user's answers.

```text
❓ **Q1** - **<question title>**: <question and choices>

➡️ <recommended answer>

---

❓ **Q2** - **<question title>**: <question and choices>

➡️ <recommended answer>
```

Recompute the frontier after each round. A question that depends on an unresolved answer belongs to a later round. Reuse settled decisions instead of interviewing again. Bound the tree to the selected question or scope, not the entire future product.

Find facts from the environment yourself, delegating exploration when available. An exploration in progress is an unsettled prerequisite: only downstream questions wait, while independent questions proceed. Decisions belong to the user; present them and wait rather than supplying unapproved answers.

Finish when the selected frontier is empty and the user confirms the shared understanding. Surface unresolved blockers explicitly. Confirmation of understanding is not authorization to implement or publish.
