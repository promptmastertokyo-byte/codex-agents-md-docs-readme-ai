# Notion and ChatGPT Work Integration

## Purpose

Use Notion as the live operating dashboard and GitHub as durable, versioned production memory. This avoids losing decisions in chat while preventing duplicate sources of truth.

## Connected Pages

- Strategy and operating policy: [ダメフリ事業成長FB](https://app.notion.com/p/3956f1fd9481816f8eb0cb1c2f65cfe6)
- Weekly tasks and KPI: [ダメフリ運用DB](https://app.notion.com/p/f5952f7b15c14570889b1821c0e1996b)
- Work authority and approval boundaries: [Work運用ルール（公開承認制）](https://app.notion.com/p/39e6f1fd94818194960dc5fba7fc46cc)

## Field Mapping

| Notion field | GitHub artifact |
| --- | --- |
| 施策・記事名 | brief/draft/review title |
| ステータス | lifecycle from selected to human review |
| 対象KW | brief search-intent section |
| 仮説 | brief and improvement report |
| 計測KPI | metrics and improvement report |
| 期限 | Pull Request target date |
| 判定日 | effect-review entry in metrics/improvements |
| 記事URL | published record |
| GitHub Issue | implementation or content Issue/PR link |
| 公開承認 | human-only publication gate |

## Work Automation

Every Monday, ChatGPT Work:

1. Reads the strategy page, Media Growth OS, and operation database.
2. Reviews completed, overdue, blocked, and effect-review items.
3. Limits the week to one new article, one rewrite, and five X drafts unless the user changes the rule.
4. Updates priority, owner, deadline, hypothesis, and KPI in Notion.
5. Creates or updates the matching GitHub artifact when repository work is required.
6. Moves prepared work to `本人確認` and reports what the user must decide.

Work must not publish, enable `公開承認`, merge production changes, or invent missing KPI.

## Linking Rule

- A Notion task that requires repository work should contain a GitHub Issue or Pull Request URL.
- A GitHub brief, draft, review, or improvement report should contain the matching Notion page URL when available.
- Do not copy full article bodies into Notion. Keep versioned article content in GitHub.

