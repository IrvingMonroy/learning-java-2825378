<!-- Republic v1, Batch 3. APPEND this to the existing Librarian instructions.
     Do not remove, reorder, or rewrite any existing rule. Existing rules stay authoritative:
     propose, don't destroy · every 00_DROP item gets exactly one outcome ·
     canonical decisions use status: active / canonical: true · superseded decisions
     are preserved and linked, never silently overwritten. -->

## LLM-Wiki pass (added in Republic v1)

After you have judged an item valuable under the existing rules, and before filing,
ask these eight questions in order and take the matching action. Update the canonical
note; do not create another random note.

| Does this… | Then |
|---|---|
| UPDATE existing knowledge? | Edit the canonical note. Add a dated changelog line. Link the source. |
| CONTRADICT existing knowledge? | Do not overwrite. Add a `contradiction` block with both claims and sources. If it affects a live decision, open a job for Rachel. |
| STRENGTHEN something? | Append to the canonical note's `evidence` list with source and date. |
| SUPERSEDE something? | Create the successor. Set the old note `status: superseded`, `superseded_by:`. Link both ways. |
| CHANGE a project? | Update the project note's status and next step. Link the source. |
| CREATE a relationship? | Add wikilinks in both directions with a one-line reason. |
| REVEAL a reusable concept? | Create or update one concept note. Link from every source that revealed it. |
| CREATE a decision? | Create a decision note with `status: proposed`. Rachel's acknowledgement moves it to `status: active`, `canonical: true`. |

Original and raw material stays at its ingest location and is linked from every note
it touched.

### Documents
Non-Markdown documents (DOCX, PPTX, XLSX, EPUB, PDF, CSV) arrive already converted by
AnyDoc as Markdown next to the original. Interpret the Markdown; keep the original.
AnyDoc never decides where knowledge belongs; you do.

### Performance evidence (learning loop)
Post-publish metrics arrive as evidence notes: one observation per post, no conclusion.
A pattern becomes a proposed canonical update to brand knowledge only when the sample
reaches `config.yaml → learning.min_sample` and the difference is substantial and
consistent. Not "this Reel underperformed, so question hooks don't work." Rather
"across 18 Physically Meta Reels, demonstration-first openings outperform talking
introductions." Proposed until Rachel acknowledges.

### After a meaningful change
Reindex the affected QMD collection as you do today. Archive and discard material
stays excluded from normal retrieval.
