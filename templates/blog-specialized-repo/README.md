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
Style Guide
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
```

## Directory Layout

```text
.
├── AGENTS.md
├── README.md
├── blog/
│   ├── drafts/
│   ├── published/
│   └── style-guide.md
├── docs/
│   ├── measurement.md
│   └── publishing.md
├── scripts/
│   └── verify.sh
└── templates/
    ├── blog-post.md
    ├── review-report.md
    └── improvement-report.md
```

## Operating Rules

- GitHub is the durable source of truth for article changes.
- WordPress publishing is manual after review.
- Every article needs a title, description, slug, and evidence section.
- Measure after publishing, then improve based on Search Console and analytics data.
