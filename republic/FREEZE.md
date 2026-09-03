# Freeze Boundary and v1.1 Change Policy

Republic v1 is frozen once it passes QA (`qa/QA_CONTRACT.md`) and the Definition of
Done (`DEFINITION_OF_DONE.md`). At that point Republic moves from **build mode** to
**operations mode**.

## Explicitly excluded from v1

| Excluded | Reason recorded |
|---|---|
| DeepSeek Harness | Out of scope; no demonstrated need |
| Herdr | Out of scope |
| Omarchy | Out of scope |
| Fincept | Out of scope |
| Vibe Trading | Out of scope |
| Anti-detection browser infrastructure | Only if a legitimate workflow later requires specialized browser automation |
| Additional writing "killer" skills (Blank Page Killer, Ghostwriter Killer, 72 Reasons to Buy, Copywriter Killer, Slop Killer, Hook Agent, Caption Agent, CTA Agent, or any successor) | Absorbed into the single Republic Writing System; installing them separately is skill soup |
| New orchestration framework | Hermes is the orchestrator |
| Soup (skill router) | Deferred; evaluated only if Hermes skill selection proves unreliable |
| PostHog | Deferred; added only for an identified measurement gap |

## What qualifies as a v1.1 change

A change is admitted only if it is one of:

1. **A demonstrated defect** — a QA finding classified BLOCKER or DEFECT, with a reproduction.
2. **A recurring manual bottleneck** — the same Rachel intervention observed on three or more jobs.
3. **Meaningful cost reduction** — measured, not estimated, against the run notes.
4. **A deliberately chosen new service capability** — a decision Rachel records as canonical in the vault.

Everything else is filed by the Librarian as *interesting, not actionable*.
A cool GitHub repo appearing on Instagram is not a change request.

## How a v1.1 change is processed

```
proposal → classify against the four criteria → Rachel decision (canonical in vault)
        → implement → Claude QA (PASS / FAIL) → merge → SPEC.md version bump
```

Model replacement is **not** a version change. Workers swap under the existing
`model-routing` policy without touching this specification (SPEC §23).
