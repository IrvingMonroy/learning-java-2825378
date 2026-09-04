#!/usr/bin/env python3
"""Republic v1 upgrade package validator.

Checks the package is internally consistent with SPEC.md and is ADDITIVE: every skill
declares its batch and what it adds to, nothing in the package targets a preserved piece,
and nothing excluded by FREEZE.md is present. Exit 0 = PASS, 1 = FAIL.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")

# capability → (batch, required references)
REQUIRED = {
    "republic-video-vision": 1,
    "republic-openmontage": 1,
    "republic-hyperframes": 1,
    "republic-last-30-days": 2,
    "republic-writing": 2,
    "republic-anydoc": 3,
    "republic-claude-seo": 4,
    "republic-claude-ads": 4,
}
WRITING_REFS = ["voice-dna", "ideation", "angles", "brand-writing", "conversion", "voice-qa"]
PM_TEMPLATES = ["educational-reel", "review-highlight", "pain-explainer", "faq", "promotion", "myth-vs-fact"]
DOCS = ["SPEC.md", "README.md", "FREEZE.md", "DEFINITION_OF_DONE.md", "GAP_ANALYSIS.md", "config.yaml",
        "qa/QA_CONTRACT.md", "qa/QA_REPORT_TEMPLATE.md", "upgrades/librarian-llm-wiki.md",
        "brands/brand-schema.md", "tests/acceptance/editing-acceptance.md", "tests/acceptance/end-to-end-run.md",
        "batches/batch-1-production.md", "batches/batch-2-intelligence.md", "batches/batch-3-knowledge.md",
        "batches/batch-4-growth.md"]
# SPEC §1 — no skill may present itself as owning a preserved piece.
PRESERVED_NAME_TERMS = ["soul", "identity", "profile", "librarian", "kanban", "ghl", "publish", "distribution",
                        "socrates", "instagram", "qmd", "triage"]
# FREEZE.md — excluded tools and the separately-installed writing skills.
EXCLUDED_TERMS = ["soup", "posthog", "herdr", "deepseek", "archify", "omarchy", "fincept", "vibe",
                  "killer", "hook-agent", "caption-agent", "cta-agent", "72-reasons"]
MODEL_ID_RE = re.compile(r"\b(claude-[a-z]+-\d|gpt-\d|gpt-[45]o|qwen\d(\.\d)?[:\-]|gemini-\d|o[13]-mini|deepseek-[a-z0-9]+)\b", re.I)
REPLACE_OK_RE = re.compile(r"^(nothing|none)\b|acceptance", re.I)

findings = []
fail = findings.append


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, text


def check_docs():
    for f in DOCS:
        if not os.path.isfile(os.path.join(ROOT, f)):
            fail(f"document missing: {f}")
    spec = open(os.path.join(ROOT, "SPEC.md"), encoding="utf-8").read() if os.path.isfile(os.path.join(ROOT, "SPEC.md")) else ""
    if "FROZEN" not in spec:
        fail("SPEC.md not marked FROZEN")
    for h in ["## 0. Posture", "## 1. Preserved", "## 2. Demonstrated weak behavior", "## 3. Capabilities added",
              "## 4. Republic Writing", "## 5. Batches", "## 6. Production acceptance", "## 7. Claude QA",
              "## 8. Boundaries", "## 9. Excluded", "## 10. Definition of DONE"]:
        if h not in spec:
            fail(f"SPEC.md missing section '{h}'")
    if "Preserve working behavior. Add missing capability. Replace only demonstrated weak behavior." not in spec:
        fail("SPEC.md missing the conservative rule verbatim")
    cfg = open(os.path.join(ROOT, "config.yaml"), encoding="utf-8").read() if os.path.isfile(os.path.join(ROOT, "config.yaml")) else ""
    for key in ("absolute_usd", "relative_pct", "min_sample", "measurement_window_days"):
        if not re.search(rf"^\s*{key}:\s*\d+", cfg, re.M):
            fail(f"config.yaml: '{key}' missing or non-numeric")
    if not re.search(r"autonomous_allowed:\s*false", cfg):
        fail("config.yaml: paid_spend.autonomous_allowed must be false (SPEC §8)")
    if MODEL_ID_RE.search(cfg):
        fail("config.yaml names a model ID; tiers only (SPEC §8)")
    patch = os.path.join(ROOT, "upgrades", "librarian-llm-wiki.md")
    if os.path.isfile(patch):
        t = open(patch, encoding="utf-8").read()
        if "APPEND" not in t or "Do not remove" not in t:
            fail("librarian patch must state it is appended and removes nothing")
        for q in ["UPDATE", "CONTRADICT", "STRENGTHEN", "SUPERSEDE", "CHANGE a project", "CREATE a relationship", "REVEAL", "CREATE a decision"]:
            if q not in t:
                fail(f"librarian patch missing question '{q}'")
    readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read() if os.path.isfile(os.path.join(ROOT, "README.md")) else ""
    for name in REQUIRED:
        if f"`{name}`" not in readme:
            fail(f"README capabilities table missing {name}")
    contract = open(os.path.join(ROOT, "qa", "QA_CONTRACT.md"), encoding="utf-8").read() if os.path.isfile(os.path.join(ROOT, "qa", "QA_CONTRACT.md")) else ""
    for cls in ("BLOCKER", "DEFECT", "IMPROVEMENT", "PREFERENCE"):
        if cls not in contract:
            fail(f"QA contract missing {cls}")
    if "Preserved pieces" not in contract:
        fail("QA contract missing the preserved-pieces rule")
    acc = os.path.join(ROOT, "tests", "acceptance", "editing-acceptance.md")
    if os.path.isfile(acc) and "Baseline" not in open(acc, encoding="utf-8").read():
        fail("editing acceptance sheet has no Baseline column (SPEC §6)")


def check_skills():
    if not os.path.isdir(SKILLS):
        fail("skills/ missing")
        return
    present = sorted(d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d)))
    for name in REQUIRED:
        if name not in present:
            fail(f"required capability missing: {name}")
    for d in present:
        if d not in REQUIRED:
            fail(f"unexpected skill '{d}': not in SPEC §3 capability table (additive package only)")
        low = d.lower()
        for t in PRESERVED_NAME_TERMS:
            if t in low:
                fail(f"{d}: name claims a preserved piece '{t}' (SPEC §1)")
        for t in EXCLUDED_TERMS:
            if t in low:
                fail(f"{d}: name contains excluded term '{t}' (FREEZE.md)")
        p = os.path.join(SKILLS, d, "SKILL.md")
        if not os.path.isfile(p):
            fail(f"{d}: SKILL.md missing")
            continue
        fm, text = frontmatter(p)
        if fm is None:
            fail(f"{d}: no front matter")
            continue
        for key in ("name", "description", "version", "batch", "adds_to", "replaces", "preserves"):
            if not fm.get(key):
                fail(f"{d}: front matter missing '{key}'")
        if fm.get("name") != d:
            fail(f"{d}: name '{fm.get('name')}' != directory")
        if d in REQUIRED and str(fm.get("batch")) != str(REQUIRED[d]):
            fail(f"{d}: batch {fm.get('batch')} != SPEC §3 batch {REQUIRED[d]}")
        rep = fm.get("replaces", "")
        if rep and not REPLACE_OK_RE.search(rep):
            fail(f"{d}: replaces '{rep}' — only 'nothing' or an acceptance-gated replacement is allowed")
        if "acceptance" in rep.lower() and d != "republic-openmontage":
            fail(f"{d}: only the editing candidate may replace behavior (SPEC §2)")
        if len(fm.get("description", "")) < 80:
            fail(f"{d}: description too short to trigger reliably")
        if "SPEC §" not in text:
            fail(f"{d}: no SPEC § citation")
        if "## Boundaries" not in text:
            fail(f"{d}: no Boundaries section")
        for m in MODEL_ID_RE.finditer(text):
            fail(f"{d}: model ID '{m.group(0)}' (tiers only)")
        if re.search(r"never publishes|never publish|no site edits|never edits campaigns|never files|never touches the existing intake", text, re.I) is None:
            fail(f"{d}: Boundaries do not state what it never does to existing steps")
    for r in WRITING_REFS:
        if not os.path.isfile(os.path.join(SKILLS, "republic-writing", "references", f"{r}.md")):
            fail(f"republic-writing reference missing: {r}.md")
    w = os.path.join(SKILLS, "republic-writing", "SKILL.md")
    if os.path.isfile(w):
        t = open(w, encoding="utf-8").read()
        for src in ("Ghostwriter Killer", "Blank Page Killer", "72 Reasons to Buy", "Direct Response Copywriter", "AI Slop Killer"):
            if src not in t:
                fail(f"republic-writing does not absorb '{src}' (SPEC §4)")
        if "would this person actually say this" not in t.lower():
            fail("republic-writing missing the permanent voice-QA rule")


def check_templates():
    base = os.path.join(ROOT, "hyperframes", "templates", "physically-meta")
    for t in PM_TEMPLATES:
        p = os.path.join(base, f"{t}.md")
        if not os.path.isfile(p):
            fail(f"hyperframes template missing: {t}.md")
            continue
        fm, _ = frontmatter(p)
        if fm is None or fm.get("template") != t:
            fail(f"hyperframes template {t}: front matter 'template' != filename")


def check_nothing_rebuilt():
    """The package must not carry structures that would duplicate the existing Republic."""
    for path in ["kanban", "brands/_template", "brands/physically-meta"]:
        if os.path.exists(os.path.join(ROOT, path)):
            fail(f"'{path}' present — would duplicate an existing Republic structure (SPEC §1)")


def main():
    check_docs()
    check_skills()
    check_templates()
    check_nothing_rebuilt()
    if findings:
        print(f"FAIL — {len(findings)} finding(s):")
        for f in findings:
            print(f"  - {f}")
        sys.exit(1)
    print(f"PASS — {len(REQUIRED)} additive capabilities across 4 batches, 1 Librarian patch, "
          f"{len(PM_TEMPLATES)} templates; no preserved piece targeted; no excluded tool present")


if __name__ == "__main__":
    main()
