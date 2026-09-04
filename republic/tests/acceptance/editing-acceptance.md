# Editing Acceptance Test — baseline vs OpenMontage vs HyperFrames

SPEC §6. Same source videos, three runs. **Baseline = the current raw-video →
Instagram workflow.** A new tool holds a permanent position only if it requires less
Rachel than the baseline on that job. Nothing is kept for being interesting.

## Test set (three real Physically Meta videos)
| ID | File | Type | Brief used |
|---|---|---|---|
| T1 | | demonstration | |
| T2 | | talking explanation | |
| T3 | | client-facing promotion | |

## Scores — 1 (poor) to 5 (excellent), evidence cited per cell
| Criterion | Baseline T1/T2/T3 | OpenMontage T1/T2/T3 | HyperFrames T1/T2/T3 | Evidence |
|---|---|---|---|---|
| Quality | | | | |
| Rachel intervention required (5 = none) | | | | intervention count |
| Time saved vs. baseline | n/a | | | wall-clock |
| Caption quality | | | | |
| Clip selection | | | n/a unless brief includes clips | |
| Brand consistency | | | | tokens applied |
| Rendering reliability (5 = 0 failures) | | | | render logs |
| Cost | | | | run notes |
| Repeatability (same inputs → same output) | | | | second-run diff |

## Decision rules
- Below 3 on *Rachel intervention* or *Rendering reliability* → no permanent position.
- New tool not better than baseline on *Rachel intervention* for a job → baseline stays for that job.
- OpenMontage weak on something HyperFrames solves → keep HyperFrames for that thing.
- Both adequate on the same job → remove one from that job.
- Neither beats baseline → record the job as a manual bottleneck (`FREEZE.md` criterion 2).

## Decision (Rachel, on the QA report)
| Job | Owner after test (baseline / OpenMontage / HyperFrames) | Removed | Date | Canonical decision note |
|---|---|---|---|---|
| Real-footage editing (select, trim, assemble, captions, audio, render) | | | | |
| Generated branded elements (titles, stats, quotes, CTA cards, explainers) | | | | |
| Overlap: on-video text overlays | | | | |

Status: **NOT RUN** — needs the tools on the Droplet/Mac Mini and three source videos.
