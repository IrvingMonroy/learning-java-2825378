---
template: pain-explainer
brand: physically-meta
version: 1.0.0
formats: [9:16, 1:1, 16:9]
changelog:
  - 2026-09-03 initial
---

# pain-explainer

Diagram + text explaining a common discomfort and what massage does about it, 25–45s.

## Slots (approved copy only)
- pain_area
- diagram_ref (brand-approved anatomy asset)
- what_happens[2–3]
- what_we_do[2–3] (scope-of-practice checked)
- closing_line

## Brand tokens
Read from the existing Physically Meta brand profile (fields per `brands/brand-schema.md → brand`). Render refuses if any token is empty.

## Acceptance
Scored in `tests/acceptance/editing-acceptance.md`. Holds a permanent position only after passing.
