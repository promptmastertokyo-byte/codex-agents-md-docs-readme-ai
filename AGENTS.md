# AGENTS.md

This file is the always-read operating guide for Codex agents in this repository.
Keep it short, concrete, and enforceable. Put longer explanations in `docs/ai/`.

## Default Workflow

1. Start from this file. Read `README.md` or `docs/` only when the task
   needs project overview or a specific policy.
2. Prefer small, reversible changes over broad rewrites.
3. Preserve user changes. Never run destructive commands such as
   `git reset --hard`, `git checkout -- <file>`, or `rm -rf` on user work
   unless explicitly asked.
4. Before editing, inspect the nearby files and follow existing style.
5. After editing, run `./scripts/verify.sh` when possible.
6. In the final response, summarize what changed and whether verification passed.

## File Placement

- User-facing project overview: `README.md`
- Human documentation: `docs/development/`
- AI/Codex operating notes: `docs/ai/`
- Temporary local work: `work/`
- User-facing deliverables: `outputs/` (local only, never committed)
- Automation and checks: `scripts/` and `.github/workflows/`

## Editing Rules

- Keep docs concise and scannable.
- Avoid duplicating the same policy across multiple files.
- Do not commit secrets, tokens, private keys, or local machine paths that are not part of the project.
- Prefer ASCII in root docs and scripts. Blog content under `blog/` and the
  blog templates are written in Japanese by design.
- Add comments only when they explain non-obvious intent.

## Verification

Run:

```sh
./scripts/verify.sh
```

The verification script checks repository hygiene for this docs-first setup.
If it fails, fix the cause or explain why it could not be run.
