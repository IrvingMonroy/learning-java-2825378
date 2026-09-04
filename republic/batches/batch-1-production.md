# Batch 1 — Production (editing is the demonstrated weak behavior)

```
EXISTING REPUBLIC
       ├── ADD republic-video-vision
       ├── ADD republic-openmontage
       └── ADD republic-hyperframes
                 ↓
       test against current editing (baseline)
                 ↓
       Claude QA
                 ↓
       KEEP what works · REMOVE what doesn't
```

## Preconditions
- Gap analysis rows for the three tools filled (`GAP_ANALYSIS.md`).
- Video Vision reachable from the Droplet (Mac Mini over Tailscale) — `scripts/smoke-test.sh`.
- Three real Physically Meta source videos available: a demonstration, a talking
  explanation, a client-facing promotion.
- Brand visual tokens present in the existing Physically Meta profile (HyperFrames
  refuses to render without them).

## Steps
1. `./scripts/install.sh --batch 1`
2. Run the baseline: today's raw-video → Instagram workflow on the three videos.
   Record time, interventions, output.
3. Run OpenMontage on the same three, against the same brief.
4. Run HyperFrames for each brief element it can produce (title, quote, stat, CTA card,
   explainer). Do not force it onto footage editing.
5. Fill `tests/acceptance/editing-acceptance.md`. Hand to Claude QA.
6. Rachel decides per job using the sheet's rules. Record the decision as canonical
   in the vault.

## Gate
Claude QA PASS on the acceptance report **and** a recorded decision for each job:
keep, remove, or baseline stays. Only then does Batch 2 begin.
