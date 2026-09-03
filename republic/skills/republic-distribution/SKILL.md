---
name: republic-distribution
description: 05_DISTRIBUTION_CRM — The Republic's interface to GHL. Schedules and publishes approved assets through GHL Social Planner, designs and maintains GHL comment-to-DM workflows, runs the reputation flow (review → sentiment → reply draft or owner alert → customer-language extraction), and records CRM/lead/booking outcomes on the card. Use when a card enters SCHEDULED, when a comment-to-DM campaign is requested, or when a new review arrives. Never recreates GHL inside Hermes.
version: 1.0.0
department: 05_DISTRIBUTION_CRM
tags: [republic, ghl, publishing, crm, comment-to-dm, reputation]
---

# 05_DISTRIBUTION_CRM — Republic owns what and why; GHL owns execution

(SPEC §2, §12, §13, §14)

## A. Publishing (card in SCHEDULED)
1. Precondition: card left `RACHEL_APPROVAL` with `approved` set by Rachel. If not,
   refuse and log a boundary event. No exceptions, no "she said it in chat".
2. For each platform version, create the GHL Social Planner post: media, caption,
   metadata, first comment, schedule time from the Platform Brief. Record planner IDs
   on the card.
3. On GHL publish confirmation, move the card to PUBLISHED with live URLs. On failure,
   attach the GHL error, retry once, then flag `publish: failed` to Socrates.
4. Where GHL does not support a platform, record `manual-publish-required` on the card
   as a bottleneck candidate. Do not build a workaround.

## B. Comment-to-DM (`references/comment-to-dm.md`)
```
POST → "Comment GUIDE" → GHL trigger → public reply → DM → resource
     → CRM contact/tag → nurture → booking/conversion
```
Republic designs the workflow (keyword, public reply, DM copy, resource, tags, nurture
sequence, booking link) as an `ops` card; it passes QA and RACHEL_APPROVAL; then this
skill builds it in GHL (via API/MCP where available, else the `ghl-crm-builder`
procedure). Keywords are registered per brand to avoid collisions.

## C. Reputation (`references/reputation.md`)
```
NEW REVIEW → sentiment → good | neutral → reply draft (Writing System, brand voice)
                       → sensitive → owner alert to Rachel via Socrates, no draft posted
           → customer-language extraction → Librarian (voice-of-customer evidence)
```
Reply drafts are posted to GHL only after Rachel's approval per brand policy in
`brands/<brand>/brand.md → review_reply_policy` (default: approve each). Recurring
negative themes (3+ in 90 days) become an `ops` card: operational intelligence.

## D. CRM outcomes
At MEASURED, pull from GHL: leads, tagged contacts, DMs sent, bookings attributed to
the card's posts. Record on the card for the learning loop.

## Boundaries
- Never publishes anything that did not pass through RACHEL_APPROVAL.
- Never modifies GHL pipelines, workflows, or contacts outside an approved `ops` card.
- Never posts a review reply on a `sensitive` classification.
- GHL unreachable → say so; do not queue publishes silently past their schedule time.
