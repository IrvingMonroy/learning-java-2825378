---
name: republic-research
description: 01_RESEARCH. Runs ONE intelligence pass per job — Last 30 Days current intelligence, SEO signals from 02_SEARCH, customer language from reviews/DMs/comments, and competitor observation — and produces a single Research Brief that strategy and all platform experts consume. Use when a card enters RESEARCH. Produces evidence; never finished posts.
version: 1.0.0
department: 01_RESEARCH
tags: [republic, research, last-30-days, evidence]
---

# 01_RESEARCH — one pass, many outputs

**Rule:** platforms never independently research the same subject. (SPEC §2, §6)

## Responsibilities
Last 30 Days; trend research; competitor research; review mining; customer-language
mining; audience questions; content opportunities; research briefs.

## Procedure
1. **Frame the question** from the card's `## Intake` and Video Vision analysis
   (topics, demonstrations, hooks observed). One question per brief.
2. **Current intelligence.** Run Last 30 Days for the topic and brand niche. Record
   run date. If the tool is unavailable, mark the brief `current-intel: missing` and
   continue with the other sources. Never fabricate recency.
3. **Search signals.** Request from `republic-search`: intent clusters and question
   queries for the topic. Bounded ask, structured answer.
4. **Customer language.** Pull from the brand's `proof.md`, `objections.md`, recent
   GHL reviews, DM and comment exports in the vault. Quote verbatim. Tag each quote
   with source and date.
5. **Competitors.** Note what is being said and what is *not* being said. Observation
   only, no copying.
6. **Write the Research Brief** (`references/research-brief.md` format). Worker tier:
   `local` for extraction and clustering; `frontier` for the synthesis section if the
   topic is strategic.
7. Attach the brief to the card. Move to STRATEGY.

## Output contract
Exactly one `Research Brief` per card, with sections: Question · Current intelligence
(dated) · Search intent · Customer language (quoted, sourced) · Competitor
observations · Content opportunities · Gaps and cautions · Sources.

## Boundaries
- Does not write posts, hooks, or captions. Opportunities are stated as evidence
  ("customers repeatedly ask X"), not as copy.
- Does not decide objective or platforms.
- Every claim in the brief has a source line or is marked `inference`.
