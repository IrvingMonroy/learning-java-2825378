---
name: republic-qa
description: Runs the Claude QA contract against a Republic build, skill, or card in the QA column — evaluates the ten questions, classifies each finding BLOCKER/DEFECT/IMPROVEMENT/PREFERENCE with a SPEC citation and reproduction, checks boundaries and operability, and returns PASS or FAIL. Use when a card enters QA or when a Republic change is proposed. Never redesigns.
version: 1.0.0
department: control
tags: [republic, qa, review, contract]
---

# Republic QA — find defects, do not redesign

Full contract: `qa/QA_CONTRACT.md`. This skill is that contract made runnable. The
architecture is already approved. (SPEC §22)

## Scope of a review
- **Card review** (card in QA): outputs attached to the card — brief, drafts,
  assets, platform versions.
- **Build review** (skill or block change): the diff plus `scripts/validate.py` result.
- **End-to-end review**: a Definition of Done run (`tests/acceptance/end-to-end-run.md`).

## Procedure
1. Load `SPEC.md`, the card or diff, and the relevant brand directory.
2. Run `scripts/validate.py` for build reviews. A failing validator is an automatic
   BLOCKER with the validator output as the reproduction.
3. Walk the ten questions. For each finding write: class · SPEC § · one-line summary ·
   reproduction (input → observed → expected) · smallest fix. No SPEC citation means
   the finding cannot be a DEFECT.
4. For card reviews, additionally run the Writing QA checklist
   (`republic-writing-system/references/writing-qa.md`) on every draft and the brand
   consistency check on every asset.
5. Complete the boundary table and operability table from `qa/QA_REPORT_TEMPLATE.md`.
6. Verdict: `PASS` if no open BLOCKER/DEFECT, else `FAIL` listing them. Write the
   report to `qa/reports/`. Return the card to the owning column on FAIL with the
   finding IDs in the card note; advance to RACHEL_APPROVAL on PASS.

## Hard limits
- May not move a card into or out of RACHEL_APPROVAL. Moves to it via `republic-kanban`
  only on PASS.
- May not approve spend, publish, or push to GHL.
- May not propose a component replacement, new framework, or department restructure.
  If tempted, record one PREFERENCE line and move on.
- Re-review after a fix covers that finding and its regression surface only.
