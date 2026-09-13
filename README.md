# website-design

可持续扩展的网站模板库 Skill，同时面向 **Codex** 和 **ZCode**。一个 Skill + 一个模板库，两个 Agent 读同一套文件，新增模板不需要重新制作 Skill。

## 结构

```
├── SKILL.md                 # Skill 核心：模板发现/选择/套用/保护/添加规则
├── AGENTS.md                # Codex/ZCode 入口，指向 SKILL.md
├── config/templates.json    # 模板索引（唯一入口）
├── templates/<id>/          # 模板母版（只读！）：源码 + template.json + README.md
└── scripts/validate.py      # 结构验证（同时是测试）
```

当前模板：**template-01 — Itkim Portfolio**（夜空视觉个人作品集，React + TS + Vite + Canvas，来源 https://itkim666.github.io/portfolio/ ）。

## 安装

整个目录复制到目标位置即可（无构建、无依赖）：

### Codex

Codex 无需注册机制：把本目录放在你的项目里（或任意固定位置），在项目根的 `AGENTS.md` 中加一行指向本目录，或直接让 Codex 打开本目录工作。Codex 会读到 `AGENTS.md` → `SKILL.md` → `config/templates.json`。

> 注意：**本环境未安装 Codex，以上为通用接入方式，未在真实 Codex 中实测。**

### ZCode

把本目录复制为 ZCode 的技能目录下的子目录（Windows 示例）：

```
xcopy /E /I "D:\projects\website—degisn" "C:\Users\<你>\.agents\skills\website-design"
```

重启会话后即可被 ZCode 发现（本仓库即按此方式安装验证过）。

## 使用（两个 Agent 相同）

- "查看有哪些模板" → 读 `config/templates.json`
- "使用 template-01 制作我的网站" → 复制 `templates/template-01` 到 templates/ 之外的新目录，改副本数据文件
- "推荐一个适合程序员的模板" → Agent 分析各 template.json 后推荐
- "把这个网站加入模板库" → Agent 建新模板目录 + 登记 `config/templates.json` + 运行验证

## 添加 / 修改模板

流程见 `SKILL.md` 的"添加新模板"。要点：新目录 `templates/template-02/` + `template.json` + `README.md` → 索引加一行 `{id, name, path}` → `python scripts/validate.py`。模板版本写在各自 `template.json`，与 Skill 版本无关。

## 验证

```bash
python scripts/validate.py
# OK - skill structure valid, 1 template(s) registered: template-01
```

## 状态说明（如实）

- Skill 已创建 ✅（文件实际存在，validate 通过）
- template-01 已注册 ✅
- **已发布到 GitHub**：https://github.com/Itkim666/website-design
- 克隆即用：`git clone https://github.com/Itkim666/website-design.git`，然后把目录放入对应 Agent 的技能/工作目录。
- 以后新增模板：加目录 + 索引加一行 → `python scripts/validate.py` → `git add -A && git commit -m "add template-02" && git push`，其他机器 `git pull` 即可。

首次推送（已完成初始化，留作参考）：

```bash
cd "D:\projects\website—degisn"
git init -b main
git add -A && git commit -m "website-design v1.0.0"
git remote add origin https://github.com/Itkim666/website-design.git
git push -u origin main
```

## 许可

MIT（见 LICENSE）。template-01 源自 https://itkim666.github.io/portfolio/ 。
