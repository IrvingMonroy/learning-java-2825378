# The Republic — v1

The Republic is Rachel's AI operating system for content, distribution, and growth,
running on Hermes Agent on the VPS Droplet. Socrates is the interface. Six permanent
departments do the work. GHL executes. The Librarian keeps the knowledge. Claude is
the independent QA layer.

Read in this order:

1. `SPEC.md` — the frozen architecture and every decision behind it.
2. `DEFINITION_OF_DONE.md` — the single test that decides when to stop building.
3. `FREEZE.md` — what is excluded and what qualifies as a v1.1 change.
4. `qa/QA_CONTRACT.md` — Claude's role and finding classifications.

## Layout

```
republic/
├── SPEC.md                    frozen specification
├── DEFINITION_OF_DONE.md      end-to-end acceptance
├── FREEZE.md                  exclusions + change policy
├── qa/                        QA contract, report template, reports
├── kanban/                    pipeline columns, gates, thresholds, card template
├── skills/                    Hermes skills (one directory per skill, SKILL.md each)
├── brands/                    Voice DNA schema per brand/client
├── hyperframes/templates/     reusable branded video element specs
├── tests/acceptance/          editing acceptance rubric, end-to-end run sheet
└── scripts/                   install, validate, smoke test
```

## Skills

| Skill | Department | Purpose |
|---|---|---|
| `republic-triage` | Republic | Register intake, open Kanban cards, route to departments |
| `republic-research` | 01_RESEARCH | One intelligence pass → Research Brief |
| `republic-search` | 02_SEARCH | Bounded delegation to Claude SEO |
| `republic-writing-system` | 03_CONTENT | Voice DNA → blank page → angles → writing mode → Writing QA |
| `republic-platform-experts` | 03_CONTENT | Native adaptation per platform |
| `republic-repurposing` | 03_CONTENT | Core content object → native versions |
| `republic-video-intake` | 04_PRODUCTION | Video Vision analysis; observe, don't decide |
| `republic-editing` | 04_PRODUCTION | OpenMontage editing pipeline |
| `republic-hyperframes` | 04_PRODUCTION | Templated branded video elements |
| `republic-production-acceptance` | 04_PRODUCTION | Score editing tools; choose the permanent stack |
| `republic-distribution` | 05_DISTRIBUTION_CRM | GHL publishing, comment-to-DM, reputation |
| `republic-paid` | 06_PAID | Bounded delegation to Claude Ads with spend gate |
| `republic-librarian` | Knowledge | LLM-Wiki upgrade on existing Librarian rules |
| `republic-anydoc` | Knowledge | Documents → Markdown before Librarian |
| `republic-qmd` | Knowledge | Reindex after Librarian changes |
| `republic-learning-loop` | Knowledge | Evidence → pattern → canonical knowledge |
| `republic-kanban` | Control | Card lifecycle, gates, status answers |
| `republic-qa` | Control | The Claude QA contract as a runnable skill |

## Install on the Droplet

```bash
git clone <this repo> ~/republic-src
cd ~/republic-src/republic
python3 scripts/validate.py          # must pass before install
./scripts/install.sh                 # links skills into ~/.hermes/skills/republic/
./scripts/smoke-test.sh              # reports which external tools are present
```

External tools (Video Vision, OpenMontage, HyperFrames, Claude SEO, Claude Ads,
Last 30 Days, AnyDoc, QMD, Understand Anything) are installed separately per their
own docs. `smoke-test.sh` only reports whether each is reachable; a missing tool
blocks the department that depends on it and nothing else.

## Operating it

- Talk to **Socrates**. Ask for status from the **Kanban board**. Never from agent chats.
- Approve at the **RACHEL APPROVAL** column. That is the gate.
- When something fails, it is a QA finding, not a redesign. File it with `qa/QA_REPORT_TEMPLATE.md`.
- New ideas go to the Librarian as *interesting, not actionable* unless they meet `FREEZE.md`.
