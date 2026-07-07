# {{REPO_NAME}}

This repository is the operational memory for AI-assisted work.

It keeps reusable rules, handoff contracts, review templates, learning records,
and setup notes in a form that Claude, Codex, local LLMs, and future agents can
read.

## Operating Principle

Keep project-specific experience in the project repository. Promote only
reusable knowledge into this repository.

## Start Here

- `AGENTS.md` - short agent rules
- `docs/index.md` - documentation map
- `docs/learnings/index.md` - learning records
- `templates/` - reusable prompts and skeletons
- `scripts/verify.sh` - local hygiene check

## Core Loop

1. Create or update a project repository.
2. Run design, implementation, review, and verification there.
3. Record concrete lessons in that project.
4. Promote reusable lessons here.
5. Run `./scripts/verify.sh`.

