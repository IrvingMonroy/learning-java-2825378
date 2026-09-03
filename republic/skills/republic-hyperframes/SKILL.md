---
name: republic-hyperframes
description: 04_PRODUCTION programmatic branded video elements via HyperFrames — animated educational slides, statistics, quote cards, diagrams, title sequences, review animations, CTA cards, explainers, branded overlays, promotional videos — rendered from reusable per-brand templates in hyperframes/templates/. Republic supplies content; HyperFrames supplies repeatable production. Use when a Platform Brief or editing job requests a generated element, or for fully generated promotional pieces.
version: 1.0.0
department: 04_PRODUCTION
tags: [republic, hyperframes, templates, motion, branded]
---

# HyperFrames — repeatable branded production

Separate job from editing real footage. (SPEC §9)

## Templates
`hyperframes/templates/<brand>/<template>.md` defines each template's content slots,
duration, and brand tokens. Physically Meta ships six:
`educational-reel · review-highlight · pain-explainer · faq · promotion · myth-vs-fact`.
A new client inherits the template set by copying the brand directory and swapping
tokens.

## Procedure
1. Receive a request from the card: template name, brand, slot content (approved copy
   only), target platform format.
2. Validate slot content against the template (required slots present, character
   limits respected, claims present in `proof.md`/`offers.md`). Reject with the exact
   missing slot rather than filling it.
3. Render with HyperFrames using brand tokens from `brands/<brand>/brand.md`. Attach
   output, render log, and time to the card.
4. If the element is for `republic-editing`, hand it back on the card; if standalone,
   move the card to QA.

## Building or changing a template
Only through a v1.1 change or the acceptance test outcome. A template change is a
card of type `ops`, passes QA, and is recorded in the template file's `changelog`.

## Boundaries
- Never writes copy. Slots take approved text only.
- Never renders a template for a brand without a complete `brand.md` token set.
- Never produces elements that duplicate what OpenMontage already produced on the same
  card; the acceptance test decides who owns overlapping capabilities.
