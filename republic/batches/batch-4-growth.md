# Batch 4 — Growth

Adds: `republic-claude-seo` and `republic-claude-ads` as bounded specialist workflows.

## Preconditions
- Batch 3 gate passed.
- Read access to Search Console, GBP, and the ad accounts already granted to the
  specialist tools; the skills request no new credentials.
- `config.yaml → paid_spend` confirmed by Rachel.

## Steps
1. `./scripts/install.sh --batch 4`
2. Run "Audit Physically Meta's local search presence." Confirm structured output and
   that recommended actions land as a job for Rachel or the existing GHL step, never
   as direct site/GBP edits.
3. Run one Claude Ads audit. Confirm every recommended change carries the spend-gate
   flag and nothing is applied.

## Gate
QA PASS; zero autonomous changes to sites, GBP, or ad accounts. Then: DONE. Freeze.
