# Documentation Index

Use this page as the map for the repository.

## Human-Facing Docs

- `docs/development/github.md` - branch, pull request, CI, and backup policy
- `docs/development/security.md` - permissions, secrets, and dependency review
- `docs/development/verification.md` - local and CI verification loop
- `docs/development/multi-device-workflow.md` - working from phone and PC together
- `docs/development/blog-workflow.md` - blog draft cycle and WordPress publishing

## AI-Facing Docs

- `docs/ai/codex-ops.md` - how Codex should work in this repository
- `docs/ai/context-budget.md` - context and token efficiency rules
- `docs/ai/github-brain.md` - template for GitHub as AI operational memory
- `docs/ai/mcp.md` - MCP configuration principles

## Templates

- `templates/github-brain/` - reusable skeleton for a self-running AI memory repo
- `templates/blog-post.md` - full article template for a new blog draft
- `templates/blog-specialized-repo/` - reusable skeleton for a blog-only repo
- `blog/style-guide.md` - blog writing, review, publishing, and improvement guide

## Reading Order

For routine work:

1. `AGENTS.md`
2. The smallest relevant doc under `docs/` (skip `README.md` unless the
   task needs project overview)

For repository setup or audits:

1. `README.md`
2. `docs/index.md`
3. All files under `docs/development/`
4. All files under `docs/ai/`

## Adding Categories

When adding a new directory under `docs/`, add exactly one line for it in
this index. Do not duplicate its contents here.
