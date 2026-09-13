# AGENTS.md

本目录是 **itkim-web-design** 网站模板库 Skill（同时面向 Codex 和 ZCode）。

任何 Agent 在此工作前，先读 [SKILL.md](SKILL.md)——模板发现、选择、套用、添加、验证的全部规则都在那里。

三条铁律：

1. 模板入口只有 `config/templates.json`，不要硬编码模板 ID。
2. `templates/` 下的原始模板**只读**；用户网站 = 复制到 `templates/` 之外的副本。
3. 改动索引或模板后运行 `python scripts/validate.py`。
