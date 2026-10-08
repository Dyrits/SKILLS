---
name: improve-codebase-architecture
description: "Scan a codebase for deepening opportunities, present them as a visual HTML report, then interview through the chosen one. Use when the user wants architecture improvements or refactoring candidates found."
metadata:
  forks: "mattpocock/skills/skills/engineering/improve-codebase-architecture"
---

# Improve Codebase Architecture

Surface architectural friction and propose **deepening opportunities**: refactors that turn shallow modules into deep ones. The aim is testability and AI-navigability.

This command is _informed_ by the project's domain model and built on a shared design vocabulary:

- [MODULES.md](MODULES.md) holds the architecture vocabulary (**module**, **interface**, **depth**, **seam**, **adapter**, **leverage**, **locality**) and its principles (the deletion test, "the interface is the test surface", "one adapter = hypothetical seam, two = real"). Use these terms exactly in every suggestion, and don't drift into "component," "service," "API," or "boundary."
- The domain language in the glossary gives names to good seams; decision records record decisions this command should not re-litigate.

## Process

### 1. Explore

**Scope before you scan: YAGNI.** Deepening a module pays off by making future changes to it easier, so put extra weight on the parts of the codebase that have recently changed. Decide *where* to look before you look:

- If the user named a direction (a module, a subsystem, a pain point), take it, and skip the inference below.
- Otherwise, walk back a good stretch of the commit history (`git log --oneline`) to find the codebase's hot spots, the files and areas that keep coming up, and let those paths pull your attention first. If the changes are scattered with no clear hot spot, widen the net.

Read the project's glossary, the decision records in the area you're touching, and the conventions file first, when `AGENTS.md` points to them; mention a likely one it does not name in the report instead of using it.
When it is missing, scan without project conventions and say so in the report.

Then spawn a sub-agent to walk the codebase. Don't follow rigid heuristics; explore organically and note where you experience friction:

- Where does understanding one concept require bouncing between many small modules?
- Where are modules **shallow**, with an interface nearly as complex as the implementation?
- Where have pure functions been extracted just for testability, but the real bugs hide in how they're called (no **locality**)?
- Where do tightly-coupled modules leak across their seams?
- Which parts of the codebase are untested, or hard to test through their current interface?

Apply the **deletion test** to anything you suspect is shallow: would deleting it concentrate complexity, or just move it? A "yes, concentrates" is the signal you want.

### 2. Present candidates as an HTML report

Write a self-contained HTML file to `documentation/architecture-audit/` in the repository (create the directory lazily if missing, and when you create it, add one line to the nearest `AGENTS.md` saying it holds architecture audit reports), filename `architecture-audit-<timestamp>.html` so each run gets a fresh file and history accumulates. Open it for the user (`xdg-open <path>` on Linux, `open <path>` on macOS, `start <path>` on Windows) and tell them the path relative to the repository root.

The report uses **Tailwind via CDN** for layout and styling, and **Mermaid via CDN** for diagrams where a graph/flow/sequence reliably communicates the structure. Mix Mermaid with hand-crafted CSS/SVG visuals: use Mermaid when relationships are graph-shaped (call graphs, dependencies, sequences), and hand-built divs/SVG when you want something more editorial (mass diagrams, cross-sections, collapse animations). Each candidate gets a **before/after visualisation**. Be visual.

For each candidate, render a card with:

- **Files**: which files/modules are involved
- **Problem**: why the current architecture is causing friction
- **Solution**: plain English description of what would change
- **Benefits**: explained in terms of locality and leverage, and how tests would improve
- **Before / After diagram**: side-by-side, custom-drawn, illustrating the shallowness and the deepening
- **Recommendation strength**: one of `Strong`, `Worth exploring`, `Speculative`, rendered as a badge

End the report with a **Top recommendation** section: which candidate you'd tackle first and why.

**Use the glossary's vocabulary for the domain, and the [MODULES.md](MODULES.md) vocabulary for the architecture.** If the glossary defines "Order," talk about "the Order intake module," not "the FooBarHandler," and not "the Order service."

**Decision record conflicts**: if a candidate contradicts an existing decision record, only surface it when the friction is real enough to warrant revisiting the record. Mark it clearly in the card (e.g. a warning callout: _"contradicts decision record 0007, but worth reopening because…"_). Don't list every theoretical refactor a record forbids.

See [HTML-REPORT.md](HTML-REPORT.md) for the full HTML scaffold, diagram patterns, and styling guidance.

Do NOT propose interfaces yet. After the file is written, ask the user: "Which of these would you like to explore?"

### 3. Refinement loop

Once the user picks a candidate, walk the decision tree with them following the [interview method](INTERVIEW.md): constraints, dependencies, the shape of the deepened module, what sits behind the seam, what tests survive.

Side effects happen inline as decisions crystallize:

- **Naming a deepened module after a concept not in the glossary, or a term turns out fuzzy?** Settle it right there: name the conflict, test it with a concrete scenario, recommend a canonical term, and once the user agrees, write it to the glossary following [GLOSSARY-FORMAT.md](GLOSSARY-FORMAT.md).
- **User rejects the candidate with a load-bearing reason?** Offer a decision record, framed as: _"Want me to record this as a decision record so future architecture reviews don't re-suggest it?"_ On yes, write it following [DECISION-RECORD-FORMAT.md](DECISION-RECORD-FORMAT.md). Only offer when the reason would actually be needed by a future explorer to avoid re-suggesting the same thing; skip ephemeral reasons ("not worth it right now") and self-evident ones.
- **Want to explore alternative interfaces for the deepened module?** Use the parallel sub-agent pattern in [DESIGN-IT-TWICE.md](DESIGN-IT-TWICE.md).
- **Deepening a cluster given its dependencies?** Follow [DEEPENING.md](DEEPENING.md) for dependency categories, seam discipline, and testing.
