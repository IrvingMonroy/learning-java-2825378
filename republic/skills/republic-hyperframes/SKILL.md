---
name: republic-hyperframes
description: Adds HyperFrames to the existing Republic production step for programmatic, branded video elements — animated educational slides, statistics, quote cards, diagrams, title sequences, review animations, CTA cards, explainers, overlays, promotional pieces — rendered from reusable per-brand templates in hyperframes/templates/. Republic supplies approved content; HyperFrames supplies repeatable production. Use when a brief or the editor requests a generated element, or for a fully generated promotional piece.
version: 1.0.0
batch: 1
adds_to: existing Republic production step
replaces: nothing
preserves: [existing brand profile as the token source, existing approval step]
tags: [republic, hyperframes, templates, motion, branded, batch-1]
---

# HyperFrames — repeatable branded elements

A separate job from editing real footage. (SPEC §3, §6)

## Templates
`hyperframes/templates/<brand>/<template>.md` defines slots, duration, and required
tokens. Physically Meta ships six: `educational-reel · review-highlight ·
pain-explainer · faq · promotion · myth-vs-fact`. A new client inherits the set by
copying the directory and pointing it at their brand profile.

## Procedure
1. Receive from the job: template, brand, slot content (approved copy only), target format.
2. Validate: required slots present, limits respected, every claim present in the
   brand's proof/offers. Reject naming the exact missing slot; never fill it.
3. Render with the brand's visual tokens read from the **existing brand profile**.
   Refuse if any token is empty. Attach output, render log, time to the job.
4. Hand back to `republic-openmontage` when the element is for a footage edit; otherwise
   the job proceeds to the existing QA/approval step.

## Changing a template
Only via the acceptance outcome or a v1.1 change, recorded in the template's `changelog`.

## Boundaries
- Never writes copy. Never renders without complete tokens.
- Never duplicates an element OpenMontage already produced on the same job; the
  acceptance test assigns overlapping capabilities to one tool.
- Never publishes or approves.
