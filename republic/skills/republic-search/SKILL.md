---
name: republic-search
description: 02_SEARCH. Delegates bounded search jobs to the Claude SEO specialist (local SEO, GBP, technical, content SEO, intent, Search Console, GEO/AI-search, competitor search) and returns structured results to The Republic. Use for any SEO request or when research needs search signals. Never ports Claude SEO internals into Hermes.
version: 1.0.0
department: 02_SEARCH
tags: [republic, seo, claude-seo, gbp, search-console]
---

# 02_SEARCH — Claude SEO as a bounded specialist

Republic requests. Claude SEO executes. Republic consumes. Internal Claude SEO agents
are opaque and stay that way. (SPEC §2, §15)

## Accepted request shapes
- `audit-local` — "Audit <brand>'s local search presence." → local/GBP audit
- `brief-page` — "Build the SEO brief for <service page>." → content SEO brief
- `intent` — "Intent clusters and question queries for <topic>." (used by research)
- `technical` — site technical audit
- `console` — Search Console readout for <property>, <window>
- `geo` — AI-search / GEO visibility check for <brand>, <queries>
- `competitor-search` — who ranks for <cluster> and how

Anything else is refused with: "Not a defined 02_SEARCH job; open an ops card."

## Procedure
1. Take the card's request; normalize to one of the shapes above with brand, target,
   and window filled in.
2. Invoke Claude SEO with exactly that request. Worker tier: `frontier`.
3. Validate the return: it must be structured (tables or keyed lists), dated, and name
   its data source. If prose-only, re-request once as structured. If still prose, attach
   as-is and flag `structure: weak` for QA.
4. Attach to the card. If the card is `search` type, move to QA. If it was a research
   sub-request, return the result to `republic-research`.

## Output contract
`Search Result` with: Request shape · Brand/target · Window · Findings (structured) ·
Recommended actions (ranked, each with expected effect) · Data sources · Run date.

## Boundaries
- No site changes, no GBP edits, no Search Console settings changes. Actions go to a
  card for Rachel or `republic-distribution` (GHL-side) to execute.
- Never uses metered workers for bulk keyword pulls that a local tier can reformat.
