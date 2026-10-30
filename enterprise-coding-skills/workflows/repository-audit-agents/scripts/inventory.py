#!/usr/bin/env python3
"""Bounded, read-only repository inventory. Does NOT audit code quality."""
import json
import os
import sys
from pathlib import Path

MARKERS = {'pom.xml','build.gradle','build.gradle.kts','settings.gradle.kts','package.json','angular.json','nx.json','pyproject.toml','requirements.txt','Pipfile','go.mod','Cargo.toml','pubspec.yaml','Podfile','Package.swift','Gemfile','Dockerfile','AGENTS.md','gradle.properties','global.json'}
EXTENSIONS = {'.csproj','.sln','.slnx','.xcodeproj','.xcworkspace','.swift','.kt','.java','.py','.ts','.tsx','.jsx','.cs','.go','.rs','.dart'}
SKIP = {'.git','node_modules','vendor','dist','build','target','.venv','venv','.next','.gradle','.idea','.terraform','.gitlab','coverage'}

def main():
    root = Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
    if not root.is_dir():
        raise SystemExit('Not a directory')
    samples = []
    counts = {}
    truncated = False
    visited = 0
    for base, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP and not d.startswith('.cache'))
        for f in sorted(files):
            visited += 1
            if visited > 100000:
                truncated = True
                break
            p = Path(base)/f
            ext = p.suffix.lower()
            if ext in EXTENSIONS:
                counts[ext] = counts.get(ext,0)+1
            if f in MARKERS or ext in {'.csproj','.sln','.slnx'}:
                if len(samples)<300:
                    samples.append(p.relative_to(root).as_posix())
                else:
                    truncated = True
        if visited > 100000:
            break
    print(json.dumps({'root': str(root), 'marker_files': samples, 'source_extension_counts': counts, 'visited_file_count': visited, 'truncated': truncated, 'note':'Inventory only; inspect files and version manifests manually. No secrets scanned or copied.'},indent=2))

if __name__=='__main__':
    main()
