# ダメフリ Blog Operations

ダメフリ（damehuri.com）の企画、執筆、レビュー、WordPress下書き、公開後の計測・改善を、ChatGPT Work・Notion・GitHub・Codexで運用するためのリポジトリです。

## Operating Model

| System | Source of truth |
| --- | --- |
| Notion | 企画、優先順位、担当、期限、KPI、効果判定 |
| GitHub | 記事Markdown、レビュー履歴、運用ルール、スクリプト、WordPressテーマ改修 |
| WordPress | 下書き確認と公開済みコンテンツ |
| ChatGPT Work | 週次運用、企画、執筆、監査、Notion更新 |
| Codex | GitHub実装、検証、Issue・Pull Request準備 |
| 本人 | 実体験・実数の確定、公開承認、WordPress公開、本番マージ |

## Notion Operating Hub

- [ダメフリ事業成長FB](https://app.notion.com/p/3956f1fd9481816f8eb0cb1c2f65cfe6)
- [ダメフリ運用DB](https://app.notion.com/p/f5952f7b15c14570889b1821c0e1996b)
- [Work運用ルール（公開承認制）](https://app.notion.com/p/39e6f1fd94818194960dc5fba7fc46cc)

Notionで「今週」と決定した項目だけをGitHubで記事・レビュー・実装へ進めます。公開準備が整ったらNotionのステータスを「本人確認」に変更します。WorkやCodexは「公開承認」を自分でONにしません。

## Weekly Workflow

1. WorkがNotionのKPI・期限・前週結果を確認する
2. 原則「新規記事1本・リライト1本・X投稿5本」を今週分として選定する
3. 企画を `blog/briefs/`、本文を `blog/drafts/` に保存する
4. Pull RequestでSEO、根拠、読みやすさ、YMYL、安全性をレビューする
5. `./scripts/verify.sh` で形式と機密情報を検査する
6. WordPressには `draft` として送信し、本人が確認して公開する
7. 公開後の数値をNotionと `blog/metrics/` に記録し、改善案を `blog/improvements/` に残す

## Quick Start

```sh
./scripts/verify.sh
sh scripts/new-post.sh <slug>
```

WordPress下書き作成は `docs/development/blog-workflow.md` を参照してください。認証情報は `.env` にだけ保存し、GitHub・Notion・チャットには記載しません。

## Repository Layout

```text
.
├── AGENTS.md
├── README.md
├── docs/
│   ├── ai/
│   └── development/
├── blog/
│   ├── ideas/
│   ├── briefs/
│   ├── drafts/
│   ├── reviews/
│   ├── published/
│   ├── metrics/
│   └── improvements/
├── templates/
├── scripts/
├── work/
└── outputs/
```

## Safety Gates

- AIは体験・数値・実績を捏造しない
- 制度・税務・法律・医療・金融は公開直前に公式情報を再確認する
- WordPressへの送信は下書きまで。公開は本人が行う
- URL変更、削除、プラグイン更新、本番マージは本人確認後に行う
- APIキー、Application Password、トークンをコミットしない

