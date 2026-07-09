# Blog Repo Agent Rules

## Response Style

- 日本語で返答
- 結論ファースト
- 変更したファイルと確認結果を短く報告

## Blog Rules

- `blog/style-guide.md` に沿って記事を書く
- ネタ集めは `blog/ideas/` に残す
- 記事企画は `blog/briefs/` に残す
- 記事本文は `blog/drafts/` に置く
- レビューは `blog/reviews/` に残す
- 公開済み記事の管理は `blog/published/` に残す
- 計測結果は `blog/metrics/` に残す
- 改善案と改善履歴は `blog/improvements/` に残す
- 勝ちパターンと失敗パターンは `docs/playbook.md` に反映する
- 制度・税務・法律・医療・金融の記事は、公開直前に最新情報を確認する
- 公式情報、確認日、監修メモを記事内に残す
- AIの出力はチャットだけで終わらせず、必要なものをファイル化する

## Safety

- `.env` や認証情報を出力しない
- WordPressへの公開操作は事前確認する
- `git commit` は確認を取ってから実行する
