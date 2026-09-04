#!/usr/bin/env bash
# Install ONE batch of Republic v1 capabilities into an existing Hermes home. Additive only.
# Usage: ./scripts/install.sh --batch N [--copy]
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
SKILL_DST="$HERMES_HOME/skills"
PKG_DST="$HERMES_HOME/republic-upgrade"
BATCH=""; MODE="link"
while [[ $# -gt 0 ]]; do case "$1" in --batch) BATCH="$2"; shift 2;; --copy) MODE="copy"; shift;; *) echo "unknown arg $1"; exit 2;; esac; done
[[ -z "$BATCH" ]] && { echo "usage: install.sh --batch N [--copy]  (one batch at a time; next batch only after Claude QA PASS)"; exit 2; }
[[ -d "$HERMES_HOME" ]] || { echo "No Hermes home at $HERMES_HOME. This installs INTO an existing Republic; set HERMES_HOME."; exit 1; }

python3 "$HERE/scripts/validate.py" || { echo "validate.py FAILED — not installing."; exit 1; }

# Refuse to overwrite anything that already exists under a different origin.
installed=0
for d in "$HERE"/skills/*/; do
  name="$(basename "$d")"
  b="$(sed -n 's/^batch:[[:space:]]*//p' "$d/SKILL.md" | head -1)"
  [[ "$b" == "$BATCH" ]] || continue
  dst="$SKILL_DST/$name"
  if [[ -e "$dst" && ! -L "$dst" ]]; then
    echo "  [skip] $name — a non-package skill already exists at $dst (preserve; resolve in GAP_ANALYSIS.md)"; continue
  fi
  rm -rf "$dst"
  if [[ $MODE == link ]]; then ln -s "$d" "$dst"; else cp -r "$d" "$dst"; fi
  echo "  [add]  $name → $dst"; installed=$((installed+1))
done
mkdir -p "$PKG_DST"
for f in SPEC.md config.yaml brands hyperframes upgrades tests qa; do
  rm -rf "$PKG_DST/$f"
  if [[ $MODE == link ]]; then ln -s "$HERE/$f" "$PKG_DST/$f"; else cp -r "$HERE/$f" "$PKG_DST/$f"; fi
done
echo "Batch $BATCH: $installed skill(s) added. Package refs at $PKG_DST. Nothing existing was modified."
[[ "$BATCH" == "3" ]] && echo "Batch 3 also needs the Librarian patch appended by hand: upgrades/librarian-llm-wiki.md (never replace the existing file)."
echo "Next: ./scripts/smoke-test.sh, then run batches/batch-$BATCH-*.md and hand the result to Claude QA."
