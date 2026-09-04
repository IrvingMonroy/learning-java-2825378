# Republic v1 — Definition of DONE

Done is not "every capability exists." Done is the four batches passed and the test
below holds on the existing Republic.

## The test
Rachel, through Socrates:
> "Here are the videos I recorded this week. Handle social for Physically Meta."

The existing workflow, with the added capabilities, runs:
`ingest → understand (Video Vision) → research (Last 30 Days) → decide → write
(Republic Writing) → edit (chosen stack) → adapt → QA → present for approval →
schedule → publish (existing GHL step) → capture results → preserve learning (Librarian)`

Rachel's only touches: the existing approval step, and approval of any paid change at
or above the `config.yaml` gate. Any other touch is a bottleneck candidate.

## Exit criteria
- [ ] Gap analysis run against the real Republic; result table filled (`GAP_ANALYSIS.md`).
- [ ] Batch 1 acceptance completed; editing stack chosen vs. baseline and recorded (`tests/acceptance/editing-acceptance.md`).
- [ ] Batches 2, 3, 4 each have a QA PASS report in `qa/reports/`.
- [ ] End-to-end run sheet PASS (`tests/acceptance/end-to-end-run.md`).
- [ ] No open BLOCKER or DEFECT.
- [ ] `scripts/validate.py` passes.
- [ ] Preserved pieces unchanged, confirmed by diff against their pre-upgrade copies.

All boxes checked: **stop building The Republic. Run it.**
