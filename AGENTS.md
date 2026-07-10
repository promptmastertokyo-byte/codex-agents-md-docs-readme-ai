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

## AI Team Roles

| AI | 役割 | 担当ディレクトリ |
|---|---|---|
| Claude (chat) | 編集長: 企画判断、タイトル・構成レビュー、公開前最終レビュー、metrics分析、playbook昇格 | ideas->briefs, reviews/, improvements/, playbook |
| Claude Code | 執筆〜WP下書き: new-post.sh実行、本文執筆・リライト、verify、PR、publish-wordpress.py実行 | drafts/, scripts/実行 |
| Codex | インフラ: スクリプト保守、verify拡張、技術リスク検証 | scripts/, .github/ |
| GPT | 外部視点: タイトル案の別視点、第三者レビュー | reviews/への意見のみ(直接編集なし) |
| Gemini | リサーチ(無料枠): 公式情報・統計の裏取り | 成果物は人間がideas/briefsに転記 |
| Grok | Xトレンド検出(無料枠): 読者の悩み収集。引用は必ず手動検証 | 成果物は人間がideas/に転記 |

補足ルール:

- Gemini/Grokはリポジトリに直接アクセスしない。収集->人間検証->転記の一方向。
- briefsまではchat Claude、drafts以降はClaude Codeが境界線。

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
