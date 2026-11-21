[English](README.md) · 简体中文 · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · [Español](README.es.md)

<p align="center">
  <img src="assets/pika-ui-logo.png" width="300" alt="Pika UI 彩色皮卡车标志">
</p>

<h1 align="center">Pika UI</h1>

<p align="center"><strong>从真实任务出发，把界面设计清楚，再按项目技术栈实现。</strong></p>

<p align="center"><a href="https://pika-ui.mytools.fyi/">访问 Pika UI 官方网站 ↗</a></p>

Pika UI 是一套为 AI coding agent 准备的跨平台界面设计与实现 skill。它帮助你从新界面、改版、截图还原到 UI 评审完成完整交付，适用于 Web、桌面、移动端及其他软件界面。

React Bits 是可选的 UI 视觉与交互参考，不是技术栈要求。React 项目可按需评估其组件；其他技术栈可以借鉴效果，再按目标平台实现。

## 安装

### 在终端安装

在任意目录运行下面这条命令。它会将 `pika-ui` 全局安装给你选择的 AI 编程 Agent 使用：

```bash
npx skills add lbxx-13/pika-ui --skill pika-ui -g
```

这个 GitHub 仓库目前是私有仓库。运行命令的电脑必须已经有仓库访问权限，例如已配置 Git 凭据、GitHub CLI 登录或 SSH。按提示选择要安装到的 Agent。若想指定多个 Agent，可添加 `-a`，例如 `-a codex -a claude-code -a cursor`。

### 让 Agent 帮你安装

把下面这句话发给任何能够运行终端命令的 AI 编程 Agent：

```text
请帮我为当前 AI 编程 Agent 安装 Pika UI skill，运行：npx skills add lbxx-13/pika-ui --skill pika-ui -g
```

运行 Agent 的电脑同样需要有这个私有 GitHub 仓库的访问权限。如果 CLI 提示认证失败，先配置 GitHub 访问权限，再重新运行命令。

### 以后更新

```bash
npx skills update pika-ui -g
```

如果你只为 Codex 手动 clone 安装，则运行：

```bash
git -C ~/.codex/skills/pika-ui pull --ff-only
```

如果使用自定义 `CODEX_HOME`，请把命令中的 `~/.codex` 替换为你的 Codex 主目录。

## 使用 Pika UI

安装后按需重启或重新加载你的 Agent。如果它支持显式调用 skill，可以按名称调用；否则直接说“请使用 Pika UI skill”并描述任务。提供相关项目、截图、品牌素材和约束，它会先检查现有技术栈，再按任务加载对应指南。

## 可以用它做什么

- **设计新界面：** 为产品页面、工作区、移动端视图或单个组件确定清楚的视觉方向并实现。
- **改造现有界面：** 先理解项目已有的页面、设计 token、共享组件与交互，再按任务调整。
- **还原参考图：** 从布局、比例、字体、颜色和层级开始，在目标视口中逐步还原。
- **比较设计方向：** 按需生成最多三个真正有差异的候选，并使用本地比较页并排查看。
- **评审体验：** 检查视觉层级、响应式布局、交互状态、键盘可用性和减少动态效果时的表现。
- **借鉴动效与素材：** 参考 React Bits 的可选组件示例，或为页面选择合适的图像、图标与动效。

## 示例请求

```text
用 Pika UI 为这款课程预约产品设计一个可预览的落地页。先根据目标用户和课程内容确定方向，再实现桌面与手机布局。
```

```text
用 Pika UI 按这张截图还原页面。先检查项目当前使用的框架和样式规范，再实现并检查窄屏布局。
```

```text
用 Pika UI 评审这个页面，只列出有截图或代码证据的问题，并给出具体修改建议，不要改文件。
```

## 工作流程

1. **理解上下文：** 确认目标用户、主要任务、设备、现有页面和项目技术栈。
2. **做出设计决定：** 明确页面主角、主操作、视觉方向、字体与色彩、主视觉和关键状态。
3. **按项目实现：** 沿用项目已有组件、设计 token、依赖和平台交互习惯。
4. **检查真实界面：** 在目标视口检查页面、重要状态与主要操作；根据发现收敛并做减法。

参考资料按任务加载，不需要一次读完。明确的小改动直接执行，不需要走完完整方向流程。

## 文档地图

| 需要处理的任务 | 入口文档 |
| --- | --- |
| 新页面、设计改版与实现 | [`references/design-workflow.md`](references/design-workflow.md) |
| 视觉方向与概念探索 | [`references/design-direction.md`](references/design-direction.md)、[`references/task-explore.md`](references/task-explore.md) |
| 营销、品牌与发布页面 | [`references/direction-persuasion.md`](references/direction-persuasion.md) |
| 截图还原、布局与视口 | [`references/layout-and-viewport.md`](references/layout-and-viewport.md) |
| 字体、颜色、表面与层级 | [`references/visual-language.md`](references/visual-language.md) |
| 设计 token 与系统维护 | [`references/design-system.md`](references/design-system.md) |
| 表单、弹窗与复杂状态 | [`references/interaction-states.md`](references/interaction-states.md) |
| 动效与减少动态效果 | [`references/motion.md`](references/motion.md) |
| 图片、图标及素材来源 | [`references/media.md`](references/media.md) |
| UX 流程走查 | [`references/ux-review.md`](references/ux-review.md) |
| 只读 UI 评审 | [`references/task-review.md`](references/task-review.md)、[`references/review-checklist.md`](references/review-checklist.md) |
| 候选页面比较 | [`references/style-explorer.md`](references/style-explorer.md) |
| 浏览器与开发工具 | [`references/tools.md`](references/tools.md) |

### React Bits 的定位

[React Bits](https://reactbits.dev/) 提供文字动画、背景、组件和微交互示例。Pika UI 将它用作可选的视觉与交互灵感来源。需要参考或集成时先查看 [`references/react-bits.md`](references/react-bits.md)：React 源码组件只在目标项目采用 React 且集成合适时直接使用；其他平台只借鉴交互意图和视觉效果。

## 目录

```text
SKILL.md                         Skill 入口与任务路由
references/                      按任务读取的设计、实现与评审指南
assets/style-explorer.html       本地候选页面比较器
assets/pika-ui-logo.png          Pika UI 皮卡车标志
scripts/create_style_explorer.py 生成比较页链接的脚本
```

方向比较器适合查看已经生成的候选页面；它不会替代方向设计，也不会自动生成设计方案。

## 设计边界

- 优先遵循项目的真实品牌、技术栈、组件和平台惯例，不强行套用固定风格。
- 只使用项目提供或已验证的产品事实，不编造数据、客户评价或功能承诺。
- React Bits 不是通用组件库或唯一组件来源；跨平台项目按目标技术栈适配。
- 视觉、交互和功能分别检查；没有实际运行的内容会明确标出未验证范围。

