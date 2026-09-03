---
name: republic-platform-experts
description: 03_CONTENT platform expertise for Instagram, TikTok, YouTube, Facebook, LinkedIn, and Google Business Profile. Answers one question — given this content and objective, what should this become on my platform? — producing a native platform brief (format, length, hook placement, metadata, caption behavior, presentation). Use when a card enters PLATFORM_BRIEF. Consumes shared research and writing; never researches or writes independently.
version: 1.0.0
department: 03_CONTENT
tags: [republic, platforms, instagram, tiktok, youtube, facebook, linkedin, gbp]
---

# Platform experts

Persistent expertise only where it provides value. Shared services (research, writing,
editing, Librarian) are consumed, not duplicated. (SPEC §3)

## The one question
**Given this content and objective, what should this become on my platform?**

## Procedure
1. Load the card's core content object, objective, writing mode, Research Brief, and
   Video Vision analysis. Do not re-research. Do not redraft the core idea.
2. For each target platform in the card, load `references/<platform>.md` and produce a
   **Platform Brief**: format · length/duration · hook placement and timing · metadata
   (title, tags, alt text, location) · caption behavior · platform-native presentation
   notes · asset requirements for production · publishing notes for GHL.
3. Hand the briefs to `republic-writing-system` (copy) and `republic-editing` /
   `republic-hyperframes` (assets) via the card. Move to PRODUCTION.

## Platform files
`references/instagram.md`, `tiktok.md`, `youtube.md`, `facebook.md`, `linkedin.md`,
`gbp.md`. Each holds current format norms and is updated only through the learning
loop (evidence) or a v1.1 change, never ad hoc per post.

## Boundaries
- No platform expert owns research, a copywriter, an editor, or a Librarian.
- Never changes the objective or writing mode set by STRATEGY.
- If a platform file is stale (older than 90 days by its `updated:` line), flag it on
  the card; do not guess new norms.
