---
name: republic-qmd
description: Keeps QMD in its intended role as The Republic's retrieval index over Obsidian — reindexes the relevant collection after meaningful Librarian changes, keeps archive/discard material excluded from normal retrieval, and answers retrieval requests from other skills. Use after Librarian changes and for any knowledge lookup. QMD is not a database-of-everything.
version: 1.0.0
department: knowledge
tags: [republic, qmd, retrieval, index]
---

# QMD — retrieval, not storage

Obsidian = durable knowledge. QMD = retrieval/index. Librarian = governance.
Hermes = reasoning/orchestration. (SPEC §19)

## Procedure — reindex
1. Triggered by `republic-librarian` with the list of changed note paths.
2. Map paths to collections (brand, project, decisions, evidence, concepts).
3. Reindex only those collections. Log collection, note count, duration.
4. Confirm exclusions: any note tagged `archive` or `discard`, and anything under an
   archive folder, is excluded from default retrieval. Included only when a caller
   passes `include_archived: true` explicitly.

## Procedure — retrieval
Accept `{query, collections?, brand?, since?}`. Return ranked note paths with the
matching passage and note front matter. Never return archive/discard without the
explicit flag. Never synthesize an answer; that is the caller's job.

## Boundaries
- Stores no content of its own. If a caller asks QMD to "remember" something, route
  to `republic-librarian`.
- Index failure → report to Socrates; retrieval falls back to the last good index and
  says so in the response header.
