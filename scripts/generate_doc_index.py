#!/usr/bin/env python3
"""Generate a Markdown index table from front matter fields."""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

from frontmatter_lib import iter_markdown_files, read_doc


def clean_cell(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value).replace("|", "\\|").replace("\n", " ")


def generate_index(root: Path, output: Path | None = None) -> str:
    rows = []
    for path in sorted(iter_markdown_files(root)):
        if output and path.resolve() == output.resolve():
            continue
        doc = read_doc(path)
        data = doc["data"]
        title = clean_cell(data.get("title") or path.stem.replace("-", " ").title())
        doc_type = clean_cell(data.get("type"))
        status = clean_cell(data.get("status"))
        tier = clean_cell(data.get("rag_tier"))
        tags = clean_cell(data.get("tags"))
        rows.append((str(path), title, doc_type, status, tier, tags))

    today = dt.date.today().isoformat()
    lines = [
        "---",
        "title: Generated Documentation Index",
        "status: active",
        f"created: '{today}'",
        f"updated: '{today}'",
        "type: index",
        "category: documentation-as-code",
        "rag_tier: '2'",
        "tags:",
        "  - generated-index",
        "  - documentation-as-code",
        f"file_path: {output or 'INDEX.generated.md'}",
        "---",
        "",
        "# Generated Documentation Index",
        "",
        f"Generated from `{root}`.",
        "",
        "| Doc | Type | Status | RAG | Tags |",
        "| --- | --- | --- | --- | --- |",
    ]

    for path, title, doc_type, status, tier, tags in rows:
        lines.append(f"| [{title}]({path}) | {doc_type} | {status} | {tier} | {tags} |")

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=".", help="Markdown directory to index")
    parser.add_argument("--output", help="Write the generated index to this file")
    args = parser.parse_args()

    output = Path(args.output) if args.output else None
    content = generate_index(Path(args.path), output)

    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(content, encoding="utf-8")
        print(f"Wrote {output}")
    else:
        print(content)
    return 0


if __name__ == "__main__":
    sys.exit(main())
