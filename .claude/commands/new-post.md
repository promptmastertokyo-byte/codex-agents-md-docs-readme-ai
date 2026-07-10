---
description: 新規ブログ記事のドラフト生成から執筆開始まで
---

新規記事のドラフトを作成して執筆を開始する。slug: $ARGUMENTS

手順:
1. `sh scripts/new-post.sh $ARGUMENTS` を実行してドラフトを生成する
2. blog/style-guide.md を読み、タイトル4要素・150文字ルール・言い換え表を確認する
3. blog/briefs/ に $ARGUMENTS に対応するブリーフがあれば読み込む。なければユーザーに記事の狙い(ターゲット読者・検索意図・結論)を確認してから進める
4. 生成された blog/drafts/$ARGUMENTS.md の frontmatter(title / description / keywords)をブリーフに合わせて更新する
5. style-guide 準拠で本文を執筆する。結論ファースト、確認日は自動挿入済みなので触らない
6. 完了後 `./scripts/verify.sh` を実行し、結果を一行報告(✅/❌ + reason)

制約:
- LTKモード適用(差分編集・不要な往復なし)
- .env には触れない
- publish はこのコマンドの範囲外(執筆と verify まで)
