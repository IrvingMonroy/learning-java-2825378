---
name: republic-writing
description: The single Republic writing skill, composed from the best parts of Ghostwriter Killer (voice DNA), Blank Page Killer (ideation and starting material), 72 Reasons to Buy (credible angles and motivations), Direct Response Copywriter (conversion writing), and AI Slop Killer (final voice QA). Picks the right behavior from the job's objective — brand writing for CONNECT/TEACH/STORY/THOUGHT LEADERSHIP, direct response only for SELL/BOOK/OPT-IN/CONVERT — and ends every draft with "would this person actually say this?". Use for any drafting, caption, hook, or copy task in the existing Republic workflow.
version: 1.0.0
batch: 2
adds_to: existing Republic drafting step
replaces: nothing — the five source skills are not installed separately
preserves: [existing brand profiles in the vault, existing approval step]
tags: [republic, writing, voice, copy, direct-response, batch-2]
---

# Republic Writing — one skill that knows which behavior the job needs

```
REPUBLIC-WRITING
├── voice DNA            (from Ghostwriter Killer)
├── ideation / starting  (from Blank Page Killer)
├── angles / motivations (from 72 Reasons to Buy)
├── conversion writing   (from Direct Response Copywriter)
└── final voice QA       (from AI Slop Killer)
```
(SPEC §4)

## Preconditions
The brand's existing profile provides the fields in `brands/brand-schema.md`. If
`voice` is not traced to real human material, or `prohibited-claims` is absent, stop
and report the missing field to Socrates. Never draft on an invented voice.

## Behavior selection (objective first, always)
| Job objective | Behaviors that run |
|---|---|
| CONNECT · TEACH · STORY · THOUGHT LEADERSHIP | voice DNA → ideation (if no draft) → angles (evidence only) → **brand writing** → voice QA |
| SELL · BOOK · OPT-IN · CONVERT | voice DNA → ideation (if no draft) → angles (ranked) → **conversion writing** → voice QA |
Conversion methodology never runs on the first row. That protects the personal brand
from endless "Pain! Hook! Agitate! Comment YES!".

## The behaviors
- **Voice DNA** (`references/voice-dna.md`): read the profile's voice fields; extract
  phrases, vocabulary, cadence, humor, polish. Read only, never author.
- **Ideation** (`references/ideation.md`): only when no draft exists. Concepts, hooks,
  outlines, story directions, one rough draft. Labeled `starting-material`. No CTAs.
- **Angles** (`references/angles.md`): *what credible reasons would different segments
  care?* Every angle sourced to reviews, DMs, comments, search, sales language, or an
  actual offer characteristic. Cluster into 3–7 motivations. Unsourced angles dropped.
- **Brand writing** (`references/brand-writing.md`): the real moment first, teach one
  thing, Rachel's phrasing marked `[R]`, no forced CTA.
- **Conversion writing** (`references/conversion.md`): one offer, one action, proof and
  objections only from the profile, every claim checked against prohibited claims.
- **Voice QA** (`references/voice-qa.md`): eleven checks; any FAIL → revise and re-run;
  two consecutive FAILs on one item → attach both versions and flag for Rachel.

## Output
`draft.md` on the job with `{brand, objective, mode, platform, angle_id, sources[],
voice_qa: PASS}`. Worker tier `frontier` for all final audience-facing copy; `local`
acceptable for ideation volume Rachel will not see.

## Boundaries
- Never introduces a claim absent from the profile's proof/offers or the research brief.
- Never uses a disliked or prohibited phrase.
- Never publishes or approves; the existing approval step is unchanged.
