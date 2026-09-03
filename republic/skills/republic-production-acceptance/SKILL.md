---
name: republic-production-acceptance
description: Runs the editing acceptance test — the same content through OpenMontage and HyperFrames, scored on quality, Rachel intervention, time saved, caption quality, clip selection, brand consistency, rendering reliability, cost, and repeatability — and records which tool holds each permanent position or is removed. Use at the end of Block A and whenever a production tool change is proposed.
version: 1.0.0
department: 04_PRODUCTION
tags: [republic, acceptance, openmontage, hyperframes, evaluation]
---

# Editing acceptance test

Nothing is kept for being cool. The permanent production system must require **less
Rachel**, not merely produce more AI. (SPEC §10)

## Procedure
1. Pick three real Physically Meta source videos already in `CONTENT_DROP/` covering:
   a demonstration, a talking explanation, and a client-facing promotion.
2. For each, produce the same Platform Brief output twice: via `republic-editing`
   (OpenMontage) and, where the brief's element types allow, via `republic-hyperframes`.
3. Score each run on the nine criteria in `tests/acceptance/editing-acceptance.md`,
   1–5, with evidence lines (render logs, intervention count, wall-clock time, cost
   from run notes).
4. Hand the scored sheet to `republic-qa`. QA identifies what each tool does poorly and
   whether the other solves it.
5. Decision rules, applied by Rachel on the QA report:
   - A tool below 3 on *Rachel intervention required* or *Rendering reliability* does
     not hold a permanent position.
   - If both tools do the same job adequately, remove one from that job.
   - If neither passes for a job, that job is recorded as a manual bottleneck under
     `FREEZE.md` criterion 2, not papered over.
6. Record the outcome in `tests/acceptance/editing-acceptance.md → Decision` and in
   the vault as a canonical decision.

## Boundaries
- Does not tune tools mid-test. Same inputs, same settings, recorded.
- Does not recommend a third tool. Out of scope for v1.
