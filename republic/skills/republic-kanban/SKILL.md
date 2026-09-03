---
name: republic-kanban
description: Owns card lifecycle on the Hermes Kanban board according to kanban/pipeline.yaml — creating cards, validating column transitions, enforcing that only Rachel moves cards out of RACHEL_APPROVAL, and answering any "what's the status of…" question from the board rather than from chat history. Use for all status questions and all column moves.
version: 1.0.0
department: control
tags: [republic, kanban, status, gates]
---

# Republic Kanban — state, not chat

**Chat = interaction. Kanban = state.** Rachel never searches agent chats for status.
(SPEC §21)

## Source of truth
`kanban/pipeline.yaml` in this package. Columns, gates, thresholds, and paths are read
from it. This skill never hardcodes a number.

## Procedure — transitions
1. On any request to move a card, load its `type` and look up `paths.<type>`.
2. Allow only a move to the next column in that path, or a return to any earlier
   column (with a note). Skipping forward is rejected.
3. **Gate enforcement.** A move out of `RACHEL_APPROVAL` is accepted only from Rachel's
   identity (Socrates relays with `actor: rachel`). Any other actor's request is
   rejected and logged as a boundary event for QA.
4. On entering `QA`, notify `republic-qa`. On entering `SCHEDULED`, notify
   `republic-distribution`. On entering `MEASURED`, notify `republic-learning-loop`.
5. Append `{stage, tier, note}` to `worker_log` on each column exit. Tier, never model.

## Procedure — status questions
Answer from the board only: card ID, column, owner, last update, blocking item if any.
Format: one line per card. If Rachel asks "why is it stuck", quote the card's most
recent note. Never reconstruct status from conversation memory.

## Procedure — health
Daily: list cards older than 7 days in any non-terminal column; cards in QA with FAIL
and no owner move; cards in RACHEL_APPROVAL older than 3 days (remind once, via
Socrates). Report as a single digest.

## Boundaries
- Never moves a card out of RACHEL_APPROVAL on its own.
- Never edits `pipeline.yaml`. Threshold changes are Rachel's, via a v1.1 change.
- Kanban unreachable → say so on the Socrates channel. Do not fall back to chat state.
