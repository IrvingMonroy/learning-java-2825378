# Batch 3 — Knowledge

Adds: the Librarian LLM-Wiki instruction patch (`upgrades/librarian-llm-wiki.md`) and
`republic-anydoc`.

## Preconditions
- Batch 2 gate passed.
- A copy of the current Librarian instructions saved before patching (for the
  preserved-pieces diff in the Definition of Done).

## Steps
1. Append `upgrades/librarian-llm-wiki.md` to the existing Librarian instructions.
   Do not remove or reorder existing rules.
2. `./scripts/install.sh --batch 3`
3. Drop three documents (a PDF, a DOCX, a spreadsheet) and two ordinary notes. Confirm
   AnyDoc converts and the Librarian applies the eight-question pass, updating
   canonical notes and leaving originals intact.
4. Reindex QMD as the Librarian already does today; confirm archive/discard exclusion.

## Gate
QA PASS; every existing Librarian rule still present verbatim; no original destroyed;
canonical notes updated rather than duplicated.
