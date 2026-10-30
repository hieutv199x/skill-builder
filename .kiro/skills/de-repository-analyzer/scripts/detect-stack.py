#!/usr/bin/env python3
"""Deterministic stack signal dump for a repository root."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def read_text(path: Path, limit: int = 200_000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:limit]
    except OSError:
        return ""


def find_version(patterns: list[str], text: str) -> str | None:
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return None


def analyze(root: Path) -> dict:
    signals: dict = {"root": str(root.resolve()), "stacks": [], "files": []}

    pom = root / "pom.xml"
    gradle = next(root.glob("build.gradle*"), None)
    package_json = root / "package.json"
    angular_json = root / "angular.json"
    pyproject = root / "pyproject.toml"
    requirements = root / "requirements.txt"

    if pom.exists() or gradle is not None:
        build_file = pom if pom.exists() else gradle
        text = read_text(build_file)
        signals["files"].append(str(build_file.relative_to(root)))
        entry = {
            "stack": "jvm",
            "spring_boot": find_version(
                [
                    r"spring-boot-starter-parent</artifactId>\s*<version>([^<]+)</version>",
                    r'springBootVersion\s*=\s*"([^"]+)"',
                    r"org\.springframework\.boot[^\n]*?version\s*[:=]\s*[\"']?([0-9][^\"'\s]+)",
                ],
                text,
            ),
            "backbase": bool(re.search(r"com\.backbase", text)),
        }
        signals["stacks"].append(entry)

    if package_json.exists():
        text = read_text(package_json)
        signals["files"].append("package.json")
        deps = text
        entry = {
            "stack": "node",
            "angular": find_version([r'"@angular/core"\s*:\s*"([^"]+)"'], deps),
            "react": find_version([r'"react"\s*:\s*"([^"]+)"'], deps),
            "backbase_frontend": '"@backbase/' in deps,
            "has_angular_json": angular_json.exists(),
        }
        signals["stacks"].append(entry)
        if angular_json.exists():
            signals["files"].append("angular.json")

    if pyproject.exists() or requirements.exists():
        text = read_text(pyproject if pyproject.exists() else requirements)
        signals["files"].append(
            "pyproject.toml" if pyproject.exists() else "requirements.txt"
        )
        signals["stacks"].append(
            {
                "stack": "python",
                "fastapi": bool(re.search(r"fastapi", text, re.I)),
                "django": bool(re.search(r"django", text, re.I)),
            }
        )

    for name in ("AGENTS.md", "CONTRIBUTING.md"):
        if (root / name).exists():
            signals["files"].append(name)

    return signals


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not root.is_dir():
        print(f"Not a directory: {root}", file=sys.stderr)
        return 1
    print(json.dumps(analyze(root), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
