---
name: republic-repurposing
description: 03_CONTENT's single Repurposing skill. Takes the CORE CONTENT OBJECT (idea, evidence, approved copy, source media) — never a finished platform post — and coordinates platform experts to produce native versions for each target platform. Use when a job targets more than one platform or when existing core content is re-run for a new platform.
version: 1.0.0
department: 03_CONTENT
tags: [republic, repurposing, multi-platform]
---

# Repurposing — from the core, not from a post

```
Bad:   Instagram Reel → copy it everywhere
Good:  CORE IDEA → IG (native) · TikTok (native) · YouTube (native)
```
(SPEC §11)

## The core content object
Lives on the card at STRATEGY exit:
`{idea, objective, writing_mode, angle_id, evidence (brief refs), approved_copy_core,
source_media (Video Vision refs), brand}`. Every platform version derives from this
object. A platform version is never the input for another platform version.

## Procedure
1. Verify the core content object is complete. If a job arrives as "make the IG post
   into a TikTok", reconstruct the core object from the card first; if it cannot be
   reconstructed, return the card to STRATEGY.
2. For each target platform, request a Platform Brief from `republic-platform-experts`
   against the core object.
3. Route copy to `republic-writing-system` per brief; assets to `republic-editing` or
   `republic-hyperframes` per brief. Each platform version carries `derived_from: core`.
4. Collect versions on the card. Move to QA.

## Boundaries
- Never produces a platform version by editing another platform's version.
- Never invents new claims during adaptation; adaptation changes form, not evidence.
- Platform experts decide the transformation; this skill only coordinates.
