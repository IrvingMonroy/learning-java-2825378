---
template: promotion
brand: physically-meta
version: 1.0.0
formats: [9:16, 1:1, 16:9]
changelog:
  - 2026-09-03 initial
---

# promotion

Offer announcement, 10–20s, CTA card.

## Slots (approved copy only)
- offer_name (offers.md)
- what_you_get[≤3]
- price_or_terms
- cta_text + cta_link
- dates

## Brand tokens
Read from `brands/physically-meta/brand.md → Visual tokens`. Render refuses if any token is empty.

## Acceptance
Scored in `tests/acceptance/editing-acceptance.md`. Holds a permanent position only after passing.
