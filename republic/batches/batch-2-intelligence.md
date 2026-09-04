# Batch 2 — Intelligence

Adds: `republic-last-30-days` (current research, one pass per job) and
`republic-writing` (the single writing skill).

## Preconditions
- Batch 1 gate passed.
- Existing brand profile for Physically Meta mapped to `brands/brand-schema.md`;
  `voice` traced to real transcripts/posts; `prohibited-claims` present.
- The five source writing skills are **not** installed anywhere in the Hermes home
  (`validate.py` checks the package; the gap analysis checks the Droplet).

## Steps
1. `./scripts/install.sh --batch 2`
2. Run one real job end to end with the existing workflow plus the two skills. Research
   Brief attached once; drafts carry `writing_qa: PASS`.
3. Claude QA reviews the drafts against the voice profile and the objective/mode rule.

## Gate
QA PASS; no draft ran direct-response on a brand-writing objective; Rachel confirms
the drafts sound like her.
