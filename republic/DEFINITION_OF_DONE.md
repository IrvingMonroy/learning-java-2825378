# Republic v1 — Definition of DONE

Republic v1 is not done because every conceivable capability exists. It is done when
the end-to-end test below passes and Claude QA reports no open BLOCKER or DEFECT.

## The test

Rachel says, through Socrates:

> "Here are the videos I recorded this week. Handle social for Physically Meta."

The system must then complete every stage below, and Rachel's only required touches
are the two marked **RACHEL**.

| # | Stage | Department / component | Evidence of completion |
|---|---|---|---|
| 1 | ingest | Triage; `CONTENT_DROP/` | One Kanban card per intake item in TRIAGE |
| 2 | understand | Video Vision | Structured analysis attached to each card |
| 3 | research | 01_RESEARCH (Last 30 Days + SEO signals + customer language) | One Research Brief per job, not per platform |
| 4 | decide | Republic strategy | Objective set (BRAND WRITING or DIRECT RESPONSE); platform set chosen |
| 5 | write | Writing System stages A–D + Writing QA | Drafts pass the Writing QA checklist |
| 6 | edit | OpenMontage and/or HyperFrames (whichever passed acceptance) | Rendered assets in the card |
| 7 | adapt | Platform experts + Repurposing | Native version per target platform |
| 8 | QA | Claude QA contract | PASS, or findings with classification |
| 9 | present for approval | Kanban RACHEL APPROVAL | **RACHEL** approves or returns with a note |
| 10 | schedule | 05_DISTRIBUTION_CRM → GHL | Scheduled in GHL Social Planner with IDs recorded on the card |
| 11 | publish | GHL | Card moves to PUBLISHED on GHL confirmation |
| 12 | capture results | GHL data, native analytics | Metrics recorded on the card at MEASURED |
| 13 | preserve learning | Librarian → Obsidian → QMD reindex | Evidence note filed; canonical update only if `learning.min_sample` reached |

## What "without Rachel coordinating" means

Rachel does **not**:

- open more than one interface (Socrates chat plus the Kanban board),
- copy prompts or outputs between tools,
- read terminals or agent chat logs to learn status,
- hand-edit every video,
- remember what happened to a prior job.

**RACHEL** touches in v1: approval at the gate, and approval of meaningful paid
spend/change (SPEC §16). Any other required touch is logged as a bottleneck candidate
under `FREEZE.md` criterion 2.

## Exit criteria

- [ ] End-to-end test run recorded in `qa/reports/` with a PASS.
- [ ] Editing acceptance test completed; permanent editing stack chosen and recorded (`tests/acceptance/editing-acceptance.md`).
- [ ] `scripts/validate.py` passes.
- [ ] No open BLOCKER or DEFECT in the latest QA report.
- [ ] `SPEC.md` marked FROZEN with version 1.0.0.

When all boxes are checked: **stop building The Republic. Run it.**
