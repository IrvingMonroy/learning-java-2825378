---
name: republic-anydoc
description: Converts documents (DOCX, PPTX, XLSX, EPUB, PDF, CSV and similar) to Markdown with AnyDoc so the Librarian can interpret them. Pure conversion — AnyDoc does not decide where knowledge belongs. Use whenever a non-Markdown document enters CONTENT_DROP/ or 00_DROP.
version: 1.0.0
department: knowledge
tags: [republic, anydoc, conversion, markdown]
---

# AnyDoc — make it machine-readable, nothing more

`DOCX / PPTX / XLSX / EPUB / PDF / CSV → AnyDoc → Markdown → Librarian` (SPEC §18)

## Procedure
1. Receive a document path from `republic-triage`. Leave the original in place.
2. Run AnyDoc to Markdown. Preserve headings, tables, and image references. Write to
   `<drop>/_converted/<original-name>.md` with front matter `{source, converted,
   converter: anydoc, pages|sheets}`.
3. Sanity check: non-empty, heading count > 0 or table count > 0 for structured
   sources. If the output is empty or garbled (scanned PDF without text layer), mark
   `conversion: failed-needs-ocr` and inform Socrates. Do not guess content.
4. Hand the Markdown path to `republic-librarian`.

## Boundaries
- Never files, tags, summarizes, or decides destination.
- Never alters the original document.
- Worker tier: none required for conversion; `local` for the sanity check summary line.
