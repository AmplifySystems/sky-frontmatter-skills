#!/usr/bin/env python3
"""Audit Markdown files for documentation-as-code front matter completeness."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from frontmatter_lib import REQUIRED_FIELDS, iter_markdown_files, read_doc


def audit_path(root: Path) -> int:
    files = sorted(iter_markdown_files(root))
    failures = []

    for path in files:
        doc = read_doc(path)
        data = doc["data"]
        if path.name == "SKILL.md" and {"name", "description"}.issubset(data):
            continue
        if not doc["has_frontmatter"]:
            failures.append((path, "missing front matter"))
            continue

        missing = [field for field in REQUIRED_FIELDS if field not in data or data[field] in ("", [])]
        if missing:
            failures.append((path, "missing fields: " + ", ".join(missing)))

        tags = data.get("tags", [])
        if tags and not isinstance(tags, list):
            failures.append((path, "tags should be a list"))

        related = data.get("related", [])
        if related and not isinstance(related, list):
            failures.append((path, "related should be a list"))
        elif len(related) < 2:
            failures.append((path, "related should include at least 2 paths"))

        file_path = data.get("file_path")
        if file_path and file_path != str(path):
            try:
                relative = str(path.relative_to(Path.cwd()))
            except ValueError:
                relative = str(path)
            if file_path != relative:
                failures.append((path, f"file_path mismatch: {file_path}"))

    print(f"Audited {len(files)} markdown files under {root}")
    if not failures:
        print("All required front matter checks passed.")
        return 0

    print("\nFront matter issues:")
    for path, message in failures:
        print(f" - {path}: {message}")
    print(f"\nTotal issues: {len(failures)}")
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".", help="Markdown file or directory to audit")
    args = parser.parse_args()
    return audit_path(Path(args.path))


if __name__ == "__main__":
    sys.exit(main())
