# Context and Token Budget

This repository is designed to keep always-loaded context small.

## Static Cost

Static cost is the content an agent must read before doing useful work.

Keep static cost low by:

- Keeping `AGENTS.md` short.
- Moving long rationale into `docs/ai/`.
- Using `docs/index.md` as a map instead of duplicating summaries everywhere.
- Avoiding large generated files in tracked docs.

## Dynamic Cost

Dynamic cost is the number of tool calls and back-and-forth turns needed to
complete a task.

Keep dynamic cost low by:

- Providing verification commands.
- Keeping file placement predictable.
- Naming docs by purpose.
- Recording decisions once, near the relevant workflow.

## Practical Limits

- `AGENTS.md` should stay under roughly 150 lines.
- Each operational doc should prefer one topic per file.
- If a doc becomes a reference manual, add a short summary and table of contents.

