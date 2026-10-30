#!/usr/bin/env python3
"""Validate enterprise skill catalog structure and references."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_simple_yaml_list(path: Path, key: str) -> list[dict]:
    """Minimal YAML reader for our catalog shape (no PyYAML required)."""
    text = path.read_text(encoding="utf-8")
    items: list[dict] = []
    current: dict | None = None
    in_section = False

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith(f"{key}:"):
            in_section = True
            continue
        if not in_section:
            continue
        if line and not line.startswith(" ") and not line.startswith("-") and line.endswith(":"):
            break
        if line.startswith("  - "):
            if current:
                items.append(current)
            current = {}
            rest = line[4:]
            if ":" in rest:
                k, v = rest.split(":", 1)
                current[k.strip()] = v.strip().strip('"').strip("'")
        elif current is not None and line.startswith("    ") and ":" in line:
            k, v = line.strip().split(":", 1)
            current[k.strip()] = v.strip().strip('"').strip("'")
    if current:
        items.append(current)
    return items


def main() -> int:
    catalog_path = ROOT / "registry" / "catalog.yaml"
    if not catalog_path.exists():
        print(f"FAIL: missing {catalog_path}")
        return 1

    skills = load_simple_yaml_list(catalog_path, "skills")
    if not skills:
        print("FAIL: no skills parsed from catalog.yaml")
        return 1

    errors: list[str] = []
    ids: set[str] = set()
    names: set[str] = set()

    for skill in skills:
        sid = skill.get("id", "")
        name = skill.get("name", "")
        rel = skill.get("path", "")

        if not sid:
            errors.append("skill missing id")
            continue
        if sid in ids:
            errors.append(f"duplicate id: {sid}")
        ids.add(sid)

        if not name:
            errors.append(f"{sid}: missing name")
        elif name in names:
            errors.append(f"duplicate name: {name}")
        names.add(name)

        if not rel:
            errors.append(f"{sid}: missing path")
            continue

        skill_dir = ROOT / rel
        skill_md = skill_dir / "SKILL.md"
        if not skill_dir.is_dir():
            errors.append(f"{sid}: path not found: {rel}")
        elif not skill_md.is_file():
            errors.append(f"{sid}: missing SKILL.md in {rel}")
        else:
            body = skill_md.read_text(encoding="utf-8")
            if not body.startswith("---"):
                errors.append(f"{sid}: SKILL.md missing YAML frontmatter")
            if f"name: {name}" not in body and f'name: "{name}"' not in body:
                # allow multiline / slight variance — still require name key present
                if "name:" not in body.split("---", 2)[1]:
                    errors.append(f"{sid}: frontmatter missing name")

            # Validate relative markdown links one level deep under references/
            for marker in ("](references/", "](./references/"):
                start = 0
                while True:
                    idx = body.find(marker, start)
                    if idx < 0:
                        break
                    end = body.find(")", idx)
                    link = body[idx + 2 : end]
                    target = (skill_dir / link).resolve()
                    if not target.is_file():
                        errors.append(f"{sid}: broken reference {link}")
                    start = idx + 1

    if errors:
        print("FAIL: catalog validation errors:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(f"OK: {len(skills)} skills validated")
    for skill in skills:
        print(f"  - {skill.get('id')} -> {skill.get('path')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
