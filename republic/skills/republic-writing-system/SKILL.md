---
name: republic-writing-system
description: 03_CONTENT's single consolidated writing system. Four stages — A Voice DNA from the brand directory, B blank-page generation of starting material, C credible angle generation grounded in customer evidence, D writing mode chosen by objective (BRAND WRITING vs DIRECT RESPONSE) — followed by the mandatory Writing QA "would this person actually say this?" check. Use for any drafting, caption, hook, or copy task. Replaces all separate "killer" writing skills.
version: 1.0.0
department: 03_CONTENT
tags: [republic, writing, voice, copy, brand]
---

# Republic Writing System

One system. Not Blank Page Killer + Ghostwriter Killer + 72 Reasons + Copywriter
Killer + Slop Killer + Hook/Caption/CTA agents competing. Their best principles live
here as stages. (SPEC §4, §5)

## Preconditions
- Card has a Research Brief and a fixed `objective` from STRATEGY.
- `brands/<brand>/` exists with all eight schema entries. If `voice.md` is still a
  template (contains `TODO-SOURCE`), stop: Voice DNA must come from real human material
  before any draft is written. Report to Socrates as a blocking item.

## Stage A — Voice DNA (read, never invent)
Load `brand.md, voice.md, audience.md, offers.md, proof.md, objections.md,
prohibited-claims.md` and skim `approved-examples/`. Extract into working memory:
recurring phrases, preferred and disliked vocabulary, cadence, humor, polish level.
Details: `references/voice-dna.md`.

## Stage B — Blank-page generation
Only when no draft exists. Produce starting material: 3 concepts, 5 hooks, 1 outline
per concept, story directions, structure options, one rough first draft. Starting
material is not conversion copy. Worker tier: `local` acceptable for volume,
`frontier` for anything Rachel will see. Details: `references/blank-page.md`.

## Stage C — Angle generation
Ask: *what credible reasons would different segments of this audience care?*
Ground every angle in the brief's customer language, reviews, DMs, comments, search
intent, or an actual offer characteristic from `offers.md`. Cluster into motivations
(3–7). Discard any angle without a source. Details: `references/angles.md`.

## Stage D — Writing mode (objective decides)
```
CONNECT · TEACH · STORY · THOUGHT LEADERSHIP  →  BRAND WRITING
SELL · BOOK · OPT-IN · CONVERT                →  DIRECT RESPONSE
```
Direct-response methodology (`references/direct-response.md`) runs **only** on the
second path. Brand writing (`references/brand-writing.md`) never carries a forced CTA.
Worker tier: `frontier` for all final audience-facing copy (model-routing hard rule).

## Writing QA (mandatory, every draft)
Run `references/writing-qa.md`. Any failed item → revise, re-run. Two consecutive
fails on the same item → attach both versions and flag for Rachel in the card. The
permanent rule: **Would this person actually say this?**

## Output contract
Per platform brief: `draft.md` with front matter `{brand, objective, writing_mode,
platform, angle_id, sources[], writing_qa: PASS}` and the copy. Rachel's verbatim
phrases from intake are marked `[R]` inline so QA and Rachel can see them.

## Boundaries
- Never runs direct-response on a BRAND WRITING objective.
- Never introduces a claim absent from `proof.md`/`offers.md`/the brief.
- Never uses a phrase listed in `voice.md → disliked` or `prohibited-claims.md`.
