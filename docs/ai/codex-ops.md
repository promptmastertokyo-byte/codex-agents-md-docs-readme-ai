# Codex Operating Notes

These notes expand on `AGENTS.md`. They are not intended to be read on every
turn unless the task touches agent behavior, repository process, or docs design.

## Effective Agent Instructions

Good instructions are:

- Concrete: they say what to do, not only what to value.
- Short: they avoid loading long policy text into every task.
- Local: they describe this repository, not general software practice.
- Verifiable: they point to commands or observable outcomes.

Avoid instructions that require hidden judgment without examples, such as
"write high quality code" or "be careful." Replace them with checks, file
placement rules, and expected command output.

## Working Pattern

1. Read the smallest useful context.
2. Make a focused change.
3. Run verification.
4. Report the changed files and verification result.

## When to Add More Agent Docs

Add a new file under `docs/ai/` only when:

- The rule is too long for `AGENTS.md`.
- The rule applies repeatedly across tasks.
- The rule prevents a real mistake that has happened or is likely.

