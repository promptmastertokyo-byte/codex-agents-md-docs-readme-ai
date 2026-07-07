# GitHub Brain Template

Use `templates/github-brain/` when a repository should act as operational
memory for AI agents.

## Purpose

The repository is not only storage. It is the durable memory that Claude,
Codex, local LLMs, and future agents can read before acting.

## Core Loop

1. Capture project work in the project repository.
2. Record concrete lessons in `docs/learnings/`.
3. Promote only reusable knowledge into playbooks, templates, skills, or
   dotfiles.
4. Verify the repository before closing the loop.

## What Belongs Here

- Stable operating rules.
- Review templates and handoff contracts.
- Lessons that changed future behavior.
- Machine setup instructions that can be recreated.
- Links to external systems, not copied private content.

## What Stays Out

- Secrets, tokens, private keys, and `.env` contents.
- Raw client data unless the repository is explicitly scoped for it.
- One-off notes that do not improve future agent behavior.
- Large generated outputs that are better kept in `outputs/` or artifacts.

## Self-Running Contract

A GitHub brain repo should always have:

- `AGENTS.md` for short always-read rules.
- `README.md` for human orientation.
- `docs/index.md` for the map.
- `docs/learnings/` for experience records.
- `templates/` for reusable prompts or repo skeletons.
- `scripts/verify.sh` for local and CI checks.

