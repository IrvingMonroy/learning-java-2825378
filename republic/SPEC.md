# The Republic — v1 Upgrade Specification

**Status:** FROZEN (decisions closed; this supersedes the earlier "departments" draft)
**Owner:** Rachel Hightower
**Reviewer:** Claude, independent QA (`qa/QA_CONTRACT.md`)
**Runtime:** the existing Republic on Hermes Agent (VPS Droplet), Socrates as interface
**Version:** 1.0.0

## 0. Posture

The Republic already exists. It has a SOUL/identity, profiles, a Librarian, knowledge in
Obsidian with QMD retrieval, Kanban job creation, a GHL direction, and a working
raw-video → Instagram workflow. **This is not a rebuild.**

```
CURRENT REPUBLIC
      │
      ├── existing SOUL / identity
      ├── existing profiles
      ├── existing Librarian
      ├── existing knowledge
      └── existing workflows
               │
               ▼
         ADD CAPABILITIES
```

**The conservative rule:** Preserve working behavior. Add missing capability. Replace only demonstrated weak behavior.

## 1. Preserved — do not touch

| Existing piece | Rule |
|---|---|
| Republic SOUL / identity | Not rewritten because new skills appeared |
| Profiles, including the Instagram profile | If it works, it is not rebuilt |
| Librarian | Instructions are upgraded in place (§3, Batch 3); never replaced |
| Knowledge: Obsidian + QMD | Untouched; QMD stays retrieval/index only |
| Kanban job creation | Left intact; new capabilities attach to existing jobs |
| GHL publishing / direction | Not touched |
| Socrates capture and interface | Not touched |
| Raw video → Instagram workflow | Becomes the **baseline** the new editing stack is measured against |

Any change to a preserved piece requires a demonstrated defect (QA BLOCKER/DEFECT with
a reproduction) and Rachel's decision. "We found a better way" is a PREFERENCE.

## 2. Demonstrated weak behavior

**Video editing.** This is the only replacement target in v1 and the first batch.

## 3. Capabilities added

| Capability | Given to | Purpose | Batch |
|---|---|---|---|
| Video Vision | Republic / shared Mac Mini | Understand raw video: transcript, timestamps, moments, clips, hooks. Observes; Republic interprets | 1 |
| OpenMontage | Republic production | Automated editing of real footage | 1 |
| HyperFrames | Republic production | Programmatic, branded video generation from templates | 1 |
| Last 30 Days | Republic | Current trend and audience research, one pass per job | 2 |
| Republic Writing (one custom skill) | Republic | Voice DNA · ideation · angles · conversion writing · final voice QA, chosen by job | 2 |
| LLM-Wiki methodology | Librarian | Maintain coherent knowledge rather than pile up notes (instruction patch) | 3 |
| AnyDoc | Librarian | Make incoming documents machine-readable before the Librarian interprets them | 3 |
| Claude SEO access/workflow | Republic | SEO and local search specialist, bounded requests | 4 |
| Claude Ads access/workflow | Republic | Paid advertising specialist, bounded requests, spend gate | 4 |

Each capability is one skill directory under `skills/` (or one patch under `upgrades/`)
with front matter declaring `batch`, `adds_to`, `replaces`, and `preserves`.

## 4. Republic Writing — one skill, not five

```
REPUBLIC-WRITING
├── Ghostwriter Killer        → voice DNA
├── Blank Page Killer         → ideation / starting
├── 72 Reasons to Buy         → angles / motivations
├── Direct Response Copywriter→ conversion writing
└── AI Slop Killer            → final voice QA
```
The skill determines which behavior applies from the job's objective:
CONNECT / TEACH / STORY / THOUGHT LEADERSHIP → brand writing;
SELL / BOOK / OPT-IN / CONVERT → direct response. Conversion methodology never runs on
the first path. Every draft ends with the voice QA: *would this person actually say
this?* Voice DNA reads the brand's **existing** profile in the vault; the schema in
`brands/brand-schema.md` lists what it expects and what to add if missing.

## 5. Batches and gates

```
Batch 1  Video Vision + OpenMontage + HyperFrames
         → test against current editing → Claude QA → KEEP what works, REMOVE what doesn't
Batch 2  Last 30 Days + Republic Writing
Batch 3  Librarian LLM-Wiki upgrade + AnyDoc
Batch 4  Claude SEO + Claude Ads
DONE
```
A batch ships only on a Claude QA PASS. Nothing from a later batch is installed
before the earlier batch passes. Batch READMEs under `batches/` state each gate.

## 6. Production acceptance (Batch 1)

Same source videos, three runs: **baseline** (current raw-video → Instagram
workflow), OpenMontage, HyperFrames where the element type allows. Scored on quality,
Rachel intervention, time saved, caption quality, clip selection, brand consistency,
rendering reliability, cost, repeatability. A new tool holds a permanent position only
if it requires **less Rachel** than the baseline on that job. If OpenMontage does
something poorly and HyperFrames solves it, keep HyperFrames. If they duplicate, remove
one. If neither beats the baseline, the baseline stays. Sheet:
`tests/acceptance/editing-acceptance.md`.

## 7. Claude QA

Strict role: find defects, do not redesign. Contract in `qa/QA_CONTRACT.md`. Findings
are BLOCKER / DEFECT / IMPROVEMENT / PREFERENCE; only the first two block a batch.
A proposal to change a preserved piece without a reproduction is a PREFERENCE.

## 8. Boundaries retained from the design discussion

- Video Vision observes. Republic interprets. Raw media never sets strategy.
- Librarian: propose, don't destroy; every drop item gets exactly one outcome;
  canonical decisions `status: active`, `canonical: true`; superseded notes preserved
  and linked. LLM-Wiki adds *update the canonical note* to that, nothing removes it.
- The existing approval step before GHL publishing stays where it is. New skills never
  publish, schedule, or approve.
- Paid: no autonomous change to substantial ad budgets. Threshold in `config.yaml`.
- Learning: a single post proves nothing. Patterns become canonical knowledge only at
  `config.yaml → learning.min_sample` and with Rachel's acknowledgement.
- Workers: skills name tiers (local / frontier / metered), never model IDs. Model
  replacement is not a spec change.

## 9. Excluded (`FREEZE.md`)

Soup, PostHog, Herdr, DeepSeek Harness, Archify, Omarchy, Fincept, Vibe Trading,
anti-detection browser infrastructure, any additional writing "killer" skill, any new
orchestration framework. Added only when an actual need appears and meets the v1.1
criteria.

## 10. Definition of DONE

`DEFINITION_OF_DONE.md`. All four batches passed QA; the editing stack chosen and
recorded; Rachel can hand the week's videos to Socrates and get scheduled, approved
posts without coordinating tools. Then: **stop building. Run it.**
