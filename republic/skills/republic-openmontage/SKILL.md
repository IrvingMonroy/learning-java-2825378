---
name: republic-openmontage
description: Adds OpenMontage as a candidate automated editor for real footage inside the existing Republic production step — select moments from the Video Vision analysis against the job's brief, trim, assemble, burn captions, level audio, place branded elements from HyperFrames where the brief asks, format per platform, render. Holds a permanent position only if it beats the current raw-video → Instagram workflow on the editing acceptance test. Use when a job with source footage reaches production.
version: 1.0.0
batch: 1
adds_to: existing Republic production step
replaces: manual video editing — only after passing tests/acceptance/editing-acceptance.md against the current workflow
preserves: [current raw-video → Instagram workflow as baseline, existing approval step, GHL publishing]
tags: [republic, openmontage, editing, captions, render, batch-1]
---

# OpenMontage — automated editing of real footage

```
raw footage → select moments → trim → assemble → captions → audio
            → B-roll / branded elements where appropriate → format → render
```
(SPEC §3, §6). Candidate, not incumbent. The current workflow stays the baseline until
the acceptance sheet says otherwise.

## Inputs (from the existing job)
- `video-analysis.md` from `republic-video-vision`
- The job's brief as the existing workflow produces it: platform, duration, hook
  placement, caption behavior, required elements
- Approved copy from the existing drafting step (or `republic-writing` after Batch 2)
- Brand visual tokens from the existing brand profile

## Procedure
1. **Select moments** from `potential clips` and `good moments` that deliver the
   brief's hook and objective; exclude dead sections. Record chosen segments and why.
2. **Trim and assemble** to the brief's duration; hook-first unless the brief says
   demonstration-first.
3. **Captions** burned in from the cleaned transcript, Rachel's phrasing intact, style
   from brand tokens.
4. **Audio**: level speech; music only if the brief asks, under speech, licensed source
   recorded on the job.
5. **Elements**: title, stat, quote, or CTA cards come from `republic-hyperframes`.
   Do not build them here.
6. **Format** per platform; **render**; attach output, checksum, render log.
7. Record on the job: wall-clock time, Rachel interventions requested, failures. These
   are the acceptance evidence.

## Error handling
Render failure → attach log, retry once with identical inputs; second failure → note
`render: failed`, tell Socrates, leave the job in production. Missing HyperFrames
element → render without it and flag `element: missing`; never substitute an
unbranded one.

## Boundaries
- Never invents on-screen text beyond approved copy.
- Never publishes, uploads, or moves the job past the existing approval step.
- Never modifies the baseline workflow; it runs alongside it during acceptance.
