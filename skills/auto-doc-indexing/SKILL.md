---
name: auto-doc-indexing
description: Add or audit YAML front matter and index registration for Markdown documentation. Use when creating docs, fixing missing metadata, adding related links, updating parent INDEX files, or preparing docs for search, RAG, Notion, static-site, or agent indexing.
---

# Auto Doc Indexing

## Procedure

1. Find the nearest existing parent `INDEX.md`, `README.md`, docs hub, or table of contents before creating a new document.
2. Add front matter using the schema in `references/frontmatter-schema.md` from this package.
3. Set `file_path` to the exact path from the repository root.
4. Add at least two `related` paths that connect the document to parent, sibling, upstream, or downstream docs.
5. Add tags as lowercase kebab-case facets that can be used for search and filtering.
6. Register the new or updated doc in the parent index with one factual description line.
7. Run the audit script against the changed docs when available:

```bash
python3 path/to/sky-frontmatter-skills/scripts/audit_frontmatter.py path/to/docs
```

## Required Front Matter

```yaml
---
title: Human-readable title
status: active
created: 'YYYY-MM-DD'
updated: 'YYYY-MM-DD'
type: reference
category: documentation
rag_tier: '1'
tags:
  - kebab-case-tag
file_path: path/from/repo/root/document.md
related:
  - path/to/parent-or-sibling.md
  - path/to/supporting-doc.md
---
```

## RAG Tier Guidelines

| Tier | Use for |
| --- | --- |
| `'1'` | Canonical architecture, runbooks, protocols, indexes, active implementation docs. |
| `'2'` | Supporting references, meeting notes, drafts that are still useful. |
| `'3'` | Archival, superseded, exploratory, or low-signal context. |

## Index Registration

If a parent index exists, add a row or short section. If it does not exist, update the nearest parent index instead of creating a new index unless the folder has enough docs to justify one.

Prefer factual routing text:

```markdown
| [Document Title](./DOCUMENT.md) | runbook | active | How to operate the workflow safely. |
```

## Completion Check

- `title`, `status`, `created`, `updated`, `type`, `category`, `rag_tier`, `tags`, and `file_path` are present.
- `related` has at least two useful paths.
- The parent index links to the doc.
- Tags are consistent with sibling docs.
- No secrets, private tokens, private customer data, or machine-local paths appear in front matter.
