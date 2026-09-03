---
name: republic-librarian
description: Knowledge governance for The Republic in Obsidian. Existing Librarian rules remain authoritative (propose don't destroy; every 00_DROP item gets exactly one outcome) and are extended with LLM-Wiki behavior — for each valuable item, decide whether it UPDATES, CONTRADICTS, STRENGTHENS, or SUPERSEDES existing knowledge, CHANGES a project, CREATES a relationship, REVEALS a reusable concept, or CREATES a decision, then update the canonical note rather than adding a random one. Use for every knowledge, evidence, or decision item.
version: 1.0.0
department: knowledge
tags: [republic, librarian, obsidian, canonical, llm-wiki]
---

# Librarian — existing rules plus LLM-Wiki behavior

(SPEC §17). Existing Librarian rules in the vault are authoritative and unchanged:
- **Propose, don't destroy.**
- **Every `00_DROP` item gets exactly one outcome.**
- Canonical decisions: `status: active`, `canonical: true`. Superseded decisions stay,
  linked from their successor, never overwritten.

## Added: the LLM-Wiki pass
After judging an item valuable (per existing triage rules), ask in order:

| Question | If yes → action |
|---|---|
| UPDATES existing knowledge? | Edit the canonical note; add a dated changelog line; link the source |
| CONTRADICTS existing knowledge? | Do not overwrite. Add a `contradiction` block to the canonical note with both claims and sources; open an `ops` card if it affects a live decision |
| STRENGTHENS something? | Append evidence to the canonical note's `evidence` list with source and date |
| SUPERSEDES something? | Create the successor; set the old note `status: superseded`, `superseded_by:`; link both ways |
| CHANGES a project? | Update the project note's status/next step; link the source |
| CREATES a relationship? | Add wikilinks both directions with a one-line reason |
| REVEALS a reusable concept? | Create or update one concept note; link from every source that revealed it |
| CREATES a decision? | Create a decision note (`status: proposed`); Rachel acknowledgement moves it to `active`, `canonical: true` |

Raw/original material is preserved at its ingest location and linked from every note
it touched. The pass edits canonical notes; it does not manufacture new orphan notes.

## Inputs
- Documents → via `republic-anydoc` first (Markdown only enters here)
- Evidence notes from `republic-learning-loop` and `republic-distribution` (reputation)
- Socrates captures, research briefs, QA reports, acceptance decisions

## After every meaningful change
Call `republic-qmd` to reindex the affected collection. Archive/discard material is
tagged so QMD excludes it from normal retrieval.

## Boundaries
- Never deletes. Never sets `canonical: true` without Rachel's acknowledgement.
- Never resolves a contradiction by choosing a side; it surfaces it.
- Worker tier: `local` for classification and extraction; `frontier` for canonical
  edits that change meaning.
