# 方向比较器

比较器源码在 `assets/style-explorer.html`。手动使用时可以在地址上设置 `a`、`b`、`c` 页面地址及相应的 `*-title`、`*-note`。候选地址可为本地相对路径或本地开发服务器地址。

也可以从项目目录运行：

```sh
python3 <skill>/scripts/create_style_explorer.py \
  --output ./design-review/compare.html \
  --candidate '当前版|./current.html|基线' \
  --candidate '方向 A|./direction-a.html|内容优先' \
  --candidate '方向 B|./direction-b.html|编辑式布局'
```

脚本复制比较器和皮卡车标志到输出位置，打印可打开的本地地址。相对候选路径按当前工作目录解析，输出目录必须已存在。可只传一个或两个候选。比较器允许统一切换桌面/手机宽度、标记选择并复制一行反馈；它不会生成候选、截图或验证页面交互。

