---
name: itkim-web-design
version: 1.0.0
description: 可持续扩展的网站模板库 Skill。Agent 读取 config/templates.json 发现模板，按用户需求选择模板，复制到新项目中修改，原始模板永不改动。适用于 Codex 和 ZCode。
---

# itkim-web-design — 网站模板库 Skill

一个模板库 + 一套规则，同时服务 Codex 和 ZCode。新增模板只需加目录、登记索引，不需要改本 Skill。

## 触发条件

用户要求：制作网站 / 套用模板 / 推荐模板 / 把某网站加入模板库。

## 模板发现（永远从这里开始）

1. 读取 `config/templates.json` —— 这是唯一的模板索引，**禁止假设只有一个模板或硬编码模板 ID**。
2. 需要详情时读取各模板的 `templates/<id>/template.json` 和 `README.md`。
3. `templates/` 下存在 `template.json` 但未登记进索引的目录视为**未完成注册**，提醒用户运行 `scripts/validate.py`。

## 模板选择

按优先级：

1. 用户指定模板 ID（如 "使用 template-01"）→ 直接用。
2. 用户指定模板名称 → 在索引中按 `name` 匹配。
3. 用户描述需求或要求推荐 → 读取所有 `template.json`，按 `category` / `style` / `recommended_for` 匹配，选匹配度最高的，并**明确告诉用户选了哪个模板**。
4. 没有合适模板 → 如实说明，禁止虚构模板；可建议把参考网站加入模板库（见下）。

## 模板套用（核心流程）

```
templates/<id>  --复制-->  <新项目目录>（在 templates/ 之外）  --修改-->  测试  --交付-->
```

1. 在 `templates/` **之外**创建目标项目目录，把模板整个复制过去。
2. 修改副本中的用户数据文件（见该模板 `template.json` 的 `user_data_files`），替换姓名、简介、技能、项目、链接等。
3. 按用户需求继续修改副本；模板核心（布局、配色、动画、组件）默认不动，除非用户明确要求。
4. 在副本中运行构建验证（如 `npm install && npm run build`），通过后交付。

**保护规则：`templates/` 下的原始模板永远只读。任何修改都发生在副本上。**

## 添加新模板（如用户说"把这个网站加入模板库"）

1. 获取并分析该网站（结构、技术栈、组件、动画、响应式、可替换内容）。
2. 创建 `templates/template-02/`（编号顺延，保持原技术栈，不重写设计），用户内容尽量分离到数据文件。
3. 写 `template.json`（字段见 template-01，如实填写，禁止编造）和 `README.md`。
4. 在 `config/templates.json` 登记一条 `{id, name, path}`。
5. 运行 `python scripts/validate.py`，通过即完成。不改动其他模板、不改动 Skill 本体。

## 验证

```bash
python scripts/validate.py
```

检查索引与模板一一对应、`template_id` 唯一、必填字段齐全、路径有效。此脚本同时是 Skill 的测试。

## 版本

Skill 版本（本文件 `version`）与各模板版本（各自 `template.json` 的 `version`）相互独立。新增模板不升级 Skill 版本。

## Codex / ZCode 使用方式

两个 Agent 都通过读取本文件 + `AGENTS.md` 使用本 Skill，通过 `config/templates.json` 发现模板——无任何私有格式。安装方式见根目录 `README.md`。

## 禁止事项

- 修改 `templates/` 下的原始模板。
- 虚构模板、虚构功能、虚构测试、虚构已发布。
- 在模板中写入绝对路径、API Key、密码。
- 为兼容某一个 Agent 而制作另一套模板库。
