---
title: Public Repo Safety
status: active
created: '2026-07-27'
updated: '2026-07-27'
type: protocol
category: public-safety
rag_tier: '1'
tags:
  - public-safety
  - frontmatter
  - documentation-as-code
file_path: AGENTS.md
related:
  - README.md
  - references/frontmatter-schema.md
---

# Public Repo Safety

This repository is designed to be safe for public sharing.

## Do Not Add Private Material

Do not commit secrets, API keys, bearer tokens, private workspace paths, customer PII, internal project names, private URLs, account IDs, credential IDs, or local machine details.

This applies to:

- YAML front matter
- examples
- generated indexes
- script output
- screenshots
- setup notes
- issue and pull request text

## Use Generic Examples

Use neutral placeholders such as:

- `docs/example-guide.md`
- `example-system`
- `example-customer`
- `https://example.com`
- `YOUR_PROJECT_NAME`

Do not use real customer names, internal system names, or private repository paths.

## Keep Skills Portable

Skills in this package should teach reusable documentation workflows, not one organization's private operating model. If a workflow needs local vocabulary, describe how users can add their own tags, categories, and schema extensions.

## Before Publishing

Run the front matter audit scripts and scan changed files for private names, private paths, tokens, and private identifiers. When in doubt, replace the detail with a generic placeholder.
