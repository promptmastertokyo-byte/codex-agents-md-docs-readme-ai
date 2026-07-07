# Workflow

This repository supports an AI collaboration loop:

1. Human defines the goal.
2. Design agent expands options and writes a clear handoff.
3. Implementation or review agent executes the task.
4. Verification runs locally and in CI when available.
5. Reusable learning is promoted into this repository.

## Handoff Minimum

- objective
- current state
- files to read
- decisions already made
- open questions
- verification commands
- requested review angle, when relevant

## Report Minimum

- changed files, including deletions and moves
- verification result, with command output summary
- differences from the instruction
- points that should improve the next handoff

