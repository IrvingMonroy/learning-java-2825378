# Freeze Boundary and v1.1 Change Policy

Republic v1 is frozen once all four batches pass Claude QA and the Definition of Done
holds. Then Republic moves from **build mode** to **operations mode**.

## Preserved pieces (frozen from the start)
SOUL/identity · profiles (Instagram included) · Librarian (patched, never replaced) ·
Obsidian + QMD · Kanban job creation · GHL publishing and its approval step · Socrates ·
the raw-video → Instagram workflow (as baseline until a tool beats it on acceptance).

## Explicitly excluded
| Excluded | Reason recorded |
|---|---|
| Soup (skill router) | Only if Hermes skill selection proves unreliable |
| PostHog | Only for an identified measurement gap; GHL, native analytics, Search Console, ad data first |
| Herdr, DeepSeek Harness, Archify, Omarchy, Fincept, Vibe Trading | No actual need |
| Anti-detection browser infrastructure | Only if a legitimate workflow later requires specialized browser automation |
| Blank Page Killer, Ghostwriter Killer, 72 Reasons to Buy, Copywriter Killer, Slop Killer, Hook/Caption/CTA agents as separate installs | Absorbed into the single `republic-writing` skill |
| Any new orchestration framework | Hermes is the orchestrator |

## What qualifies as a v1.1 change
1. **A demonstrated defect** — QA BLOCKER or DEFECT with a reproduction.
2. **A recurring manual bottleneck** — the same Rachel intervention on three or more jobs.
3. **Meaningful cost reduction** — measured against run notes, not estimated.
4. **A deliberately chosen new service capability** — recorded as a canonical decision in the vault.

Everything else the Librarian files as *interesting, not actionable*. A cool GitHub
repo appearing on Instagram is not a change request.

## Processing a v1.1 change
```
proposal → classify against the four criteria → Rachel decision (canonical in vault)
        → implement additively → Claude QA PASS → install → SPEC.md version bump
```
Model replacement is not a version change; workers swap under `model-routing`.
