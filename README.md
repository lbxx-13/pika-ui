# Pika UI Skill

![Pika UI pickup truck logo](assets/pika-ui-logo.png)

面向 React 界面的设计与实现工作流，参考 oil-ui 的分主题文档结构，并将 React Bits 作为可选组件来源。Skill 入口是 `SKILL.md`；参考资料按任务加载，不需要一次读完。

## 使用

把整个 `pika-ui` 文件夹复制到 Codex skills 目录（通常为 `$CODEX_HOME/skills/pika-ui`，未设置时为 `~/.codex/skills/pika-ui`），然后使用 `$pika-ui`，或直接提出页面设计、组件选型、截图还原和 UI 评审任务。

方向比较器适用于已经生成的候选页面；本目录提供的 `scripts/create_style_explorer.py` 可生成可打开的比较页地址。详情见 `references/style-explorer.md`。

## 目录

- `SKILL.md`：技能说明与任务路由。
- `references/`：方向、页面、视觉、交互、动效、素材和验收规范。
- `assets/style-explorer.html`：本地候选页面比较器。
- `assets/pika-ui-logo.png`：ImageGen 生成的彩色皮卡车标志。
- `scripts/create_style_explorer.py`：比较页链接生成脚本。

