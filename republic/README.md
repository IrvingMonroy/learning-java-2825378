# The Republic — v1 upgrade package

The Republic already runs on Hermes Agent on the VPS Droplet: SOUL, profiles, Librarian,
Obsidian + QMD knowledge, Kanban jobs, a GHL direction, and a working raw-video →
Instagram workflow. This package **feeds it carefully selected capabilities** and
gives Claude a strict QA role. It does not rebuild anything.

**Rule:** Preserve working behavior. Add missing capability. Replace only demonstrated
weak behavior. The one demonstrated weak behavior is video editing, so Batch 1 is
production.

Read in order: `SPEC.md` → `GAP_ANALYSIS.md` → `batches/` → `qa/QA_CONTRACT.md` →
`DEFINITION_OF_DONE.md` → `FREEZE.md`.

## Layout

```
republic/
├── SPEC.md                  upgrade specification (frozen)
├── GAP_ANALYSIS.md          what must be read on the existing Republic before install
├── config.yaml              thresholds (paid spend gate, learning sample, review policy)
├── batches/                 one README per batch: what is added, the QA gate
├── skills/                  additive Hermes skills, each tagged with its batch
├── upgrades/                instruction patches appended to existing pieces (Librarian)
├── brands/brand-schema.md   what Republic Writing expects from an existing brand profile
├── hyperframes/templates/   branded template specs (Physically Meta)
├── tests/acceptance/        editing acceptance (baseline vs new), end-to-end run sheet
├── qa/                      QA contract, report template, reports
└── scripts/                 validate.py, install.sh --batch N, smoke-test.sh
```

## Capabilities by batch

| Batch | Skill / patch | Adds to | Replaces |
|---|---|---|---|
| 1 | `republic-video-vision` | existing video intake | nothing |
| 1 | `republic-openmontage` | existing production step | manual editing, only if it passes acceptance |
| 1 | `republic-hyperframes` | existing production step | nothing |
| 2 | `republic-last-30-days` | existing research/idea step | nothing |
| 2 | `republic-writing` | existing drafting step | nothing (the five source skills are not installed) |
| 3 | `upgrades/librarian-llm-wiki.md` | existing Librarian instructions | nothing; appended |
| 3 | `republic-anydoc` | existing Librarian intake | nothing |
| 4 | `republic-claude-seo` | Republic | nothing |
| 4 | `republic-claude-ads` | Republic | nothing |

## Install (on the Droplet, one batch at a time)

```bash
cd republic
python3 scripts/validate.py            # package consistency
./scripts/install.sh --batch 1         # links only Batch 1 skills into ~/.hermes/skills/
./scripts/smoke-test.sh                # which external tools are reachable
```
Install the next batch only after Claude QA reports PASS on the current one. The
Librarian patch is applied by hand: append `upgrades/librarian-llm-wiki.md` to the
existing Librarian instructions; do not replace the file.

## Operating it
Talk to Socrates. Status comes from Kanban, as it does today. Approval happens where
it happens today. Anything that fails is a QA finding (`qa/QA_REPORT_TEMPLATE.md`),
not a redesign. New ideas go to the Librarian as *interesting, not actionable* unless
they meet `FREEZE.md`.
