#!/usr/bin/env bash
# Reports which Republic dependencies are reachable on this machine. Never fails on a
# missing external tool — a missing tool blocks the department that needs it, nothing else.
set -uo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
CONTENT_DROP="${CONTENT_DROP:-$HOME/CONTENT_DROP}"

echo "== Republic v1 smoke test =="
python3 "$HERE/scripts/validate.py" || exit 1

ok()   { printf "  [ok]      %-22s %s\n" "$1" "$2"; }
miss() { printf "  [missing] %-22s %s\n" "$1" "$2"; }
have() { command -v "$1" >/dev/null 2>&1; }

echo "-- Hermes"
[[ -d "$HERMES_HOME" ]] && ok "hermes home" "$HERMES_HOME" || miss "hermes home" "$HERMES_HOME (set HERMES_HOME)"
have hermes && ok "hermes cli" "$(command -v hermes)" || miss "hermes cli" "not on PATH"
[[ -d "$HERMES_HOME/skills/republic" ]] && ok "republic skills" "$(ls "$HERMES_HOME/skills/republic" 2>/dev/null | wc -l | tr -d ' ') installed" || miss "republic skills" "run scripts/install.sh"
[[ -d "$CONTENT_DROP" ]] && ok "CONTENT_DROP" "$CONTENT_DROP" || miss "CONTENT_DROP" "$CONTENT_DROP (set CONTENT_DROP)"

echo "-- Departments → external tools (SPEC §2)"
check() { # name, department, candidates...
  local name="$1" dept="$2"; shift 2
  for c in "$@"; do
    if have "$c" || [[ -e "$c" ]]; then ok "$name" "$dept — $c"; return; fi
  done
  miss "$name" "$dept blocked until installed"
}
check "Video Vision"   "04_PRODUCTION"       video-vision videovision "$HOME/video-vision"
check "OpenMontage"    "04_PRODUCTION"       openmontage "$HOME/openmontage"
check "HyperFrames"    "04_PRODUCTION"       hyperframes "$HOME/hyperframes"
check "Last 30 Days"   "01_RESEARCH"         last30days last-30-days "$HOME/last30days"
check "Claude SEO"     "02_SEARCH"           claude-seo "$HOME/claude-seo"
check "Claude Ads"     "06_PAID"             claude-ads "$HOME/claude-ads"
check "AnyDoc"         "knowledge"           anydoc "$HOME/anydoc"
check "QMD"            "knowledge"           qmd "$HOME/qmd"
check "Obsidian vault" "knowledge"           "${OBSIDIAN_VAULT:-$HOME/vault}"
echo "-- Workers (model-routing; tiers only)"
if [[ -n "${OLLAMA_HOST:-}" ]]; then ok "T0 local endpoint" "$OLLAMA_HOST (set)"; else miss "T0 local endpoint" "OLLAMA_HOST unset — see model-routing/references"; fi
[[ -n "${GHL_API_KEY:-}${GHL_LOCATION_ID:-}" ]] && ok "GHL credentials" "present in env" || miss "GHL credentials" "05_DISTRIBUTION_CRM blocked until configured"
echo "== done. Missing rows block only their department. =="
