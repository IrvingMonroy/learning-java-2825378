---
name: republic-paid
description: 06_PAID. Delegates bounded paid-acquisition requests (audits, Meta/Google/TikTok/YouTube strategy, wasted-spend identification, creative analysis, optimization plans) to the Claude Ads specialist, routes findings through QA where appropriate, and enforces that any meaningful spend or budget change requires Rachel's approval via the Kanban gate. Use for any advertising question or request. Never autonomously alters ad budgets.
version: 1.0.0
department: 06_PAID
tags: [republic, paid, ads, claude-ads, meta, google, budget]
---

# 06_PAID — Claude Ads as a bounded specialist

```
Republic → Paid Acquisition request → Claude Ads → audit / strategy / findings
        → Republic → Claude QA where appropriate → Rachel approval for meaningful spend/change
```
(SPEC §2, §16). A specialist service, not nineteen agents.

## Accepted request shapes
`audit-account` · `wasted-spend` · `creative-analysis` · `campaign-strategy` ·
`optimization-plan` — each with platform(s), brand, account, window.

## Procedure
1. Normalize the card's request to one shape. Confirm read access to the ad account is
   already granted; this skill never requests new credentials.
2. Invoke Claude Ads with the request. Worker tier: `frontier`. Require structured
   output: findings · recommended changes (each with current value, proposed value,
   expected effect, confidence) · data source · window.
3. **Spend gate.** For every recommended change compute absolute and relative budget
   delta. If either meets `kanban/pipeline.yaml → gates.paid_spend`, mark the change
   `requires: rachel` and the card cannot leave QA except to RACHEL_APPROVAL.
   `autonomous_allowed: false` means no change is applied by this skill at all in v1;
   approved changes are applied by Rachel or by an approved `ops` card with a named
   executor.
4. Route to `republic-qa` for audits that recommend changes; skip QA for read-only
   audits with no recommendations (record `qa: not-required`).
5. Attach and move per `paths.paid`.

## Boundaries
- Never edits campaigns, budgets, bids, audiences, or creatives.
- Never uses metered workers for a request Rachel has not opened a card for.
- Findings that imply platform policy risk (health claims, before/after imagery) are
  flagged against `prohibited-claims.md` before Rachel sees them.
