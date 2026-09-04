# Gap Analysis — existing Republic vs. this upgrade package

**Status: NOT YET RUN.** Claude has not had read access to the existing Republic (the
Droplet's Hermes home and the vault). Until it does, every skill in this package is
*believed* additive, not *verified* additive.

## What Claude needs to read (read-only)

| Source | Why |
|---|---|
| Hermes home: `skills/`, `profiles/`, SOUL/identity file | To list what exists and detect name or behavior overlap |
| Existing Librarian instructions | To write the LLM-Wiki patch as an append, in the Librarian's own structure |
| Vault brand profiles | To map Republic Writing's Voice DNA onto existing fields instead of new files |
| The current raw-video → Instagram workflow (skill, profile, or run notes) | Baseline for the editing acceptance test |
| Kanban job conventions (how a job is created, named, moved) | So new capabilities attach to jobs instead of inventing cards |
| GHL publishing step and its approval gate | To confirm new skills sit upstream of it and never touch it |

Provide by attaching the vault repo to the session, or pasting directory listings and
the relevant files.

## Procedure (per capability)

1. **Exists already?** Search existing skills/profiles for the same job. If found:
   package skill is deleted, or reduced to a patch appended to the existing one.
2. **Overlaps partially?** Package skill is trimmed to the missing part only and
   declares `adds_to:` the existing piece by name.
3. **Genuinely missing?** Package skill installs as-is, in its batch.
4. **Demonstrated weak?** Only video editing qualifies in v1. Replacement follows the
   acceptance test, never a judgment call.

## Result table (fill during the run)

| Capability | Existing piece found | Decision: keep / trim / delete / patch | Evidence |
|---|---|---|---|
| Video Vision | | | |
| OpenMontage | | | |
| HyperFrames | | | |
| Last 30 Days | | | |
| Republic Writing | | | |
| Librarian LLM-Wiki patch | | | |
| AnyDoc | | | |
| Claude SEO workflow | | | |
| Claude Ads workflow | | | |
| `config.yaml` thresholds | | | |
| `brands/brand-schema.md` | | | |
