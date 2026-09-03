# Editing Acceptance Test — OpenMontage vs HyperFrames

SPEC §10. Same content, both tools, nine criteria, 1–5 each with evidence.
Run by `republic-production-acceptance`; reviewed by `republic-qa`; decided by Rachel.

## Test set (three real Physically Meta videos from CONTENT_DROP/)
| ID | File | Type | Platform Brief used |
|---|---|---|---|
| T1 | | demonstration | |
| T2 | | talking explanation | |
| T3 | | client-facing promotion | |

## Scores
Score each cell 1 (poor) – 5 (excellent). Evidence column cites render log, card note, or run-notes line.

| Criterion | OpenMontage T1/T2/T3 | HyperFrames T1/T2/T3 | Evidence |
|---|---|---|---|
| Quality | | | |
| Rachel intervention required (5 = none) | | | intervention count on card |
| Time saved (vs. Rachel editing by hand) | | | wall-clock on card |
| Caption quality | | | |
| Clip selection | | | n/a for HyperFrames unless brief includes clips |
| Brand consistency | | | tokens applied per brand.md |
| Rendering reliability (5 = 0 failures) | | | render logs |
| Cost | | | run notes |
| Repeatability (same inputs → same output) | | | second run diff |

## Decision rules
- Below 3 on *Rachel intervention* or *Rendering reliability* → no permanent position for that job.
- Both adequate on the same job → remove one from that job.
- Neither adequate → record a manual bottleneck (`FREEZE.md` criterion 2). Do not paper over.

## Decision
| Job | Permanent owner | Removed | Date | Canonical decision note |
|---|---|---|---|---|
| Real-footage editing (select, trim, assemble, captions, audio, render) | | | | |
| Generated branded elements (titles, stats, quotes, CTA cards, explainers) | | | | |
| Overlap: on-video text overlays | | | | |

Status: **NOT RUN** — requires the tools installed on the Droplet and three source videos.
