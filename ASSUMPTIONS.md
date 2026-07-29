# ASSUMPTIONS.md

- 渡されたタスク内容は `setup-hygiene.sh`（ローカル実行スクリプト）そのものであり、
  本来ステージされるはずの参照ファイル（`hygiene-reusable.yml`, `caller-template.yml`,
  `WO-001-hygiene-rollout.md`, `WO-004-issue-driven-step.md`, `run-wo.sh`,
  `WO-002-template-upgrade.md`）はこのセッションに存在しなかったため、
  `work-orders/` ディレクトリの作成は行っていない。
- `hygiene-reusable.yml` / `templates/hygiene-caller-workflow.yml` は、
  既存の `.github/workflows/hygiene.yml`（`./scripts/verify.sh` を実行するのみ）から
  検証ロジックを変えずに `workflow_call` 化したもの。既存の検証項目（ファイル存在チェック、
  AGENTS.md行数、secret検出、blog draft frontmatter、サブテンプレートverify）は増減なし。
- クロスリポジトリ参照用の `uses:` は本リポジトリ名
  `promptmastertokyo-byte/codex-agents-md-docs-readme-ai` を前提にしている。
