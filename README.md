# Codex Agents Docs Workspace

This repository is a docs-first workspace for keeping Codex agent instructions,
human onboarding notes, verification habits, and project operations in one
portable structure.

## Quick Start

```sh
./scripts/verify.sh
```

For Codex agents, start with `AGENTS.md`.

For humans, start with:

- `docs/index.md`
- `docs/development/github.md`
- `docs/development/verification.md`
- `docs/development/security.md`
- `docs/ai/github-brain.md`

## Repository Layout

```text
.
├── AGENTS.md                 # Short, always-read agent rules
├── README.md                 # Human-facing entry point
├── docs/
│   ├── index.md              # Documentation map
│   ├── ai/                   # AI/Codex-specific operating notes
│   └── development/          # Human development and operations docs
├── templates/
│   └── github-brain/         # Reusable operational-memory repo template
├── scripts/
│   └── verify.sh             # Local hygiene checks
├── work/                     # Local scratch space, ignored by Git
└── outputs/                  # Per-session deliverables handed to the user.
                              # Local only, ignored by Git. Anything worth
                              # keeping goes to docs/ or its own repository.
```

## Design Principles

- Keep `AGENTS.md` short enough to be followed.
- Separate human docs from AI operating notes.
- Make verification easy to run locally and in CI.
- Avoid storing secrets or machine-specific state in the repository.
- Prefer simple conventions that can be copied into new repositories.
- Treat GitHub as operational memory for AI agents: keep durable lessons in
  versioned docs, and promote only reusable knowledge from project work.
