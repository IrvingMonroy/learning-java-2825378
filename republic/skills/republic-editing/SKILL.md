---
name: republic-editing
description: 04_PRODUCTION editing engine using OpenMontage on real footage — select moments from the Video Vision analysis against the Platform Brief, trim, assemble, caption, mix audio, add B-roll or HyperFrames elements where the brief calls for them, format per platform, and render. Use when a content card with source media enters PRODUCTION. First component built in Block A; subject to the editing acceptance test.
version: 1.0.0
department: 04_PRODUCTION
tags: [republic, editing, openmontage, captions, render]
---

# Editing engine — OpenMontage on real footage

```
raw footage → select moments → trim → assemble → captions → audio
            → B-roll / assets where appropriate → format → render
```
(SPEC §8). OpenMontage holds this position only while it passes
`republic-production-acceptance`.

## Inputs (all from the card)
- `video-analysis.md` (Video Vision): potential clips, dead sections, on-screen text
- Platform Brief: format, duration, hook placement, caption behavior, asset requirements
- Approved copy from `republic-writing-system`: on-screen hook text, caption
- `brands/<brand>/brand.md`: colors, fonts, caption style, logo usage

## Procedure
1. **Select moments.** From `potential clips` and `good moments`, choose segments that
   deliver the brief's hook and objective. Exclude `awkward/dead sections`. Record
   chosen segments with reasons on the card.
2. **Trim and assemble** to the brief's duration. Hook segment first if the brief says
   hook-first; demonstration-first where the learning loop says so for this brand.
3. **Captions.** Burn in per platform norms. Source text is the cleaned transcript;
   Rachel's phrasing preserved. Style from `brand.md`.
4. **Audio.** Level speech; music only if the brief asks, under the speech, from a
   licensed source recorded on the card.
5. **Assets.** Where the brief specifies a title card, stat, quote, or CTA card,
   request it from `republic-hyperframes` and place it. Do not build such elements here.
6. **Format** per platform (aspect, safe zones, duration caps). **Render** and attach
   with a checksum and render log.
7. Record on the card: time to render, Rachel interventions requested (should be 0),
   any failures. These feed the acceptance test.

## Error handling
- Render failure → attach the log, retry once with the same inputs. Second failure →
  card note `render: failed`, Socrates informed, card stays in PRODUCTION.
- Missing asset from HyperFrames → render without it and flag `asset: missing` so QA
  sees it. Never substitute an unbranded element.

## Boundaries
- Never invents on-screen text beyond approved copy.
- Never selects clips that contradict the brief's objective to chase a "better" moment.
- Never publishes or uploads. Output stays on the card for QA and approval.
