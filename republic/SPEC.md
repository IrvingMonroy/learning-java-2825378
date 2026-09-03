# The Republic — v1 Implementation Specification

**Status:** FROZEN (architecture decisions closed)
**Owner:** Rachel Hightower
**Reviewer:** Claude, independent QA (see `qa/QA_CONTRACT.md`)
**Runtime:** Hermes Agent (Nous) on the VPS Droplet, reached over Tailscale
**Version:** 1.0.0

This document is the authoritative description of what Republic v1 is. It records
decisions already made. It is not a design discussion. Changes to this document
after v1 ships follow the v1.1 change policy in `FREEZE.md`.

---

## 1. Governing architecture

```
                         RACHEL
                            │
                            ▼
                       SOCRATES
                 Personal EA / interface
                            │
                   submits requests
                            ▼
                    ╔══════════════╗
                    ║ THE REPUBLIC ║
                    ╚══════════════╝
                            │
                         KANBAN
                            │
     ┌──────────┬───────────┼───────────┬───────────┐
     ▼          ▼           ▼           ▼           ▼
 RESEARCH     SEARCH      CONTENT    PRODUCTION     PAID
     │          │           │           │           │
     │      Claude SEO      │       Video Vision  Claude Ads
     │                      │       OpenMontage
     │                      │       HyperFrames
     └──────────────┬───────┴───────────┘
                    ▼
                   GHL
          publishing / CRM / automation
                    ▼
                 RESULTS
                    ▼
                LIBRARIAN
                    │
             Obsidian + QMD
                    │
                    └────→ Republic learns
```

Claude sits outside this loop:

```
Republic build/change → Claude independent QA → PASS / FAIL / findings → fix only demonstrated issues
```

Claude does not redesign Republic every time it reviews it.

**Roles**

| Actor | Role | Never does |
|---|---|---|
| Rachel | Principal. Approves. Sets direction. | Coordinates models by hand |
| Socrates | Personal EA / interface. Captures, submits requests, reports status. | Posts, schedules, approves, edits video |
| The Republic | Orchestrator. Owns *what* and *why*. Routes work through Kanban to departments. | Executes publishing itself; redesigns itself |
| Departments | Six permanent functional areas (§2). | Own private copies of shared services |
| GHL | Execution: scheduling, publishing, CRM, automation. | Decides strategy |
| Librarian | Knowledge governance in Obsidian; QMD reindex. | Destroys originals |
| Claude | Independent QA against this spec. | Redesigns; approves spend; publishes |

## 2. Permanent departments

Six permanent functional areas. Each is one Hermes skill directory under `skills/`.

### 01_RESEARCH — produces evidence
Last 30 Days; trend research; competitor research; review mining; customer-language
mining; audience questions; content opportunities; research briefs.
**Output:** a Research Brief. **Does not** write finished posts.

### 02_SEARCH — specialist: Claude SEO
Local SEO; Google Business Profile; technical SEO; content SEO; keyword and search
intent; Search Console; GEO / AI-search optimization; competitor search analysis.
Republic delegates bounded jobs to Claude SEO and receives structured output. The
Claude SEO ecosystem is **not** ported into Hermes.

### 03_CONTENT — editorial brain
Content strategy; campaigns; content briefs; angles; writing; platform adaptation;
brand voice. Contains the **Republic Writing System** (§4, §5), the **platform
experts** (§3), and **Repurposing** (§11).

### 04_PRODUCTION — highest-priority build
Media understanding; clip selection; editing; captions; graphics; generated visual
assets; rendering; formatting.
Core stack: **Video Vision + OpenMontage + HyperFrames.** Each must earn its
permanent position by passing the editing acceptance test (§10).

### 05_DISTRIBUTION_CRM — the GHL interface
Scheduling; publishing; CRM; lead capture; comment-to-DM; review workflows; nurture;
funnels; appointment and booking workflows. **GHL is not recreated inside Hermes.**

### 06_PAID — specialist: Claude Ads
Advertising audits; Meta; Google; TikTok; YouTube; campaign strategy; wasted-spend
identification; creative analysis; optimization plans. A specialist service, not
nineteen new Hermes agents.

## 3. Platform experts

Persistent expertise only where it provides value. Under CONTENT:
Instagram, TikTok, YouTube, Facebook, LinkedIn, Google Business Profile.

Their one question: **Given this content and objective, what should this become on
my platform?** They know format, audience expectations, hooks, length, metadata,
caption behavior, and platform-native presentation. They do **not** each own a
research department, copywriter, editor, or Librarian. Shared services do that.

## 4. The Republic Writing System (consolidated)

One system, four stages. The following are **not** installed as separate competing
skills: Blank Page Killer, Ghostwriter Killer, 72 Reasons to Buy, Copywriter Killer,
Slop Killer, Hook Agent, Caption Agent, CTA Agent. Their best principles are
absorbed into the stages below.

