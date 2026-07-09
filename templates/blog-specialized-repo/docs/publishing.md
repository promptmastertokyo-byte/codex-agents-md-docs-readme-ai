# Publishing

WordPressへの公開は手動確認を挟みます。

## Flow

1. `blog/drafts/` で記事を作成
2. レビューを実施
3. `./scripts/verify.sh` を通す
4. WordPressに下書きとして投入
5. wp-adminで最終確認
6. 公開

## Pre-Publish Check

- タイトルに年・数字・検索語・権威性がある
- メタディスクリプションがある
- FAQが3〜5問ある
- 参考資料と確認日がある
- 監修者がいる場合は監修情報がある
- アイキャッチとカテゴリを設定した
