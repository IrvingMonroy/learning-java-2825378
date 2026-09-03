---
name: republic-video-intake
description: 04_PRODUCTION media understanding. Runs Video Vision on raw media registered from CONTENT_DROP/ and attaches a structured analysis (transcript, timestamps, topics, visual events, demonstrations, on-screen text, good moments, dead sections, potential clips, possible hooks, visual context, content ideas) to the Kanban card. Video Vision observes; Republic interprets. Use for every new video or audio intake item.
version: 1.0.0
department: 04_PRODUCTION
tags: [republic, video, video-vision, intake, transcript]
---

# Video intake — Video Vision observes, Republic interprets

Raw media never decides strategy. (SPEC §7)

## Procedure
1. Receive the card from `republic-triage` with a `CONTENT_DROP/` path. Confirm the
   file is readable and note duration, resolution, and audio presence. Never move or
   rename the original.
2. Run Video Vision. Required output fields — any missing field is recorded as
   `missing`, never filled in by guess:
   - transcript (with speaker if detectable)
   - timestamps
   - subjects / topics
   - visual events
   - demonstrations (what is physically shown)
   - on-screen text
   - good moments
   - awkward / dead sections
   - potential clips (start, end, why)
   - possible hooks (quoted from transcript)
   - visual context (setting, lighting, framing issues)
   - content ideas (observational: "she explains X while demonstrating Y")
3. Transcript cleanup at worker tier `local`: fix mis-hearings only. Rachel's phrasing
   is never rewritten (model-routing hard rule 2).
4. Attach `video-analysis.md` to the card. Move the card to RESEARCH.

## Boundaries (interpretation)
Video Vision's `content ideas` and `possible hooks` are **observations**. They are
inputs to research and strategy, not decisions. This skill never sets objective,
platform, or writing mode, and never selects the final clip. Clip selection happens
in `republic-editing` against the Platform Brief.

## Error handling
- Video Vision unavailable → card note `video-vision: unavailable`, card stays in
  TRIAGE, Socrates informed once. No silent retry loop; one retry after 10 minutes.
- Unreadable or corrupt file → card note with the error; ask Rachel via Socrates for
  a re-drop. Do not attempt repair.
