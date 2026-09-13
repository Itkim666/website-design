# template-01 — Itkim Portfolio

| | |
|---|---|
| 模板 ID | template-01 |
| 版本 | 1.0.0 |
| 来源 | https://itkim666.github.io/portfolio/ |
| 技术栈 | React 18 + TypeScript + Vite · 零第三方动画/路由/图标库 · 背景 = 原生 Canvas 2D |

夜空视觉（北极星 + 极光 + 流星）个人作品集：简历 + 项目库 + GitHub 展示 + 项目技术文档，单页滚动 + 项目详情 hash 路由。

## 页面与组件

- 单页：Hero → About → Skills → Projects → GitHub → Education → Contact → Footer，滚动联动导航高亮
- 项目详情页：卡片网格点击进入，含滚动联动大纲（ProjectOutline）
- `src/background/`：engine 统一驱动 stars（星野+北极星）/ aurora（1/4 分辨率离屏）/ meteors（流星状态机）/ particles（对象池）/ pointer / glow

## 可替换内容（用户数据）

改这些文件即可换掉全部个人信息，**不动页面代码**：

| 文件 | 内容 |
|---|---|
| `src/data/site.ts` | 姓名、职业、一句话简介、GitHub、邮箱、About 段落、技能分组、教育经历 |
| `data/projects.json` | 项目列表：名称、封面、技术栈、详情（背景/目标/功能/架构/踩坑/结果） |
| `public/projects/<slug>/` | 各项目封面图等静态资源 |

## 固定内容（模板核心，默认不改）

布局、夜空背景引擎与全部动画、颜色/字体体系（`src/styles/global.css`）、组件结构、响应式断点。除非用户明确要求，套用时不要改。

## 使用方法

```bash
# 1. 把本目录整个复制到 templates/ 之外的新项目目录（禁止直接在本目录修改）
# 2. 在副本中：
npm install
npm run dev       # 开发预览
npm run build     # 纯静态构建到 dist/，可部署 GitHub Pages / Netlify / 任意静态服务器
```

加新项目 = 在 `public/projects/` 建目录放封面 + 在 `data/projects.json` 加一段 JSON。

## 注意事项

- 邮箱留空时 Contact 条目自动隐藏（优雅降级）。
- `src/data/site.ts` 中 `education` 有一处 "My University" 占位，套用时替换。
- `.github/workflows/deploy.yml` 是原作者的 GitHub Pages 自动部署配置，副本中需改成自己的仓库或删除。
- 动画已含移动端降级与 prefers-reduced-motion，不要为性能砍掉粒子系统，引擎自身会降级。
