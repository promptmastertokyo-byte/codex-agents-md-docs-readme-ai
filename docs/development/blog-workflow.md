# Damehuri Blog Workflow (Notion -> GitHub -> WordPress -> Measure)

This repository manages versioned Markdown drafts and WordPress automation for damehuri.com. Notion is the operating hub for priorities and KPI; GitHub is the source of truth for article changes and code. Publishing remains a deliberate human action.

## Connected Notion Pages

- [ダメフリ事業成長FB](https://app.notion.com/p/3956f1fd9481816f8eb0cb1c2f65cfe6)
- [ダメフリ運用DB](https://app.notion.com/p/f5952f7b15c14570889b1821c0e1996b)
- [Work運用ルール（公開承認制）](https://app.notion.com/p/39e6f1fd94818194960dc5fba7fc46cc)

## Responsibility Boundary

- Notion stores task status, priority, owner, deadline, hypothesis, KPI, effect-review date, article URL, and GitHub Issue/PR URL.
- GitHub stores ideas worth preserving, briefs, article Markdown, review reports, publishing scripts, metrics snapshots, improvement history, and theme/code changes.
- WordPress stores preview drafts and published content.
- Work and Codex stop at `本人確認`. Only the user enables publication approval and publishes.

## Directory Layout

- `blog/ideas/` - reusable article ideas and reader problems
- `blog/briefs/` - search intent, target reader, evidence, article angle, and priority
- `blog/drafts/` - one Markdown file per new post or rewrite
- `blog/reviews/` - SEO, readability, YMYL, evidence, and edge-case reviews
- `blog/published/` - published URL, date, and revision history
- `blog/metrics/` - Search Console and Analytics snapshots
- `blog/improvements/` - measured improvement proposals and outcomes
- `blog/style-guide.md` - writing, review, and publishing guide
- `scripts/publish-wordpress.py` - sends a reviewed article to WordPress as a draft

## Draft Format

Every draft needs `title:`, `description:`, and `slug:` frontmatter fields:

```markdown
---
title: My Post Title
description: One-sentence meta description / excerpt.
slug: my-post-slug
---

Post body goes here.
```

## Weekly Cycle

1. **Select in Notion** - Work checks current KPI and unfinished tasks. Initial operating limit is one new article, one rewrite, and five X drafts per week.
2. **Design** - create or update a brief with reader, search intent, conclusion, proof source, internal links, and target KPI.
3. **Draft** - run `sh scripts/new-post.sh <slug>` for a new article, then write to `blog/drafts/<slug>.md` using `blog/style-guide.md`.
4. **Human facts** - use `【体験談ここ】` for personal facts or experiences that only the user can provide.
5. **Review** - open a Pull Request and check SEO, readability, practical examples, official evidence, YMYL wording, and missing edge cases.
6. **Verify** - run `./scripts/verify.sh`. GitHub Actions runs the same check for Pull Requests.
7. **Approval gate** - when ready, update the matching Notion item to `本人確認`; do not enable `公開承認`.
8. **WordPress draft** - after approval to create a draft, load `.env` locally and run:

   ```sh
   set -a; . ./.env; set +a
   python3 scripts/publish-wordpress.py blog/drafts/<slug>.md
   ```

   The script always sends `status: draft`; the user reviews and clicks Publish in WordPress.
9. **Measure** - record Search Console and Analytics results after 2-4 weeks in Notion and `blog/metrics/`.
10. **Improve** - create a measured improvement plan with hypothesis, KPI, and an eight-week judgement date.

## Credentials

- `WP_SITE_URL`, `WP_USERNAME`, and `WP_APP_PASSWORD` are read from the environment and must never be committed or stored in Notion.
- Copy `.env.example` to `.env`; the real `.env` remains ignored by Git.
- Use a dedicated WordPress account with only the permissions required to create and edit drafts.

## Safety Rules

- Never fabricate experience, analytics, search queries, revenue, or credentials.
- If current data is unavailable, create a Notion collection task instead of estimating.
- Existing URL changes need a verified 301 redirect plan and user approval.
- Publishing, SNS posting, deletion, plugin/theme updates, permission changes, and production merges require explicit user approval.

