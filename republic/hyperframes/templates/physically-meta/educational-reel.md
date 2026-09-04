---
template: educational-reel
brand: physically-meta
version: 1.0.0
formats: [9:16, 1:1, 16:9]
changelog:
  - 2026-09-03 initial
---

# educational-reel

Animated educational slides teaching one thing, 20–40s.

## Slots (approved copy only)
- title (≤ 40 chars)
- points[3] (≤ 60 chars each)
- demonstration_clip? (optional, from editing)
- closing_line (BRAND WRITING, no CTA unless objective is conversion)

## Brand tokens
Read from the existing Physically Meta brand profile (fields per `brands/brand-schema.md → brand`). Render refuses if any token is empty.

## Acceptance
Scored in `tests/acceptance/editing-acceptance.md`. Holds a permanent position only after passing.
