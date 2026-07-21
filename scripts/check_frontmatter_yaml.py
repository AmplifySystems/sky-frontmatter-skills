#!/usr/bin/env python3
"""Check that Markdown front matter is parseable YAML when PyYAML is available."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from frontmatter_lib import extract_frontmatter, iter_markdown_files, parse_simple_frontmatter

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    yaml = None


def validate_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    frontmatter, _ = extract_frontmatter(text)
    if not frontmatter:
        return ""

    if yaml is None:
        parsed = parse_simple_frontmatter(frontmatter)
        return "" if parsed else f"{path}: front matter exists but no keys were parsed"

    try:
        yaml.safe_load(frontmatter)
        return ""
    except Exception as exc:
        return f"{path}: {exc}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".", help="Markdown file or directory to check")
    args = parser.parse_args()

    root = Path(args.path)
    files = sorted(iter_markdown_files(root))
    errors = [err for err in (validate_file(path) for path in files) if err]

    mode = "PyYAML" if yaml is not None else "dependency-free parser"
    print(f"Checked {len(files)} markdown files with {mode}.")

    if not errors:
        print("All front matter YAML checks passed.")
        return 0

    print("\nFront matter YAML issues:")
    for err in errors:
        print(f" - {err}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
