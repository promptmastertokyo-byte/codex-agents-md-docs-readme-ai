# Blog Specialized Repo Template

Markdownで記事を作成し、レビューし、WordPress下書きへ投入し、公開後に改善するためのブログ特化リポジトリテンプレートです。

## Quick Start

```sh
./scripts/verify.sh
```

新しい記事は `blog/drafts/` に作成します。

```sh
cp templates/blog-post.md blog/drafts/example-post.md
```

## Workflow

```text
Idea Research
↓
Article Brief
↓
Draft
↓
Review
↓
Publish
↓
Measure
↓
Improve
↓
Feed Learnings Back to Ideas
```

## Directory Layout

```text
.
├── AGENTS.md
├── README.md
├── blog/
│   ├── ideas/
│   ├── briefs/
│   ├── drafts/
│   ├── reviews/
│   ├── published/
│   ├── metrics/
│   ├── improvements/
│   └── style-guide.md
├── docs/
│   ├── measurement.md
│   ├── playbook.md
│   └── publishing.md
├── scripts/
│   └── verify.sh
└── templates/
    ├── idea-research-request.md
    ├── article-brief.md
    ├── blog-post.md
    ├── review-report.md
    ├── content-calendar.md
    └── improvement-report.md
```

## AI Team Roles

| Directory | Owner | Purpose |
| --- | --- | --- |
| `blog/ideas/` | ネタ集めAI | 世間の悩み、検索語、トレンド、読者の本音を保存 |
| `blog/briefs/` | 記事企画AI | 読者、検索意図、見出し、根拠、記事化優先度を整理 |
| `blog/drafts/` | Claude | Style Guideに沿って本文を作成 |
| `blog/reviews/` | レビューAI / Codex | SEO、読みやすさ、実務性、根拠を確認 |
| `blog/published/` | 公開担当 | 公開済み記事のURL、公開日、更新履歴を管理 |
| `blog/metrics/` | 計測AI | Search Console / Analytics の結果を保存 |
| `blog/improvements/` | 改善AI | 計測結果から改善案と実施内容を残す |
| `docs/playbook.md` | 編集長 / Codex | 勝ちパターン、失敗パターン、運用ルールを蓄積 |

## Operating Rules

- GitHub is the durable source of truth for article changes.
- WordPress publishing is manual after review.
- Every article needs a title, description, slug, and evidence section.
- Measure after publishing, then improve based on Search Console and analytics data.
- Every AI output should become a repository artifact, not just a chat message.
