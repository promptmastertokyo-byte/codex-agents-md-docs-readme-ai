# AGENTS.md

This file is the always-read operating guide for AI agents in this repository.
Keep it short, concrete, and enforceable.

## Default Workflow

1. Read this file first.
2. Read `README.md` or `docs/` only when the task needs more context.
3. Preserve user changes and avoid broad rewrites.
4. Before editing, inspect nearby files and follow existing style.
5. After editing, run `./scripts/verify.sh` when possible.
6. Report changed files, verification results, and any instruction differences.

## Memory Rules

- Project-specific notes stay in the project repository.
- Reusable lessons go in `docs/learnings/`.
- Reusable prompts or skeletons go in `templates/`.
- Machine setup and recovery notes go in `docs/setup/`.
- Do not commit secrets, tokens, private keys, or `.env` contents.

## Close Rule

Do not close work with "reflect later." Reflect, promote, verify, then close.

