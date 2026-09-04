# QA Report — Republic v1 upgrade package (initial, before gap analysis)

- **Date:** 2026-09-03
- **Reviewer:** Claude (independent QA)
- **Scope:** `SPEC.md` (upgrade-in-place posture) and the package as pushed. Static review
  plus `scripts/validate.py`. **Not in scope:** the existing Republic on the Droplet and
  the vault — Claude has not read them yet (`GAP_ANALYSIS.md` is NOT RUN).
- **Spec version:** 1.0.0
- **Verdict:** **FAIL** — one BLOCKER (F1) and one DEFECT (F2) open. Both are inputs
  from Rachel, not redesigns. Supersedes the earlier "departments" review, which was
  written against a rebuild the spec no longer describes.

## Findings

| ID | Class | SPEC § | Summary | Reproduction | Smallest fix |
|---|---|---|---|---|---|
| F1 | BLOCKER | §1, §5 | Additivity is asserted, not verified. Every skill declares `adds_to` an existing step by description only. Without reading the Droplet's skills/profiles and the vault, a name or behavior collision with a preserved piece cannot be ruled out. | Install Batch 1 → a same-purpose skill or profile step already exists → two behaviors compete (the skill-soup failure). Expected: gap analysis result table filled first. | Give Claude read access (attach the vault repo, or paste Hermes `skills/`, `profiles/`, SOUL, Librarian instructions, and the current video → Instagram workflow). Run `GAP_ANALYSIS.md`. Delete or trim what collides. |
| F2 | DEFECT | §4, `brands/brand-schema.md` | Republic Writing requires a `voice` field traced to real human material and a `prohibited-claims` field. Neither is known to exist in the Physically Meta profile. The skill refuses to draft without them (by design), so Batch 2 cannot pass. | Batch 2 job → `republic-writing` reads profile → `voice` untraced → stops. | Map existing profile fields in the gap analysis; extract voice from 3+ transcripts/posts; add scope-of-practice prohibited claims. No code change. |
| F3 | DEFECT | §8 | "Meaningful spend/change" has no number in the spec. `config.yaml` defaults: $50 absolute or 20% relative, `autonomous_allowed: false`. | Claude Ads recommends +$40/day → gate or not? | Rachel confirms or edits two numbers. |
| F4 | DEFECT | §8 | "Sufficient evidence" has no number. `config.yaml` defaults: `min_sample: 12`, 7-day window, Rachel acknowledgement before canonical. | 6 Reels show a pattern → canonical or not? | Rachel confirms or edits. |
| F5 | IMPROVEMENT | §6 | The baseline workflow (raw video → Instagram) is named but its steps and typical Rachel-intervention count are not recorded anywhere Claude can read. The acceptance test needs that baseline row. | Fill the acceptance sheet → Baseline column has no reference. | Record one baseline run (time, interventions, output) before Batch 1 tools run. Already in `batches/batch-1-production.md` step 2. |
| F6 | IMPROVEMENT | §3 | Video Vision is "Republic / shared Mac Mini." The package assumes it is reachable from the Droplet over Tailscale like Ollama. Unverified. | `smoke-test.sh` on the Droplet → Video Vision missing → Batch 1 blocked. | Confirm the endpoint or run Video Vision on the Mac Mini and drop the analysis file into the job. |
| F7 | PREFERENCE | §1 | The package keeps HyperFrames template specs under `hyperframes/templates/`; the vault may prefer them next to the brand profile. | — | Move at install if the vault has a convention. One line, no advocacy. |

## Boundary check

| Boundary | Verified | Note |
|---|---|---|
| Socrates never publishes, schedules, approves | ☑ | No skill grants Socrates anything |
| No added skill bypasses the existing approval step | ☑ | Every skill's Boundaries says it never publishes/approves |
| Paid spend above gate is never autonomous | ☑ | `config.yaml`; `republic-claude-ads` applies nothing |
| Librarian preserves originals; supersedes are linked | ☑ | Patch is append-only; states it removes no rule |
| Claude never approves or publishes | ☑ | Contract; QA skill removed from package (Claude runs QA from the contract, not as a Hermes skill) |
| Skills reference worker tiers, not model IDs | ☑ | `validate.py` regex PASS |
| Preserved pieces unchanged | ☐ | Cannot verify until pre-upgrade copies exist; F1 |

## Operability check
| Question | Answer |
|---|---|
| Can Rachel get status from Kanban alone? | Yes, unchanged: the package adds no status surface |
| Any step requiring a terminal or agent chat? | Install and smoke test only (operator, one-time per batch) |
| Any prompt copied between tools? | No by design; Librarian patch is a one-time append |
| Any model name Rachel needs to know? | No |

## Verified
- `scripts/validate.py` PASS: eight additive capabilities across four batches; every skill declares batch, adds_to, replaces, preserves; only the editing candidate may replace anything and only via acceptance; no skill name claims a preserved piece; no excluded tool; no `kanban/` or brand directories that would duplicate existing structure; Librarian patch is append-only with all eight questions; acceptance sheet has a Baseline column.

## Not verified
- Anything on the Droplet, the Mac Mini, or in the vault. Every external tool. The Hermes skill loader's front-matter tolerance for the extra keys (`batch`, `adds_to`, `replaces`, `preserves`) — standard Agent Skills loaders ignore unknown keys; confirm on first install.

## To reach PASS
Close F1 by giving Claude read access and running the gap analysis. Close F2 by extracting voice and prohibited claims into the existing profile. Confirm F3 and F4. Then run Batch 1.
