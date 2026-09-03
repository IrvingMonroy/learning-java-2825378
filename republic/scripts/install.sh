#!/usr/bin/env bash
# Install Republic v1 skills into a Hermes Agent home.
# Usage: ./scripts/install.sh [--copy]   (default: symlink; --copy copies instead)
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
SKILL_DST="$HERMES_HOME/skills/republic"
PKG_DST="$HERMES_HOME/republic"
MODE="link"; [[ "${1:-}" == "--copy" ]] && MODE="copy"

echo "Republic v1 install → $HERMES_HOME ($MODE)"
python3 "$HERE/scripts/validate.py" || { echo "validate.py FAILED — not installing."; exit 1; }

mkdir -p "$SKILL_DST" "$HERMES_HOME/skills"
for d in "$HERE"/skills/*/; do
  name="$(basename "$d")"
  rm -rf "$SKILL_DST/$name"
  if [[ $MODE == link ]]; then ln -s "$d" "$SKILL_DST/$name"; else cp -r "$d" "$SKILL_DST/$name"; fi
done

# Package (spec, kanban, brands, templates, tests, qa) available to skills at a stable path.
rm -rf "$PKG_DST"
if [[ $MODE == link ]]; then ln -s "$HERE" "$PKG_DST"; else cp -r "$HERE" "$PKG_DST"; fi

cat <<MSG

Installed $(ls "$HERE/skills" | wc -l | tr -d ' ') skills to $SKILL_DST
Package at $PKG_DST (SPEC.md, kanban/pipeline.yaml, brands/, hyperframes/)

Next:
  1. Run ./scripts/smoke-test.sh to see which external tools are reachable.
  2. Fill brands/physically-meta/voice.md from real transcripts (remove TODO-SOURCE).
  3. Confirm thresholds in kanban/pipeline.yaml (paid_spend, learning.min_sample).
  4. Start Block A: drop three videos in CONTENT_DROP/ and run the editing acceptance test.
MSG
