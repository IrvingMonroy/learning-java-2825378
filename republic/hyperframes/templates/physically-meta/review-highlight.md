---
template: review-highlight
brand: physically-meta
version: 1.0.0
formats: [9:16, 1:1, 16:9]
changelog:
  - 2026-09-03 initial
---

# review-highlight

Review animation: quote card with rating, 8–15s.

## Slots (approved copy only)
- quote (verbatim from proof.md, ≤ 140 chars)
- reviewer_first_name_or_initial
- rating (1–5)
- source_platform
- consent_ref (proof.md row)

## Brand tokens
Read from the existing Physically Meta brand profile (fields per `brands/brand-schema.md → brand`). Render refuses if any token is empty.

## Acceptance
Scored in `tests/acceptance/editing-acceptance.md`. Holds a permanent position only after passing.
