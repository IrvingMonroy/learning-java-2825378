# QA Report — Republic v1 specification and package (initial build)

- **Date:** 2026-09-03
- **Reviewer:** Claude (independent QA)
- **Scope:** `SPEC.md` as transcribed from Rachel's approved architecture; the v1 package
  (skills, kanban, brands, templates, tests, scripts). Static review plus
  `scripts/validate.py`. **Not in scope:** runtime behavior on the Droplet — no external
  tool was executed here, so "does it work" is verified only for package consistency.
- **Spec version:** 1.0.0
- **Verdict:** **FAIL** — two BLOCKERs open, both need Rachel's input, neither is a redesign.

## Findings

| ID | Class | SPEC § | Summary | Reproduction | Smallest fix |
|---|---|---|---|---|---|
| F1 | BLOCKER | §12, §21 vs. existing `model-routing` hard rule 1 | Two authoritative documents disagree on who may push to GHL. SPEC routes approved cards `Republic → GHL` from the Droplet after the RACHEL_APPROVAL gate. The existing model-routing skill says "GHL pushes — Claude session only, via social-media-manager." A Republic publish would violate one or the other. | Card reaches SCHEDULED → `republic-distribution` pushes to GHL → model-routing rule 1 says this must not happen outside a Claude session. Expected: one rule. | Rachel picks one line. Package assumes SPEC wins: amend model-routing hard rule 1 to "The approval gate is the RACHEL_APPROVAL Kanban column; GHL pushes happen only from an approved card via `republic-distribution`." Alternative: keep rule 1 and have Republic hand approved cards to a Claude session. |
| F2 | BLOCKER | §4 Stage A, Definition of Done | Physically Meta `voice.md` has no human source material. Writing System refuses to draft while `TODO-SOURCE` is present (by design), so stage 5 of the Definition of Done cannot run. | `brands/physically-meta/voice.md` contains `TODO-SOURCE`, `sources: []`. Expected: phrases, vocabulary, cadence traced to transcripts/emails/posts. | Rachel supplies 3+ transcripts or approved posts; Librarian extracts into `voice.md`; remove marker. No code change. |
| F3 | DEFECT | §16 | "Meaningful spend/change" is undefined in the spec. Package sets defaults ($50 absolute or 20% relative) in `kanban/pipeline.yaml → gates.paid_spend`. | Claude Ads recommends +$40/day → is that "meaningful"? Spec cannot answer. | Rachel confirms or edits the two numbers. |
| F4 | DEFECT | §26 | "Sufficient evidence" is undefined. Package sets `learning.min_sample: 12`, `measurement_window_days: 7`, and requires Rachel acknowledgement before `canonical: true`. | 6 Reels show a pattern → canonical or not? Spec cannot answer. | Rachel confirms or edits the numbers. |
| F5 | DEFECT | §14 | Spec does not say whether good/neutral review replies post automatically or after approval. Package defaults to `review_reply_policy: approve-each` per brand. | New 5-star review → reply draft → posted? Spec silent. | Rachel confirms the default or sets `auto-good-only` per brand in `brand.md`. |
| F6 | IMPROVEMENT | §21 | Column list is written for content jobs; search, paid, knowledge, and ops requests have no defined path. Package adds `paths.<type>` in `pipeline.yaml`, each still passing RACHEL_APPROVAL where an action results. | A "audit our local SEO" request has no column path in §21 alone. | Already implemented; record as accepted or adjust the paths. |
| F7 | IMPROVEMENT | §13 | §2 says "do not recreate GHL inside Hermes"; §13 says Republic "builds/manages the GHL workflow." The build mechanism is unspecified. Package: designed as an `ops` card, built via GHL API/MCP from Hermes where available, else via the existing `ghl-crm-builder` procedure in a Claude session. | Comment-to-DM approved → who clicks in GHL? | Confirm the mechanism once the GHL API/MCP access from the Droplet is known. |
| F8 | IMPROVEMENT | §10 | Acceptance criteria are named but not scaled or thresholded. Package uses 1–5 with "below 3 on intervention or reliability = no permanent position." | Tool scores 3/5 on quality — keep? | Confirm the threshold or change it in `tests/acceptance/editing-acceptance.md`. |
| F9 | PREFERENCE | §20 | Understand Anything has no runtime role, so the package ships no skill for it; it is documented in SPEC only. | — | None required. |

## Boundary check

| Boundary | Verified | Note |
|---|---|---|
| Socrates never publishes, schedules, approves | ☑ | No skill grants Socrates a gate or GHL action; triage only |
| No department bypasses RACHEL_APPROVAL | ☑ | `validate.py` rejects any content/search/paid/ops path without it |
| Paid spend above gate is never autonomous | ☑ | `autonomous_allowed: false`; `republic-paid` applies no change in v1 |
| Librarian preserves originals; supersedes are linked | ☑ | `republic-librarian` never deletes; SUPERSEDES links both ways |
| Claude never approves or publishes | ☑ | `republic-qa` hard limits; F1 must close for GHL boundary to be single-sourced |
| Skills reference worker tiers, not model IDs | ☑ | `validate.py` regex; PASS |

## Operability check

| Question | Yes/No |
|---|---|
| Can Rachel get status from Kanban alone? | Yes by design (`republic-kanban`); unverified at runtime |
| Does any step require reading a terminal or agent chat? | No by design; smoke test is operator-only |
| Does any step require copying a prompt between tools? | No by design; F7 mechanism may require GHL clicks until confirmed |
| Does any step require knowing which model ran? | No; `worker_log` records tiers |

## What was verified
- `scripts/validate.py` PASS: 18 skills, front matter complete, departments covered, 11 columns match §21, gates correct, brand schema complete, six Physically Meta templates present, FREEZE exclusions absent, no model IDs.
- Every skill cites the SPEC sections it implements and has a Boundaries section.

## What was not verified
- Any external tool (Video Vision, OpenMontage, HyperFrames, Last 30 Days, Claude SEO, Claude Ads, AnyDoc, QMD) — none is installed in the review environment. `scripts/smoke-test.sh` reports presence on the Droplet.
- Hermes Kanban API shape. `pipeline.yaml` is the contract; the binding to Hermes's board is done at install on the Droplet.
- The end-to-end Definition of Done run. Sheet: `tests/acceptance/end-to-end-run.md`.

## To reach PASS
Close F1 and F2 (Rachel decisions and source material). F3–F5 are one-line confirmations. Then run Block A and the end-to-end sheet on the Droplet.
