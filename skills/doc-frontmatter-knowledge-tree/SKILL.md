---
name: doc-frontmatter-knowledge-tree
description: Connect Markdown front matter to a human and machine knowledge graph. Use when wiring tags, related links, categories, RAG tiers, parent indexes, document hubs, graph views, or browse paths across a documentation repo.
---

# Doc Frontmatter Knowledge Tree

## Purpose

Turn isolated Markdown files into a navigable knowledge tree. A useful doc should be findable through:

- A parent index or hub.
- `related` front matter links.
- Consistent `tags`.
- `category`, `type`, and `rag_tier` fields.
- Optional semantic tags, modules, owners, and supersession links.

## Procedure

1. Identify the document's parent branch: product, project, module, knowledge area, or operating system.
2. Normalize tags across sibling docs. Prefer stable kebab-case tokens over one-off variants.
3. Add `related` links in both directions when practical: child to parent and parent or sibling index back to child.
4. Use `rag_tier` intentionally. Do not mark every file tier `'1'`.
5. Keep index descriptions short enough to scan.
6. For long docs, pair with `markdown-toc-section-nav`.
7. Generate or refresh a docs index if the repo uses generated indexes:

```bash
python3 path/to/frontmatter-skills-kit/scripts/generate_doc_index.py docs --output docs/INDEX.generated.md
```

## Tag Guidelines

Use tags that help both humans and machines filter:

```yaml
tags:
  - documentation-as-code
  - frontmatter
  - onboarding
  - runbook
```

Avoid near-duplicates such as `frontmatter`, `front-matter`, and `front_matter` in the same repo. Pick one spelling and keep it consistent.

## Relationship Guidelines

Good `related` links answer at least two of these questions:

- What parent index owns this doc?
- What system or architecture doc governs it?
- What runbook executes it?
- What sibling doc continues the same topic?
- What superseded doc explains the history?

## Output Standard

When you update a knowledge tree, report the front matter changes, index links changed, and any remaining orphan docs.
