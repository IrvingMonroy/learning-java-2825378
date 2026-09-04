---
name: republic-video-vision
description: Adds Video Vision to the existing Republic video intake. Runs on the shared Mac Mini and attaches a structured observation of raw footage (transcript, timestamps, topics, visual events, demonstrations, on-screen text, good moments, dead sections, potential clips, possible hooks, visual context, content ideas) to the existing Kanban job. Video Vision observes; Republic interprets. Use whenever raw video or audio enters the existing intake.
version: 1.0.0
batch: 1
adds_to: existing Republic video intake and Kanban job
replaces: nothing
preserves: [existing intake workflow, Kanban job creation, raw files in place]
tags: [republic, video-vision, intake, transcript, batch-1]
---

# Video Vision — observe, don't decide

Attaches to the job the existing Republic already creates for incoming media. It does
not create jobs, move raw files, or set strategy. (SPEC §3, §8)

## Procedure
1. Take the job's raw media path from the existing intake. Confirm readable; note
   duration, resolution, audio presence. Never move or rename the original.
2. Run Video Vision (Mac Mini over Tailscale; worker tier `local`). Required fields,
   each recorded as `missing` if absent, never guessed:
   transcript · timestamps · subjects/topics · visual events · demonstrations ·
   on-screen text · good moments · awkward/dead sections · potential clips (start,
   end, why) · possible hooks (quoted) · visual context · content ideas (observational).
3. Transcript cleanup fixes mis-hearings only. Rachel's phrasing is never rewritten.
4. Attach `video-analysis.md` to the job in the place the existing workflow keeps
   intake notes. Hand back to the existing workflow's next step.

## Interpretation line
`content ideas` and `possible hooks` are observations for the existing strategy step.
This skill never chooses objective, platform, or final clip. Clip selection happens
in editing against the brief.

## Error handling
Video Vision unreachable → note `video-vision: unavailable` on the job, tell Socrates
once, retry once after 10 minutes, then leave the job where the existing workflow
would leave a job with no transcript. Corrupt file → note the error, ask via Socrates
for a re-drop. No repair attempts.

## Boundaries
- Never publishes, edits, or decides. Never touches the existing intake logic.
