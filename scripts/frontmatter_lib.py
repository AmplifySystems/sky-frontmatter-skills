#!/usr/bin/env python3
"""Shared helpers for simple Markdown front matter scripts."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


REQUIRED_FIELDS = [
    "title",
    "status",
    "created",
    "updated",
    "type",
    "category",
    "rag_tier",
    "tags",
    "file_path",
    "related",
]


def iter_markdown_files(root: Path) -> Iterable[Path]:
    ignored = {".git", "node_modules", "dist", "tmp", "reports"}
    if root.is_file() and root.suffix.lower() == ".md":
        yield root
        return

    for path in root.rglob("*.md"):
        if ignored.isdisjoint(path.parts):
            yield path


def extract_frontmatter(text: str) -> Tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return "", text
    return parts[1], parts[2]


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value[0:1] in {"'", '"'} and value[-1:] == value[0]:
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in inner.split(",")]
    return value


def parse_simple_frontmatter(frontmatter: str) -> Dict[str, Any]:
    """Parse the common front matter subset used by these skills.

    This is intentionally small and dependency-free. If a repository needs full
    YAML support, install PyYAML and use check_frontmatter_yaml.py.
    """

    data: Dict[str, Any] = {}
    current_key = ""
    for raw_line in frontmatter.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue

        item = re.match(r"^\s*-\s+(.*)$", line)
        if item and current_key:
            data.setdefault(current_key, [])
            if isinstance(data[current_key], list):
                data[current_key].append(parse_scalar(item.group(1)))
            continue

        match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", line)
        if match:
            current_key = match.group(1)
            value = match.group(2) or ""
            data[current_key] = [] if value == "" else parse_scalar(value)
            continue

        current_key = ""

    return data


def read_doc(path: Path) -> Dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    frontmatter, body = extract_frontmatter(text)
    data = parse_simple_frontmatter(frontmatter) if frontmatter else {}
    return {
        "path": path,
        "has_frontmatter": bool(frontmatter),
        "frontmatter": frontmatter,
        "body": body,
        "data": data,
    }
