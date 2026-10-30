#!/usr/bin/env python3
"""Rebuild .kiro/skills/* symlinks from enterprise-coding-skills/**/SKILL.md."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "enterprise-coding-skills"
KIRO_SKILLS = REPO / ".kiro" / "skills"


def main() -> int:
    if not SOURCE.is_dir():
        print(f"FAIL: missing {SOURCE}", file=sys.stderr)
        return 1

    KIRO_SKILLS.mkdir(parents=True, exist_ok=True)

    # Remove old symlinks only (leave unexpected real dirs alone but warn)
    for child in list(KIRO_SKILLS.iterdir()):
        if child.is_symlink():
            child.unlink()
        elif child.is_dir():
            print(f"WARN: leaving non-symlink directory {child.name}")

    seen: dict[str, Path] = {}
    for skill_md in sorted(SOURCE.rglob("SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        match = re.search(r'^name:\s*["\']?([a-z0-9-]+)["\']?', text, re.M)
        if not match:
            print(f"WARN: no name in {skill_md}")
            continue
        name = match.group(1)
        if name in seen:
            print(f"FAIL: duplicate skill name {name}: {seen[name]} vs {skill_md.parent}")
            return 1
        seen[name] = skill_md.parent

    for name, src in sorted(seen.items()):
        dest = KIRO_SKILLS / name
        rel = Path(os.path.relpath(src, start=dest.parent))
        dest.symlink_to(rel, target_is_directory=True)

    missing = [n for n, p in seen.items() if not (KIRO_SKILLS / n / "SKILL.md").exists()]
    if missing:
        print("FAIL: broken links:", ", ".join(missing))
        return 1

    print(f"OK: linked {len(seen)} skills into {KIRO_SKILLS}")
    for name in sorted(seen):
        print(f"  - {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
