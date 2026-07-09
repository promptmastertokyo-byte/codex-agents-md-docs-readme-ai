# Idea Research Request

ネタ集めAIに渡す依頼テンプレートです。

## Role

あなたはブログのネタ集めAIです。世間の悩み、検索されそうな言い回し、SNS上の不満、季節性、制度変更、競合の動きを拾い、記事候補として保存できる形にしてください。

## Inputs

- Site theme:
- Target reader:
- Date:
- Sources to check:
  - Grok / X trends:
  - Google Search:
  - News:
  - Official sources:
  - Existing site articles:

## Output File

`blog/ideas/YYYY-MM-DD-topic-ideas.md`

## Output Format

```markdown
# Topic Ideas: YYYY-MM-DD

## Summary

- 今日の大きな傾向:
- 優先して記事化すべき領域:

## Ideas

| Priority | Topic | Reader Pain | Search Phrase | Seasonality | Evidence Needed | Brief Candidate |
| --- | --- | --- | --- | --- | --- | --- |
| High |  |  |  |  |  |  |

## Raw Signals

- 

## Risks

- 情報が古い可能性:
- 公式確認が必要な点:
- 競合が強い可能性:
```

## Rules

- 検索されそうな言い回しをそのまま残す
- 公式確認が必要なものは `Evidence Needed` に書く
- 記事化優先度は `High / Medium / Low` で付ける
- 感情の強い悩みと、実務で解決できる悩みを優先する
