---
name: republic-learning-loop
description: Closes the loop from publish to knowledge — captures performance at MEASURED from GHL, native analytics, Search Console, and ad platforms; files an evidence note with the Librarian; and only when a pattern reaches the minimum sample in kanban/pipeline.yaml proposes a canonical brand-knowledge update. Use when a card enters MEASURED and for periodic pattern review. Never rewrites Republic per post.
version: 1.0.0
department: knowledge
tags: [republic, learning, analytics, evidence, patterns]
---

# The learning loop — evidence accumulates, then knowledge changes

```
publish → performance → what happened? → Librarian → evidence accumulates
       → meaningful pattern? → update canonical knowledge
```
(SPEC §26, §27). Measurement uses GHL data, native social analytics, Search Console,
ad-platform data. PostHog is not installed in v1.

## Procedure — per card (MEASURED)
1. At `measurement_window_days` after publish, pull metrics per platform version:
   reach/views, retention or watch time, saves/shares, comments, DMs (via
   `republic-distribution`), clicks, leads, bookings.
2. Record on the card. Attach the attributes under test from the card: hook type,
   opening style (demonstration-first vs talking), format, duration band, objective,
   writing mode, angle motivation, template used, publish time.
3. File one **evidence note** with `republic-librarian`: `{brand, card, platform,
   attributes, metrics, window}`. Observations only. No conclusion in a single note.
4. Move the card to DONE.

## Procedure — pattern review (weekly)
1. For each brand and attribute, count evidence notes. If count <
   `learning.min_sample`, report "insufficient evidence" and stop for that attribute.
2. At or above the sample, compare attribute values on the primary metric for the
   objective. Report the difference with the sample size and the spread.
3. Only a substantial, consistent difference becomes a **proposed canonical update**
   to `brands/<brand>/` (e.g. `voice.md` or a `learned-patterns.md` note) via the
   Librarian's SUPERSEDES/STRENGTHENS pass, `status: proposed` until Rachel
   acknowledges (`learning.canonical_requires`).

## The rule, in one example
Not: "This Reel got fewer views, therefore question hooks don't work."
But: "Across 18 Physically Meta Reels, demonstration-first openings substantially
outperform static talking introductions." That becomes durable brand knowledge.

## Boundaries
- Never edits a skill, template, or platform norms file directly. Proposes to the
  Librarian; Rachel acknowledges; a v1.1 change applies it if it touches SPEC.
- Never draws a conclusion below `min_sample`.
- Worker tier: `local` for metric pulls and counting; `frontier` for the pattern
  write-up Rachel will read.
