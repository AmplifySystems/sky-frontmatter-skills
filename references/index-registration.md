---
title: Index Registration
status: active
created: '2026-07-21'
updated: '2026-07-21'
type: reference
category: documentation-as-code
rag_tier: '1'
tags:
  - indexes
  - documentation-as-code
  - navigation
file_path: references/index-registration.md
related:
  - README.md
  - references/frontmatter-schema.md
---

# Index Registration

Every substantive Markdown file should be findable from at least one parent index.

## Parent Index Row

Use a compact table when a folder has many docs:

```markdown
| Doc | Type | Status | Notes |
| --- | --- | --- | --- |
| [Document Title](./DOCUMENT.md) | runbook | active | One sentence about why it exists. |
```

Use a short list when the folder is small:

```markdown
### [Document Title](./DOCUMENT.md)

One sentence about why it exists.
```

## Registration Checklist

- Add or update the document front matter.
- Add a parent `INDEX.md` or update the nearest existing index.
- Add at least two `related` paths that connect parent, sibling, upstream, or downstream docs.
- Keep link paths repo-relative or relative to the index file. Pick one convention per repo.
- Keep descriptions factual. Indexes are routing surfaces, not marketing pages.

## Generated Indexes

Generated indexes should say they are generated and identify the command used. Do not hand-edit generated output unless you intend to make it canonical.
