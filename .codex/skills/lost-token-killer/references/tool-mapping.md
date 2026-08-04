# Tool Mapping and Integration

`SKILL.md` の補足。移植の経緯を確認するとき、他リポジトリへ持ち出すとき、
シェル出力の圧縮まで踏み込むときだけ読む。

## Claude Code 版からの移植対応表

このスキルは Claude Code スキル `lost-token-killer` の Codex 移植版。
運用思想はそのままで、実行系の名前と発動方式だけを置き換えている。

| Claude Code 版 | Codex 版 | 補足 |
| --- | --- | --- |
| description による自動発動のみ | 自動発動 + `$lost-token-killer` / `/skills` | Codex は明示呼び出し手段がある |
| `view` / `view_range` | `rg -n` で位置特定 → `sed -n 'X,Yp'` | 行範囲読みの思想は同じ |
| `str_replace` | `apply_patch` の差分ブロック | 差分編集の原則は同じ |
| `create_file` での全文再出力 | `apply_patch` の `*** Add File` | 新規作成時のみ使用 |
| `present_files` | ファイルパスの提示 | Codex に相当機能なし |
| Fable / Opus / Sonnet の使い分け | `/model`、`model_reasoning_effort` | Codex は設定でエフォートを直接制御できる |

## 設置場所

- 個人用: `~/.codex/skills/lost-token-killer/`
- プロジェクト用: `<repo>/.codex/skills/lost-token-killer/`

チーム全員に同じ運用を効かせるならプロジェクト側に置き、リポジトリに含める。
個人の癖として持ち歩くなら個人側に置く。両方に置くと二重管理になるので片方に寄せる。

## AGENTS.md への組み込み

Codex は `AGENTS.md` を毎ターン読むため、ここに全文を書くと常時コストになる。
スキル本体は遅延ロードされるので、`AGENTS.md` には発動条件と優先順位だけを短く書く。

```markdown
## Token Budget

When the user says `LTK`, `節約モード`, or a session becomes long or repetitive,
use the `lost-token-killer` skill: diff edits only, conclusion-first replies,
one-line reports. Safety confirmations in this file always override it.
```

最後の一文が重要。無駄往復ロストの「聞かずに実行」ルールは可逆操作に限る前提なので、
承認制のあるリポジトリでは `AGENTS.md` 側が勝つと明記しておかないと運用が壊れる。

## シェル出力の圧縮（任意）

このスキルはプロンプト層のルールで、`git diff` やテスト出力そのものは短くしない。
ビルドログやテスト出力が支配的なワークロードでは、シェル層で圧縮する外部ツールが効く。

- [rtk-ai/rtk](https://github.com/rtk-ai/rtk)（Apache-2.0）— コマンド出力を LLM に渡る前に
  圧縮する CLI プロキシ。`rtk init -g --codex` で `AGENTS.md` と `RTK.md` に導入手順が入る

効果はワークロード依存で、低エフォート時はかえってトークンが増えたという第三者計測もある。
常用する前に、自分の典型セッションで前後比較してから判断する。

## 効果の確かめ方

節約施策は体感で判断すると外れる。次の3点だけ記録すれば足りる。

1. 同じ規模のタスクを1件、導入前後で通す
2. `/status` などでセッションのトークン使用量を比べる
3. 成果物の品質が落ちていないか、検証コマンドの結果で確認する

品質が落ちているなら、削った工程が実は効いていたということなので戻す。
