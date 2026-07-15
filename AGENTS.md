# AGENTS.md

This file is the always-read operating guide for Codex agents in this repository.
Keep it short, concrete, and enforceable. Put longer explanations in `docs/ai/`.

## Default Workflow

1. Read this file, then check the Notion operating hub links in `README.md` when the task depends on current priorities, KPI, deadlines, or approval state.
2. Work only on items selected as `今週` or explicitly requested by the user.
3. Prefer small, reversible changes over broad rewrites.
4. Preserve user changes. Never run destructive commands such as `git reset --hard`, `git checkout -- <file>`, or `rm -rf` on user work unless explicitly asked.
5. Before editing, inspect nearby files and follow existing style.
6. After editing, run `./scripts/verify.sh` when possible.
7. Summarize changed files, verification, and anything waiting for user approval.

## Sources of Truth

- Notion: priorities, tasks, KPI, deadlines, effect-review dates, and approval state.
- GitHub: versioned article drafts, reviews, scripts, operating rules, and WordPress/theme changes.
- WordPress: draft preview and published content.
- The user's current instruction overrides stored operating notes when they conflict.

Do not duplicate full article bodies in Notion and GitHub. Keep task/KPI context in Notion and versioned content in GitHub; link the two records.

## AI Team Roles

| Actor | Role | Main responsibility |
| --- | --- | --- |
| ChatGPT Work | 編集長・運用OS | Notion週次運用、企画、優先順位、下書き、SEO/YMYL監査、KPIレビュー |
| Codex | GitHub実行担当 | 記事・スクリプト・WordPressテーマの差分、検証、Issue、Pull Request |
| Claude / Claude Code | 任意の制作支援 | 追加執筆・レビュー。既存ルールとNotionの優先順位に従う |
| 本人 | 最終責任者 | 実体験・実数、公開承認、WordPress公開、本番マージ |

Work or Codex may move a prepared item to `本人確認`, but must never enable `公開承認` or publish externally without an explicit user instruction.

## Blog Workflow

- Ideas: `blog/ideas/`
- Briefs: `blog/briefs/`
- Drafts and rewrites: `blog/drafts/`
- Reviews: `blog/reviews/`
- Published URL and update history: `blog/published/`
- Search Console / Analytics snapshots: `blog/metrics/`
- Improvement plans and results: `blog/improvements/`
- Durable wins and failures: `docs/playbook.md` when available

When personal experience is missing, insert `【体験談ここ】`; never invent it.

## File Placement

- User-facing project overview: `README.md`
- Human documentation: `docs/development/`
- AI/Codex operating notes: `docs/ai/`
- Temporary local work: `work/`
- User-facing deliverables: `outputs/` (local only, never committed)
- Automation and checks: `scripts/` and `.github/workflows/`

## Safety and Publishing

- Never commit secrets, tokens, Application Passwords, private keys, or real `.env` values.
- WordPress automation may create `draft` posts only.
- External publication, SNS posting, deletion, URL migration, plugin/theme updates, payments, permission changes, and production merges require explicit user approval.
- For tax, investment, legal, medical, or other YMYL content, verify current official primary sources immediately before publication.

## Verification

Run:

```sh
./scripts/verify.sh
```

If verification fails, fix the cause or clearly report why it could not run.

