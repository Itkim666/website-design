#!/usr/bin/env python3
"""Validate the itkim-web-design skill: index <-> templates consistency.

Run from anywhere: python scripts/validate.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FIELDS = ["template_id", "template_name", "version", "description"]

errors = []


def check(cond, msg):
    if not cond:
        errors.append(msg)


# 1. Skill core files
for f in ["SKILL.md", "AGENTS.md", "README.md", "LICENSE", "config/templates.json"]:
    check((ROOT / f).is_file(), f"missing core file: {f}")

# 2. Index is valid JSON
index_path = ROOT / "config" / "templates.json"
try:
    index = json.loads(index_path.read_text(encoding="utf-8"))
    check(isinstance(index, list) and index, "templates.json must be a non-empty array")
except Exception as e:
    print(f"FAIL templates.json is not valid JSON: {e}")
    sys.exit(1)

# 3. Each index entry -> template on disk
seen_ids = set()
for entry in index:
    tid = entry.get("id", "<no id>")
    check(all(k in entry for k in ("id", "name", "path")), f"{tid}: index entry needs id/name/path")
    check(tid not in seen_ids, f"duplicate template_id in index: {tid}")
    seen_ids.add(tid)

    tdir = ROOT / entry["path"]
    check(tdir.is_dir(), f"{tid}: path not found: {entry['path']}")

    tjson = tdir / "template.json"
    try:
        meta = json.loads(tjson.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"{tid}: missing template.json")
        continue
    except Exception as e:
        errors.append(f"{tid}: template.json invalid JSON: {e}")
        continue

    missing = [f for f in REQUIRED_FIELDS if f not in meta]
    check(not missing, f"{tid}: template.json missing fields: {missing}")
    check(meta.get("template_id") == tid, f"{tid}: template_id mismatch in template.json ({meta.get('template_id')})")
    check((tdir / "README.md").is_file(), f"{tid}: missing README.md")
    for uf in meta.get("user_data_files", []):
        check((tdir / uf).exists(), f"{tid}: user_data_file not found: {uf}")

# 4. Every template dir on disk is registered in the index
on_disk = {p.parent.name for p in (ROOT / "templates").glob("*/template.json")}
unregistered = on_disk - seen_ids
check(not unregistered, f"templates exist but not in index (run this script after registering): {sorted(unregistered)}")

if errors:
    print("FAIL")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)

print(f"OK - skill structure valid, {len(index)} template(s) registered: {', '.join(sorted(seen_ids))}")
