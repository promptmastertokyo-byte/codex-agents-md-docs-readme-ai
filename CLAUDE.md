# CLAUDE.md

Repository-specific rules for Claude (chat) and Claude Code in this repo.
Read `AGENTS.md` first for the general operating guide and AI team roles.

## 執筆時のルール

- 記事を書く・リライトする際は `blog/style-guide.md` に必ず準拠する

## セキュリティ

- `.env` は読まない・内容を出力しない・`cat` しない
- `scripts/publish-wordpress.py` 実行時は `set -a; . ./.env; set +a` で環境変数
  としてロードするのみ。値を表示・ログ出力しない

## 公開

- 公開(publish)は行わない。WordPressへの投稿は常に `status: draft` で作成する。
  公開はwp-adminで人間が行う

## 応答スタイル

- LTKモード適用: 差分編集・結論ファースト・一行報告
