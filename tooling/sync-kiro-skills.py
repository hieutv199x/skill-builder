#!/usr/bin/env python3
"""Copy enterprise-coding-skills/**/SKILL.md folders into real .kiro/skills/<name>/ trees.

Replaces any previous symlinks with full directory copies so Kiro/GitHub clones
work without broken links.
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "enterprise-coding-skills"
KIRO_SKILLS = REPO / ".kiro" / "skills"


def discover_skills() -> dict[str, Path]:
    seen: dict[str, Path] = {}
    for skill_md in sorted(SOURCE.rglob("SKILL.md")):
        text = skill_md.read_text(encoding="utf-8")
        match = re.search(r'^name:\s*["\']?([a-z0-9-]+)["\']?', text, re.M)
        if not match:
            print(f"WARN: no name in {skill_md}")
            continue
        name = match.group(1)
        if name in seen:
            raise SystemExit(
                f"FAIL: duplicate skill name {name}: {seen[name]} vs {skill_md.parent}"
            )
        seen[name] = skill_md.parent
    return seen


def clear_kiro_skills() -> None:
    KIRO_SKILLS.mkdir(parents=True, exist_ok=True)
    for child in list(KIRO_SKILLS.iterdir()):
        if child.is_symlink() or child.is_file():
            child.unlink()
        elif child.is_dir():
            shutil.rmtree(child)


def copy_skill(src: Path, dest: Path) -> None:
    if dest.exists() or dest.is_symlink():
        if dest.is_symlink() or dest.is_file():
            dest.unlink()
        else:
            shutil.rmtree(dest)
    shutil.copytree(
        src,
        dest,
        symlinks=False,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
    )


def main() -> int:
    if not SOURCE.is_dir():
        print(f"FAIL: missing {SOURCE}", file=sys.stderr)
        return 1

    try:
        skills = discover_skills()
    except SystemExit as exc:
        print(exc, file=sys.stderr)
        return 1

    clear_kiro_skills()

    for name, src in sorted(skills.items()):
        copy_skill(src, KIRO_SKILLS / name)

    missing = [n for n in skills if not (KIRO_SKILLS / n / "SKILL.md").is_file()]
    if missing:
        print("FAIL: missing SKILL.md after copy:", ", ".join(missing), file=sys.stderr)
        return 1

    # Ensure no symlinks remain under .kiro/skills
    stray = [
        p.relative_to(REPO).as_posix()
        for p in KIRO_SKILLS.rglob("*")
        if p.is_symlink()
    ]
    if stray:
        print("FAIL: symlinks still present:", ", ".join(stray), file=sys.stderr)
        return 1

    print(f"OK: copied {len(skills)} skills into {KIRO_SKILLS} (real directories)")
    for name in sorted(skills):
        print(f"  - {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
