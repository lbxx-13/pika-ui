# React Bits 组件选型与适配

[React Bits](https://reactbits.dev/) 提供可组合的 React 动效组件、背景和微交互。官方页面可以查看预览、可调参数与源代码；按组件页面说明选择 JavaScript/TypeScript 和 CSS/Tailwind 变体。组件既可复制源码，也可按当前文档使用 CLI。这里的目录和安装信息会变化，集成时以官网当前页面为准。

在 Pika UI 中，React Bits 是**可选的 UI 视觉与交互参考**，不是本 skill 的技术栈要求，也不是唯一组件来源。它的视觉效果可用于启发任何平台；源码组件本身基于 React，只有目标项目使用 React 且适配成本合理时才直接集成。其他技术栈应将效果转译为符合项目框架、原生能力和交互规范的实现。

## 先按体验目标选

| 体验目标 | 可查看的组件类型 | 使用边界 |
| --- | --- | --- |
| 标题或短文案入场 | text animations、stagger、scramble、blur reveal | 少量强调；完整正文不应延迟显示或反复扰动 |
| 内容进入视口时揭示 | animated/fade content、scroll reveal | 内容默认可见；关闭动效时仍能完整阅读 |
| 背景氛围 | particles、waves、aurora、grid、shader backgrounds | 对比度弱于内容，避免持续高负载和遮挡文字 |
| 图片或作品展示 | galleries、carousels、parallax、image reveal | 同时提供按钮或常规滚动操作，触屏可用 |
| 轻量反馈 | hover、tilt、glare、cursor effects | 不替代焦点/按下状态，不让光标效果成为唯一线索 |
| 强交互展示 | draggable、3D、canvas、shader | 明确手势与性能边界；为低性能或不支持环境提供静态回退 |

以真实页面任务筛选，不把一串炫酷效果拼成组件清单。通常每屏只需要一个主视觉效果和少数轻量反馈。

## 组件组合建议

- **标题强调：** 从 Text Animations 找一个只作用于标题或数字的短动画；副标题、说明和按钮保持静态，避免阅读被拆碎。
- **入场揭示：** Animated Content / Fade Content 一类 wrapper 适合有限区块；按阅读顺序设置触发，确保首屏关键内容不因等待滚动才出现。
- **背景氛围：** Backgrounds 类组件放在内容层之后，减弱亮度/不透明度，静态色底作为低性能和减少动态效果回退。
- **悬停提示：** Micro Interactions 类组件用于可点击/可聚焦目标；触屏需可见的非悬停反馈，不靠光标效果传达状态。
- **作品/图像浏览：** Components 类画廊只用于内容适合被探索时；给出按钮或原生滚动路径，并避免强制拖拽。

组件名、目录分类和安装参数可能更新。以免费组件页面实际显示的变体、依赖和授权为准；不要从 Pro 页面推断免费组件可用性。

## 集成前检查

1. 在官网打开组件，查看真实预览、可调参数、源码变体和相关依赖；确认它是免费内容还是需要 Pro 权限。
2. 确认目标项目是否使用 React。若是，再查看 React/构建版本、包管理器、TypeScript、CSS/Tailwind 配置、动画库与组件目录；若不是，只提取效果目标并查找当前技术栈的实现方式。
3. 比较复制源码、文档提供的 CLI 和现有依赖实现的成本。优先选不会带来重复库、全局样式冲突或构建配置改动的做法。
4. 只添加实际要用的组件及其依赖；审阅生成文件和 package manifest，不接受整套演示项目覆盖现有项目。
5. 适配 Pika UI 的变量、字体、颜色、边界半径和状态；删除演示文案与无关控制项。
6. 检查窄屏、触屏、键盘焦点、减少动态效果偏好和组件加载失败时的静态状态。

官方页面示例：

- [Animated Content](https://reactbits.dev/animations/animated-content) 展示滚动揭示类组件，并分别提供 TS/JS、Tailwind/CSS 选项。
- [React Bits 首页](https://reactbits.dev/) 提供 Text Animations、Animations、Components、Backgrounds 和 Micro Interactions 等浏览入口。

官方命令可能随组件变更；不要把某个组件的安装命令写死或直接对所有项目运行。只有用户要求集成或功能确有需要时才安装，且遵循项目实际依赖和授权范围。

