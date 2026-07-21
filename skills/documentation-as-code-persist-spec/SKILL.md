---
name: documentation-as-code-persist-spec
description: Persist substantive chat output into repository Markdown with front matter, links, and index registration. Use when a response is becoming a durable spec, runbook, architecture note, protocol, checklist, or implementation guide that should survive beyond the chat.
---

# Documentation as Code Persist Spec

## Decision Rule

Persist the work to Markdown when the answer would otherwise become more than about 15 lines of actionable architecture, runbook steps, schema notes, operational procedure, or implementation planning.

## Procedure

1. Search before creating. Look for an existing canonical doc, parent index, or adjacent folder.
2. Choose the smallest durable location that future humans and agents would naturally search.
3. Write or update the Markdown file with complete front matter.
4. Add `related` links to the parent index, nearest architecture/reference doc, and any immediate implementation docs.
5. Ripple one link into the parent index or docs hub.
6. Keep the chat response short and link to the file instead of duplicating the full spec.
7. Run front matter validation or audit scripts when available.

## Location Heuristics

- `docs/architecture/`: system shape, canonical models, cross-cutting decisions.
- `docs/implementation/`: operating runbooks, checklists, deployment steps, workflow instructions.
- `docs/reference/`: glossaries, schemas, field definitions, stable lookup docs.
- `docs/protocols/`: required processes and safety rules.
- `docs/indexes/` or `INDEX.md`: navigation and discovery surfaces.

Follow the repository's existing layout over these defaults when a local pattern is obvious.

## Chat Response Pattern

After writing the doc, answer with:

- The file path.
- The important change or decision captured.
- Any verification run.
- Any real blocker.

Do not paste the entire saved document into chat.

## Safety

For public repos, scrub front matter and examples for secrets, bearer tokens, private workspace paths, customer PII, and vendor-specific identifiers that should not be published.
