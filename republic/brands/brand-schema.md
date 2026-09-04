# Brand profile schema — what `republic-writing` expects

Republic Writing reads the brand's **existing** profile in the vault. This is not a
new directory to create. It is the list of fields the skill looks for; the gap
analysis maps each to where it already lives, and only genuinely missing fields are
added to the existing profile.

| Field | Used by | Content | If missing |
|---|---|---|---|
| `brand` | all | name, positioning, visual tokens (colors, fonts, caption style, logo) | HyperFrames refuses to render; add tokens |
| `voice` | Voice DNA, final QA | recurring phrases, preferred and disliked vocabulary, cadence, humor, polish level, openers/closers, **each traced to real human material** (transcripts, emails, posts, conversations, approved writing) | Writing refuses to draft; extract from transcripts first |
| `audience` | angles | segments, verbatim questions, their language for the problem and result | angles run on research brief only, flagged |
| `offers` | conversion writing | what, price, booking path, characteristics that may be claimed | direct response refuses; add |
| `proof` | conversion writing, reviews | verbatim, sourced, dated, consent noted | no proof claims allowed |
| `objections` | conversion writing | in customer words, with honest answers from offers/proof | flagged |
| `prohibited-claims` | final QA | scope-of-practice, guarantees, competitor naming, before/after without consent, platform-sensitive terms | **blocking** — add before any draft |
| `approved-examples` | Voice DNA, final QA | published writing in this voice, with why it was approved | QA compares to `voice` only, flagged |

Physically Meta specifics to record where the profile lives: massage scope-of-practice
language belongs in `prohibited-claims`; GBP and Facebook matter for a local business;
first learning-loop attributes to track are demonstration-first vs talking openings.
