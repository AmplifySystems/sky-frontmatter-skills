---
name: markdown-toc-section-nav
description: Add stable table-of-contents anchors and Prev/Next navigation rows to long Markdown documents. Use for runbooks, protocols, specs, or guides where readers need to move between numbered sections without excessive scrolling.
---

# Markdown TOC Section Nav

## Procedure

1. Confirm the document has a table of contents with links to major sections.
2. Replace a plain `## Table of contents` heading with a stable HTML anchor:

```html
<h2 id="table-of-contents">Table of contents</h2>
```

3. Add a navigation row immediately before each major numbered section.
4. Match link anchors to the table of contents anchors already used by the renderer.
5. For the final section, point `Next` to `#related-documents`, the next major section, or `#table-of-contents`.

## Nav Row Pattern

```html
<p align="center"><a href="#table-of-contents">Table of contents</a> · <a href="#previous-section">Prev</a> · <a href="#next-section">Next</a></p>
```

For the first section, omit `Prev` or point it to the table of contents.

For a related-documents block with no Markdown heading, use:

```html
<h2 id="related-documents">Related documents</h2>
```

## Completion Check

- Every TOC link resolves.
- Every major numbered section has a nav row.
- Section anchors match the renderer's slug convention.
- Nav rows do not interrupt code blocks, tables, or admonitions.
- The document still renders cleanly in GitHub Markdown.
