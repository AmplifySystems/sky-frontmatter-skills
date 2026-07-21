---
title: Frontmatter Schema
status: active
created: '2026-07-21'
updated: '2026-07-21'
type: reference
category: documentation-as-code
rag_tier: '1'
tags:
  - frontmatter
  - schema
  - documentation-as-code
file_path: references/frontmatter-schema.md
related:
  - README.md
  - references/index-registration.md
---

# Frontmatter Schema

Use this schema for Markdown documents that should be easy for humans, search tools, RAG pipelines, and agents to discover.

## Minimum Required Fields

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

## Field Rules

| Field | Rule |
| --- | --- |
| `title` | Use a searchable human title under 100 characters when practical. |
| `status` | Prefer `active`, `draft`, `deprecated`, `archived`, `complete`, or `superseded`. |
| `created` | Quote the date as `'YYYY-MM-DD'`. |
| `updated` | Quote the date as `'YYYY-MM-DD'` and change it when the document changes. |
| `type` | Use a stable content type such as `index`, `reference`, `architecture`, `implementation`, `runbook`, `protocol`, `playbook`, `template`, `article`, or `specification`. |
| `category` | Use the broad knowledge area or business domain. Keep it lowercase and hyphenated. |
| `rag_tier` | Use `'1'` for canonical docs, `'2'` for useful supporting docs, and `'3'` for archival/background docs. |
| `tags` | Use lowercase kebab-case facets that a human might browse and an agent might filter. |
| `file_path` | Use the exact repo-relative path to the current file. |
| `related` | Include at least two repo-relative links to parent, sibling, upstream, or downstream docs. |

## Optional Fields

```yaml
audience:
  - agents
  - operators
canonical_url: https://example.com/docs/page
owners:
  - docs-team
semantic_tags:
  - domain:documentation
  - type:reference
modules:
  - knowledge-base
supersedes:
  - old-doc.md
superseded_by: newer-doc.md
impact_filters:
  - DOCS-AS-CODE
```

Use optional fields only when they improve routing, ownership, versioning, or search. Avoid front matter bloat that nobody reads.

## Public Repo Safety

Never include secret values, bearer tokens, private customer data, private workspace paths, or hidden infrastructure identifiers in front matter. Prefer stable slugs over IDs when publishing open-source examples.
