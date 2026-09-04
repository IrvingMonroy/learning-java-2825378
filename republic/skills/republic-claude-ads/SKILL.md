---
name: republic-claude-ads
description: Gives the existing Republic a bounded workflow for the Claude Ads specialist — account audits, Meta/Google/TikTok/YouTube strategy, wasted-spend identification, creative analysis, optimization plans — with a hard spend gate so any meaningful budget or campaign change requires Rachel's approval. Use for any advertising question or request. Never autonomously alters ad budgets.
version: 1.0.0
batch: 4
adds_to: Republic (specialist access)
replaces: nothing
preserves: [ad accounts — read only; existing approval step]
tags: [republic, paid, ads, claude-ads, budget, batch-4]
---

# Claude Ads — bounded specialist with a spend gate

```
Republic → request → Claude Ads → audit / strategy / findings → Republic
        → Claude QA where appropriate → Rachel approval for meaningful spend/change
```
(SPEC §3, §8)

## Request shapes
`audit-account` · `wasted-spend` · `creative-analysis` · `campaign-strategy` ·
`optimization-plan`, each with platform(s), brand, account, window.

## Procedure
1. Normalize the request. Confirm read access already exists; request no credentials.
2. Invoke Claude Ads. Worker tier `frontier`. Require: findings · recommended changes
   (current value, proposed value, expected effect, confidence) · data source · window.
3. **Spend gate.** For each recommended change compute absolute and relative delta
   against `config.yaml → paid_spend`. At or above either threshold → mark
   `requires: rachel`. `autonomous_allowed: false` means this skill applies nothing in v1.
4. Audits with recommendations go to Claude QA; read-only audits record `qa: not-required`.
5. Flag any finding implying platform-policy risk (health claims, before/after imagery)
   against the brand's prohibited claims before Rachel sees it.

## Boundaries
- Never edits campaigns, budgets, bids, audiences, or creatives.
- Never runs on a request Rachel has not opened a job for.