**Stage A — Voice DNA.** Each brand/client has a `BRAND/` directory:
`brand.md, voice.md, audience.md, offers.md, proof.md, objections.md,
prohibited-claims.md, approved-examples/`. `voice.md` is built primarily from real
human material: transcripts, emails, existing posts, conversations, approved writing,
recurring phrases, preferred and disliked vocabulary, cadence, humor, level of polish.

**Stage B — Blank-page generation.** Produces useful starting material when no draft
exists: concepts, hooks, outlines, story directions, structures, first drafts. It does
not automatically turn everything into conversion copy.

**Stage C — Angle generation.** Asks: *what credible reasons would different segments
of this audience care?* Grounded in reviews, DMs, comments, search, sales language,
customer questions, actual offer characteristics. Clustered into motivations. Not a
literal 72 claims.

**Stage D — Writing mode.** Objective is determined first:

```
CONNECT / TEACH / STORY / THOUGHT LEADERSHIP  →  BRAND WRITING
SELL / BOOK / OPT-IN / CONVERT                →  DIRECT RESPONSE
```
Direct-response methodology runs **only** on the second path.

## 5. Final Writing QA

Every draft is checked for: generic AI phrasing; fake profundity; excessive polish;
repetitive rhetorical patterns; unnecessary summaries; clichés; invented claims;
excessive adjectives; voice drift; forced CTAs; phrases the client doesn't use.

The goal is not to fool a detector. The permanent rule: **Would this person actually
say this?**

## 6. Research system

Last 30 Days is Republic's current-intelligence capability. One intelligence pass,
many outputs:

```
Research request → Last 30 Days + SEO signals + customer language + competitors
               → RESEARCH BRIEF → Republic Strategy → platform experts
```
Platforms never independently research the same subject.

## 7. Video intake

Raw media enters `CONTENT_DROP/`. Republic registers it as an intake item (Kanban
card in TRIAGE). Video Vision produces a structured analysis: transcript, timestamps,
subjects/topics, visual events, demonstrations, on-screen text, good moments,
awkward/dead sections, potential clips, possible hooks, visual context, content ideas.

**Video Vision observes. Republic interprets.** Video Vision does not decide strategy.

## 8. Editing engine

OpenMontage is tested as the primary editor for real footage:
`select moments → trim → assemble → captions → audio → B-roll/assets → format → render`.
This is the first component built in implementation.

## 9. HyperFrames

Separate job: programmatically generated branded video elements (animated educational
slides, statistics, quote cards, diagrams, title sequences, review animations, CTA
cards, explainers, branded overlays, promotional videos). Built as reusable templates
per brand, e.g. `hyperframes/templates/physically-meta/{educational-reel,
review-highlight, pain-explainer, faq, promotion, myth-vs-fact}`.
Republic supplies content. HyperFrames supplies repeatable production.

## 10. Editing acceptance test

Neither OpenMontage nor HyperFrames is kept for being interesting. For the same
content, each is scored on: Quality; Rachel intervention required; Time saved; Caption
quality; Clip selection; Brand consistency; Rendering reliability; Cost; Repeatability.
The permanent system must require **less Rachel**, not merely produce more AI. If a
tool does something poorly, Claude QA identifies it. If the other tool solves it, keep
that one. If they duplicate each other, remove one. Rubric: `tests/acceptance/editing-acceptance.md`.

## 11. Repurposing

One Repurposing skill. Input is the **core content object**, not a platform post.
```
CORE IDEA → IG (native) / TikTok (native) / YouTube (native) / …
```
Platform experts decide the transformation.

## 12. GHL publishing

Approved assets flow `Republic → GHL → schedule/publish`. Republic owns what and why.
GHL owns execution, for every platform GHL supports.

## 13. Comment-to-DM

No standalone product. A Republic capability that designs and manages the GHL
workflow: `POST → "Comment GUIDE" → GHL trigger → public reply → DM → resource →
CRM contact/tag → nurture → booking/conversion`. Republic designs. GHL executes.

## 14. Reputation

GHL review capabilities plus Republic intelligence:
```
NEW REVIEW → sentiment → good | neutral | sensitive
             good/neutral → reply draft ; sensitive → owner alert
           → customer-language extraction → Republic knowledge
```
Positive reviews become voice-of-customer research. Recurring negatives become
operational intelligence.

## 15. Search department

Claude SEO as a bounded specialist. Republic requests, e.g. "Audit Physically Meta's
local search presence" or "Build the SEO brief for this service page." Claude SEO
executes; Republic consumes structured results. Internal Claude SEO agents are opaque.

## 16. Paid department

