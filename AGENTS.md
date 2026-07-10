# AGENTS.md

This file is the always-read operating guide for Codex agents in this repository.
Keep it short, concrete, and enforceable. Put longer explanations in `docs/ai/`.

## Default Workflow

1. Start from this file. Read `README.md` or `docs/` only when the task needs project overview or a specific policy.
2. Prefer small, reversible changes over broad rewrites.
3. Preserve user changes. Never run destructive commands such as `git reset --hard`, `git checkout -- <file>`, or `rm -rf` on user work unless explicitly asked.
4. Before editing, inspect nearby files and follow existing style.
5. After editing, run `./scripts/verify.sh` when possible.
6. In the final response, summarize changed files and whether verification passed.

## Task Routing

- Agent behavior or repository process: `docs/ai/codex-ops.md`
- Context and token efficiency: `docs/ai/context-budget.md`
- Editorial roles and approval gates: `docs/ai/team-roles.md`
- MCP configuration: `docs/ai/mcp.md`
- Blog production and WordPress drafts: `docs/development/blog-workflow.md`
- Security, permissions, or external tools: `docs/development/security.md`
- Branches, pull requests, and CI: `docs/development/github.md`
- Verification changes or failures: `docs/development/verification.md`

Read only the smallest relevant set.

## File Placement

- User-facing project overview: `README.md`
- Human documentation: `docs/development/`
- AI operating notes: `docs/ai/`
- Temporary local work: `work/`
- User-facing deliverables: `outputs/` (local only, never committed)
- Automation and checks: `scripts/` and `.github/workflows/`

## Safety and Approval

- Do not commit secrets, tokens, private keys, passwords, or machine-specific credentials.
- Prefer repository-local commands and read-only access.
- Use a branch and pull request for durable changes when practical.
- No AI may approve and merge its own pull request.
- Public publishing, destructive actions, permission expansion, and external writes require explicit human authorization.
- For editorial work, follow `docs/ai/team-roles.md`.

## Editing Rules

- Keep docs concise and scannable.
- Avoid duplicating the same policy across multiple files.
- Prefer ASCII in root docs and scripts. Blog content and blog templates are Japanese by design.
- Add comments only when they explain non-obvious intent.

## Verification

Run:

```sh
./scripts/verify.sh
```

If verification fails, fix the cause or clearly explain why it could not be run.
