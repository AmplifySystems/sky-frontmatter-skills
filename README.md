---
title: Frontmatter Skills Kit
status: active
created: '2026-07-21'
updated: '2026-07-27'
type: index
category: documentation-as-code
rag_tier: '1'
tags:
  - frontmatter
  - documentation-as-code
  - codex-skills
  - cursor-skills
  - knowledge-graph
file_path: README.md
related:
  - references/frontmatter-schema.md
  - references/index-registration.md
---

# Frontmatter Skills Kit

Portable Codex/Cursor skills for turning Markdown documentation into durable, indexable, human-readable knowledge infrastructure.

The core idea is simple: write Markdown with structured front matter so humans can navigate it, agents can search it, and scripts can keep indexes, relationships, and RAG ingestion clean.

## Skills

| Skill | Use it when |
| --- | --- |
| [`auto-doc-indexing`](skills/auto-doc-indexing/SKILL.md) | Creating or auditing Markdown docs that need complete YAML front matter, related links, and parent index registration. |
| [`documentation-as-code-persist-spec`](skills/documentation-as-code-persist-spec/SKILL.md) | Turning long chat answers, specs, runbooks, or architecture notes into repo Markdown instead of losing them in chat. |
| [`doc-frontmatter-knowledge-tree`](skills/doc-frontmatter-knowledge-tree/SKILL.md) | Wiring `tags`, `related`, category, and RAG metadata into a navigable knowledge tree for humans and machines. |
| [`markdown-toc-section-nav`](skills/markdown-toc-section-nav/SKILL.md) | Adding stable table-of-contents anchors and Prev/Next navigation to long Markdown docs. |

## Scripts

Run from the repo root you want to inspect:

```bash
python3 path/to/frontmatter-skills-kit/scripts/audit_frontmatter.py docs
python3 path/to/frontmatter-skills-kit/scripts/check_frontmatter_yaml.py docs
python3 path/to/frontmatter-skills-kit/scripts/generate_doc_index.py docs --output docs/INDEX.generated.md
```

The scripts use Python standard library only. If `PyYAML` is installed, `check_frontmatter_yaml.py` also performs a real YAML parse.

## Front Matter Shape

See [`references/frontmatter-schema.md`](references/frontmatter-schema.md) for the canonical field set and [`examples/minimal-doc.md`](examples/minimal-doc.md) for a complete example.

## Install

Copy or symlink the folders in `skills/` into your agent skill directory:

```bash
cp -R skills/* ~/.codex/skills/
```

For Cursor-style setups, copy them to your project-local skill folder:

```bash
mkdir -p .cursor/skills
cp -R skills/* .cursor/skills/
```

## Public Safety

These skills are designed for public repositories. Do not place API keys, secrets, private tokens, customer PII, or private workspace paths in front matter, examples, generated indexes, or script logs.

## Built by Amplify Systems

This kit was created by Amplify Systems while building practical AI operating systems for teams that want their knowledge, workflows, and customer experience to compound instead of scatter.

We help teams tighten their **Value Engines**: the connected systems that attract the right people, deliver on the promise, and turn useful work into reusable momentum.

Learn more at [amplifysystems.io](https://amplifysystems.io), or read [AMPLIFY-SYSTEMS.md](./AMPLIFY-SYSTEMS.md) for the short version.
