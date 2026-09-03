---
name: republic-triage
description: Registers every incoming item (CONTENT_DROP media, Socrates request, new review, ad question) as exactly one Kanban card, types it, sets brand and objective hypothesis, and routes it to the owning department. Use whenever something new arrives that The Republic should work on. Never does the work itself.
version: 1.0.0
department: republic
tags: [republic, intake, kanban]
---

# Republic Triage

**Job:** turn arrivals into state. One arrival → one card in `TRIAGE`. Nothing enters
The Republic without a card. (SPEC §7, §21)

## Inputs
- New files in `CONTENT_DROP/` (video, audio, images, documents)
- Socrates captures (`socrates-*.md`) and direct requests
- New GHL review events (from `republic-distribution`)
- Paid/search requests from Rachel

## Procedure
1. **Detect and register.** For each arrival create a card from `kanban/card-template.md`.
   Copy Rachel's words verbatim into `## Intake`. Preserve the original file; never move
   or rename raw media.
2. **Type the card.** `content` (media or idea for posts), `search` (SEO ask),
   `paid` (ads ask), `knowledge` (documents, notes with no publishing intent),
   `ops` (system/GHL workflow ask). If two types apply, open two cards and link them.
3. **Set brand.** Honor any `brand:` line. Otherwise infer from context and mark
   `brand-inferred: true` so the STRATEGY step confirms it. Worker tier: `local`.
4. **Objective hypothesis.** Guess the objective (CONNECT / TEACH / STORY /
   THOUGHT_LEADERSHIP / SELL / BOOK / OPT_IN / CONVERT). Mark it a hypothesis. STRATEGY
   fixes it; triage never chooses writing mode.
5. **Route.** Media → `republic-video-intake` first, then RESEARCH. Documents →
   `republic-anydoc` → `republic-librarian`. Reviews → `republic-distribution`
   reputation flow. Search → `republic-search`. Paid → `republic-paid`.
6. **Report.** Tell Socrates: card ID, type, brand, next column. Nothing else.

## Boundaries
- Never writes, edits, publishes, or approves.
- Never deletes or moves raw material (Librarian rule: propose, don't destroy).
- If `CONTENT_DROP/` is unreachable or Kanban rejects the card, stop and report the
  error on the Socrates channel. Do not queue silently.
