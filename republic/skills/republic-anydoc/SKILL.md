---
name: republic-anydoc
description: Adds AnyDoc in front of the existing Librarian so incoming documents (DOCX, PPTX, XLSX, EPUB, PDF, CSV and similar) become Markdown the Librarian can interpret. Pure conversion next to the original; AnyDoc never decides where knowledge belongs. Use whenever a non-Markdown document lands in the existing drop folder.
version: 1.0.0
batch: 3
adds_to: existing Librarian intake
replaces: nothing
preserves: [existing Librarian rules, original documents in place, existing drop folder]
tags: [republic, anydoc, conversion, librarian, batch-3]
---

# AnyDoc — make it machine-readable, nothing more

`DOCX / PPTX / XLSX / EPUB / PDF / CSV → AnyDoc → Markdown → existing Librarian` (SPEC §3)

## Procedure
1. Detect a non-Markdown document in the existing drop folder. Leave it in place.
2. Convert with AnyDoc to `<same folder>/_converted/<name>.md`, front matter
   `{source, converted, converter: anydoc, pages|sheets}`. Preserve headings, tables,
   image references.
3. Sanity check: non-empty; headings or tables present for structured sources. Empty or
   garbled (scanned PDF without a text layer) → mark `conversion: failed-needs-ocr`,
   tell Socrates once. Never guess content.
4. Hand the Markdown path to the existing Librarian, which applies its own rules plus
   the LLM-Wiki patch.

## Boundaries
- Never files, tags, summarizes, or chooses a destination.
- Never alters the original.