```
Republic → Paid Acquisition request → Claude Ads → audit/strategy/findings
        → Republic → Claude QA where appropriate → Rachel approval for meaningful spend/change
```
Experimental agents never autonomously alter substantial ad budgets. Threshold:
`kanban/pipeline.yaml → gates.paid_spend`.

## 17. Librarian upgrade

Existing Librarian rules remain authoritative, especially **Propose, don't destroy**
and **Every 00_DROP item gets exactly one outcome.** Added: LLM-Wiki behavior. After
judging something valuable, Librarian asks whether it UPDATES, CONTRADICTS,
STRENGTHENS, or SUPERSEDES existing knowledge; CHANGES a project; CREATES a
relationship; REVEALS a reusable concept; or CREATES a decision. Then it updates the
canonical note rather than creating another random one. Raw material is preserved.
Canonical decisions carry `status: active` / `canonical: true`; superseded decisions
are preserved and linked, never silently overwritten.

## 18. AnyDoc

Before Librarian interpretation when needed: `DOCX/PPTX/XLSX/EPUB/PDF/CSV → AnyDoc
→ Markdown → Librarian`. AnyDoc converts. It does not decide where knowledge belongs.

## 19. QMD

Obsidian = durable knowledge. QMD = retrieval/index. Librarian = governance.
Hermes = reasoning/orchestration. QMD is not a database-of-everything. After
meaningful Librarian changes the relevant collection is reindexed. Archive/discard
material is excluded from normal retrieval.

## 20. Understand Anything

For Rachel's comprehension, not Republic's runtime. Pointed first at the AI
operating-system documentation (Socrates ↔ Republic ↔ profiles ↔ skills ↔ systems ↔
knowledge). Reduce scope if overwhelming. Not a source of truth.

## 21. Kanban is Republic's operational truth

Hermes Kanban represents actual work. Content job columns:
`TRIAGE → RESEARCH → STRATEGY → PLATFORM BRIEF → PRODUCTION → QA → RACHEL APPROVAL →
SCHEDULED → PUBLISHED → MEASURED → DONE`. **Chat = interaction. Kanban = state.**
Definition: `kanban/pipeline.yaml`.

## 22. Claude is the QA layer

Strict role: find defects, do not redesign. Full contract in `qa/QA_CONTRACT.md`.
Findings are BLOCKER / DEFECT / IMPROVEMENT / PREFERENCE. Only BLOCKER and DEFECT
prevent Republic v1 from shipping.

## 23. Models and workers

Model selection is not architectural. Republic uses the appropriate worker (Qwen
local, Claude, Codex, other) per the existing `model-routing` skill. Every workflow
must survive model replacement. Skills reference **worker tiers**, never model IDs.

## 24. Soup

Not installed. Skills are structured so a router (`Republic → [future router] →
skill library`) could be inserted later. Soup is evaluated only if Hermes skill
selection proves unreliable.

## 25. Explicitly excluded from v1

No DeepSeek Harness. No Herdr. No Omarchy. No Fincept. No Vibe Trading. No
anti-detection browser infrastructure (unless a legitimate workflow later requires
specialized browser automation). No additional writing "killer" skills. No new
orchestration framework. This is the freeze boundary (`FREEZE.md`).

## 26. The learning loop

```
publish → performance → what happened? → Librarian → evidence accumulates
       → meaningful pattern? → update canonical knowledge
```
Republic does not rewrite itself per post. A single underperforming Reel proves
nothing. A pattern across a sufficient sample (`kanban/pipeline.yaml →
learning.min_sample`) becomes durable brand knowledge.

## 27. PostHog

Not installed in v1. Measurement uses GHL data, native social analytics, Search
Console, and ad-platform data. Added only when a specific measurement gap is
identified.

## 28. Implementation sequence

Five build blocks:

- **Block A — Production first:** Video Vision → OpenMontage → HyperFrames → QA → choose permanent editing stack.
- **Block B — Republic intelligence:** Last 30 Days → Research → Writing System → brand schemas → platform experts.
- **Block C — Growth:** Claude SEO → GHL comment-to-DM / reputation / CRM → Claude Ads.
- **Block D — Knowledge:** Librarian LLM-Wiki upgrade → AnyDoc → QMD → Understand Anything.
- **Block E — Control:** Kanban → Claude QA contract → acceptance tests → documentation → freeze.

## Definition of DONE

See `DEFINITION_OF_DONE.md`. In one line: Rachel can say *"Here are the videos I
recorded this week. Handle social for Physically Meta,"* and the system runs
`ingest → understand → research → decide → write → edit → adapt → QA → present for
approval → schedule → publish → capture results → preserve learning` without Rachel
coordinating models, digging through terminals, copying prompts, hand-editing every
video, or remembering what happened. Then: **stop building. Run it.**
