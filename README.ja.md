[English](README.en.md) · [简体中文](README.md) · 日本語 · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Español](README.es.md)

<p align="center">
  <img src="assets/pika-ui-logo.png" width="300" alt="Pika UI のカラフルなピックアップトラックのロゴ">
</p>

<h1 align="center">Pika UI</h1>

<p align="center"><strong>実際の課題から始め、UI を明確に設計し、プロジェクトに合った方法で実装します。</strong></p>

Pika UI は、AI コーディングエージェント向けのクロスプラットフォーム UI 設計・実装スキルです。Web、デスクトップ、モバイルなど、さまざまなソフトウェアの画面で、新規 UI、リデザイン、スクリーンショットの再現、UI レビューまでを支援します。

React Bits は、ビジュアルやインタラクションを考えるための任意の参考資料であり、技術スタックの指定ではありません。React プロジェクトでは必要に応じてコンポーネントを検討し、それ以外の環境では対象プラットフォームに合わせて効果を実装します。

## はじめる

リポジトリを Codex の skills ディレクトリに clone します。

```bash
git clone https://github.com/lbxx-13/pika-ui.git ~/.codex/skills/pika-ui
```

独自の `CODEX_HOME` を使う場合は、`$CODEX_HOME/skills/pika-ui` に配置してください。非公開リポジトリには、マシン上で GitHub にアクセスできる設定が必要です。インストール後、新しい Codex のターンで `$pika-ui` を使うか、作業内容をそのまま伝えてください。

インストール済みの skill を更新する場合：

```bash
git -C ~/.codex/skills/pika-ui pull --ff-only
```

## できること

- **新しい UI の設計：** プロダクトページ、ワークスペース、モバイル画面、コンポーネントの方向を決めて実装します。
- **既存 UI の改善：** ページ、デザイントークン、共有コンポーネント、動作を把握してから変更します。
- **参考画像の再現：** レイアウト、比率、書体、色、階層を再現し、対象ビューポートで確認します。
- **方向性の比較：** 依頼に応じて、実質的に異なる最大 3 案を作り、ローカル比較ページで並べて確認します。
- **体験のレビュー：** 階層、レスポンシブ、状態、キーボード操作、動きを減らす設定を確認します。
- **動きと素材の検討：** React Bits を任意の参考にしたり、画像、アイコン、アニメーションを選んだりできます。

## プロンプト例

```text
$pika-ui このコース予約サービスのランディングページを作って、プレビューできるようにしてください。対象ユーザーと講座内容に合わせて方向を決め、デスクトップとモバイルのレイアウトを実装してください。
```

```text
Pika UI を使って、このスクリーンショットを再現してください。まずプロジェクトのフレームワークとスタイル規約を確認し、実装後に狭い画面幅も確認してください。
```

```text
Pika UI でこのページをレビューしてください。スクリーンショットまたはコードで裏付けられる問題と具体的な修正案だけを報告し、ファイルは変更しないでください。
```

## ワークフロー

1. **状況を理解する：** 対象ユーザー、主なタスク、デバイス、既存 UI、プロジェクトの技術スタックを確認します。
2. **設計を決める：** 焦点、主な操作、方向性、書体と色、ビジュアル素材、重要な状態を明確にします。
3. **プロジェクトに合わせて実装する：** 既存コンポーネント、デザイントークン、依存関係、プラットフォーム規約を活用します。
4. **実際の UI を確認する：** 対象ビューポート、重要な状態、主な操作を確認し、不要な要素を整理します。

参考資料はタスクに必要なものだけ読みます。小さく明確な変更には、設計方向のフルプロセスは不要です。

## ガイド一覧

| タスク | ガイド |
| --- | --- |
| 新規 UI、リデザイン、実装 | [`references/design-workflow.md`](references/design-workflow.md) |
| デザイン方向とコンセプト探索 | [`references/design-direction.md`](references/design-direction.md)、[`references/task-explore.md`](references/task-explore.md) |
| マーケティング、ブランド、ローンチページ | [`references/direction-persuasion.md`](references/direction-persuasion.md) |
| 画像再現、レイアウト、ビューポート | [`references/layout-and-viewport.md`](references/layout-and-viewport.md) |
| 書体、色、表面、階層 | [`references/visual-language.md`](references/visual-language.md) |
| デザイントークンとシステムの保守 | [`references/design-system.md`](references/design-system.md) |
| フォーム、ダイアログ、複雑な状態 | [`references/interaction-states.md`](references/interaction-states.md) |
| モーションと動きを減らす設定 | [`references/motion.md`](references/motion.md) |
| 画像、アイコン、素材の出典 | [`references/media.md`](references/media.md) |
| UX フローの確認 | [`references/ux-review.md`](references/ux-review.md) |
| 読み取り専用の UI レビュー | [`references/task-review.md`](references/task-review.md)、[`references/review-checklist.md`](references/review-checklist.md) |
| 候補の比較 | [`references/style-explorer.md`](references/style-explorer.md) |
| ブラウザーと開発ツール | [`references/tools.md`](references/tools.md) |

### React Bits の位置づけ

[React Bits](https://reactbits.dev/) には、テキストアニメーション、背景、コンポーネント、マイクロインタラクションがあります。Pika UI では、ビジュアルや操作を考えるための任意の参考として扱います。利用・適応する場合は [`references/react-bits.md`](references/react-bits.md) を参照してください。React のソースコンポーネントを直接使うのは、対象プロジェクトが React を採用し、適合する場合に限ります。それ以外のプラットフォームでは、意図や視覚効果を各環境に合わせて実装します。

## ディレクトリ構成

```text
SKILL.md                          Skill の入口とタスクルーティング
references/                       設計・実装・レビューのガイド
assets/style-explorer.html        ローカル候補比較ページ
assets/pika-ui-logo.png           Pika UI のピックアップトラックロゴ
scripts/create_style_explorer.py  比較ページのリンク生成スクリプト
```

比較ページは、すでにある候補を確認するためのものです。デザイン案を自動生成する機能ではありません。

## 設計上の原則

- 固定スタイルを押しつけず、プロジェクトのブランド、技術スタック、コンポーネント、プラットフォームの規約に従います。
- プロジェクトで提示された、または検証できた事実を使い、指標、顧客の声、機能の約束を作りません。
- React Bits はクロスプラットフォームのコンポーネントライブラリでも、唯一の選択肢でもありません。参考を対象スタックに合わせます。
- 視覚、操作、機能を分けて確認します。実行していない部分は未確認として明記します。

