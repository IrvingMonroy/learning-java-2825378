---
name: republic-claude-seo
description: Gives the existing Republic a bounded workflow for the Claude SEO specialist — local SEO, Google Business Profile, technical and content SEO, keyword and search intent, Search Console readouts, GEO/AI-search visibility, competitor search analysis. Republic sends a defined request such as "Audit Physically Meta's local search presence" or "Build the SEO brief for this service page" and receives structured results. Use for any SEO request or when research needs search signals. Claude SEO internals are not ported into Hermes.
version: 1.0.0
batch: 4
adds_to: Republic (specialist access)
replaces: nothing
preserves: [existing site, GBP, and Search Console settings — read only]
tags: [republic, seo, claude-seo, gbp, search-console, batch-4]
---

# Claude SEO — bounded specialist

Republic requests. Claude SEO executes. Republic consumes. (SPEC §3)

## Request shapes
`audit-local` · `brief-page <page>` · `intent <topic>` · `technical` · `console <window>` ·
`geo <queries>` · `competitor-search <cluster>`. Anything else → "not a defined SEO job;
open a job for Rachel."

## Procedure
1. Normalize the job's request to one shape with brand, target, window.
2. Invoke Claude SEO with exactly that. Worker tier `frontier`.
3. Require structured, dated output naming its data source. Prose-only → re-request
   once as structured; still prose → attach and flag `structure: weak`.
4. Attach to the job. Recommended actions become a job for Rachel or the existing GHL
   step. This skill changes nothing itself.

## Boundaries
- No site edits, GBP edits, or Search Console changes.
- No metered workers for bulk keyword pulls a local tier can reformat.
