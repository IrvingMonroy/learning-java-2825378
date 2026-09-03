#!/usr/bin/env python3
"""Republic v1 package validator.

Checks that the package is internally consistent with SPEC.md before install.
Exit 0 = PASS, exit 1 = FAIL with every finding listed. No network, no external tools.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
BRANDS = os.path.join(ROOT, "brands")
HF = os.path.join(ROOT, "hyperframes", "templates")
PIPELINE = os.path.join(ROOT, "kanban", "pipeline.yaml")

REQUIRED_SKILLS = {
    "republic-triage": "republic",
    "republic-research": "01_RESEARCH",
    "republic-search": "02_SEARCH",
    "republic-writing-system": "03_CONTENT",
    "republic-platform-experts": "03_CONTENT",
    "republic-repurposing": "03_CONTENT",
    "republic-video-intake": "04_PRODUCTION",
    "republic-editing": "04_PRODUCTION",
    "republic-hyperframes": "04_PRODUCTION",
    "republic-production-acceptance": "04_PRODUCTION",
    "republic-distribution": "05_DISTRIBUTION_CRM",
    "republic-paid": "06_PAID",
    "republic-librarian": "knowledge",
    "republic-anydoc": "knowledge",
    "republic-qmd": "knowledge",
    "republic-learning-loop": "knowledge",
    "republic-kanban": "control",
    "republic-qa": "control",
}
DEPARTMENTS = {"01_RESEARCH", "02_SEARCH", "03_CONTENT", "04_PRODUCTION", "05_DISTRIBUTION_CRM", "06_PAID"}
BRAND_FILES = ["brand.md", "voice.md", "audience.md", "offers.md", "proof.md", "objections.md", "prohibited-claims.md", "approved-examples"]
PM_TEMPLATES = ["educational-reel", "review-highlight", "pain-explainer", "faq", "promotion", "myth-vs-fact"]
PLATFORMS = ["instagram", "tiktok", "youtube", "facebook", "linkedin", "gbp"]
COLUMNS = ["TRIAGE", "RESEARCH", "STRATEGY", "PLATFORM_BRIEF", "PRODUCTION", "QA", "RACHEL_APPROVAL", "SCHEDULED", "PUBLISHED", "MEASURED", "DONE"]
# FREEZE.md exclusions must not appear as installed skills.
EXCLUDED_TERMS = ["soup", "posthog", "herdr", "omarchy", "fincept", "vibe", "deepseek", "killer", "hook-agent", "caption-agent", "cta-agent"]
# SPEC §23: skills reference worker tiers, never model IDs.
MODEL_ID_RE = re.compile(r"\b(claude-[a-z]+-\d|gpt-\d|gpt-[45]o|qwen\d(\.\d)?[:\-]|gemini-\d|o[13]-mini|deepseek-[a-z0-9]+)\b", re.I)

findings = []


def fail(msg):
    findings.append(msg)


def frontmatter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
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


def check_skills():
    if not os.path.isdir(SKILLS):
        fail("skills/ directory missing")
        return
    present = {d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d))}
    for name in REQUIRED_SKILLS:
        if name not in present:
            fail(f"required skill missing: {name}")
    names_seen = set()
    depts_seen = set()
    for d in sorted(present):
        skill_md = os.path.join(SKILLS, d, "SKILL.md")
        if not os.path.isfile(skill_md):
            fail(f"{d}: SKILL.md missing")
            continue
        fm, text = frontmatter(skill_md)
        if fm is None:
            fail(f"{d}: SKILL.md has no YAML front matter")
            continue
        for key in ("name", "description", "version", "department"):
            if not fm.get(key):
                fail(f"{d}: front matter missing '{key}'")
        if fm.get("name") != d:
            fail(f"{d}: front matter name '{fm.get('name')}' != directory name")
        if fm.get("name") in names_seen:
            fail(f"{d}: duplicate skill name")
        names_seen.add(fm.get("name"))
        if d in REQUIRED_SKILLS and fm.get("department") != REQUIRED_SKILLS[d]:
            fail(f"{d}: department '{fm.get('department')}' != expected '{REQUIRED_SKILLS[d]}'")
        depts_seen.add(fm.get("department"))
        if len(fm.get("description", "")) < 80:
            fail(f"{d}: description too short to trigger reliably (<80 chars)")
        if "SPEC §" not in text:
            fail(f"{d}: no SPEC § citation (traceability)")
        if "## Boundaries" not in text and "## Hard limits" not in text:
            fail(f"{d}: no Boundaries/Hard limits section")
        for m in MODEL_ID_RE.finditer(text):
            fail(f"{d}: model ID '{m.group(0)}' in skill text (SPEC §23: worker tiers only)")
        low = d.lower()
        for term in EXCLUDED_TERMS:
            if term in low:
                fail(f"{d}: skill name contains excluded term '{term}' (FREEZE.md)")
    for dept in DEPARTMENTS:
        if dept not in depts_seen:
            fail(f"department {dept} has no skill")
    # platform expert references
    for p in PLATFORMS:
        ref = os.path.join(SKILLS, "republic-platform-experts", "references", f"{p}.md")
        if not os.path.isfile(ref):
            fail(f"platform reference missing: {p}.md")
    for ref in ["voice-dna", "blank-page", "angles", "brand-writing", "direct-response", "writing-qa"]:
        if not os.path.isfile(os.path.join(SKILLS, "republic-writing-system", "references", f"{ref}.md")):
            fail(f"writing-system reference missing: {ref}.md")


def check_pipeline():
    if not os.path.isfile(PIPELINE):
        fail("kanban/pipeline.yaml missing")
        return
    with open(PIPELINE, encoding="utf-8") as f:
        text = f.read()
    ids = re.findall(r"^\s*-\s*id:\s*([A-Z_]+)\s*$", text, re.M)
    if ids != COLUMNS:
        fail(f"pipeline columns {ids} != SPEC §21 {COLUMNS}")
    # gate: only rachel advances out of RACHEL_APPROVAL
    m = re.search(r"RACHEL_APPROVAL:\s*\n\s*may_advance:\s*\[([^\]]*)\]", text)
    if not m or m.group(1).strip() != "rachel":
        fail("gates.RACHEL_APPROVAL.may_advance must be exactly [rachel]")
    if not re.search(r"autonomous_allowed:\s*false", text):
        fail("gates.paid_spend.autonomous_allowed must be false (SPEC §16)")
    for key in ("absolute_usd", "relative_pct", "min_sample", "measurement_window_days"):
        if not re.search(rf"^\s*{key}:\s*\d+", text, re.M):
            fail(f"pipeline threshold '{key}' missing or non-numeric")
    # every path uses defined columns and ends at DONE
    for name, body in re.findall(r"^\s*(content|search|paid|knowledge|ops):\s*\[([^\]]*)\]", text, re.M):
        cols = [c.strip() for c in body.split(",")]
        for c in cols:
            if c not in COLUMNS:
                fail(f"path {name} uses undefined column {c}")
        if cols[-1] != "DONE":
            fail(f"path {name} does not end at DONE")
        if name in ("content", "search", "paid", "ops") and "RACHEL_APPROVAL" not in cols:
            fail(f"path {name} bypasses RACHEL_APPROVAL")
    if re.search(r"model\s*:\s*[a-z]", text, re.I):
        fail("pipeline.yaml names a model; use worker tiers (SPEC §23)")


def check_brands():
    if not os.path.isdir(BRANDS):
        fail("brands/ missing")
        return
    for b in sorted(os.listdir(BRANDS)):
        bd = os.path.join(BRANDS, b)
        if not os.path.isdir(bd):
            continue
        for f in BRAND_FILES:
            if not os.path.exists(os.path.join(bd, f)):
                fail(f"brand {b}: missing {f} (SPEC §4 Stage A schema)")
        voice = os.path.join(bd, "voice.md")
        if os.path.isfile(voice):
            fm, text = frontmatter(voice)
            if "TODO-SOURCE" not in text and (fm is None or fm.get("sources", "[]") in ("[]", "")):
                fail(f"brand {b}: voice.md has no TODO-SOURCE marker and no sources — voice must trace to human material")


def check_hyperframes():
    pm = os.path.join(HF, "physically-meta")
    for t in PM_TEMPLATES:
        p = os.path.join(pm, f"{t}.md")
        if not os.path.isfile(p):
            fail(f"hyperframes template missing: physically-meta/{t}.md (SPEC §9)")
            continue
        fm, _ = frontmatter(p)
        if fm is None or fm.get("template") != t:
            fail(f"hyperframes template {t}: front matter 'template' != filename")


def check_docs():
    for f in ["SPEC.md", "FREEZE.md", "DEFINITION_OF_DONE.md", "README.md", "qa/QA_CONTRACT.md", "qa/QA_REPORT_TEMPLATE.md", "kanban/card-template.md", "tests/acceptance/editing-acceptance.md", "tests/acceptance/end-to-end-run.md"]:
        if not os.path.isfile(os.path.join(ROOT, f)):
            fail(f"document missing: {f}")
    spec = os.path.join(ROOT, "SPEC.md")
    if os.path.isfile(spec):
        with open(spec, encoding="utf-8") as fh:
            s = fh.read()
        if "FROZEN" not in s:
            fail("SPEC.md not marked FROZEN")
        for n in range(1, 29):
            if not re.search(rf"^## {n}\. ", s, re.M):
                fail(f"SPEC.md missing section {n}")
    readme = os.path.join(ROOT, "README.md")
    if os.path.isfile(readme):
        with open(readme, encoding="utf-8") as fh:
            r = fh.read()
        for name in REQUIRED_SKILLS:
            if f"`{name}`" not in r:
                fail(f"README skills table missing {name}")
    contract = os.path.join(ROOT, "qa", "QA_CONTRACT.md")
    if os.path.isfile(contract):
        with open(contract, encoding="utf-8") as fh:
            c = fh.read()
        for cls in ("BLOCKER", "DEFECT", "IMPROVEMENT", "PREFERENCE"):
            if cls not in c:
                fail(f"QA contract missing classification {cls}")


def main():
    check_docs()
    check_skills()
    check_pipeline()
    check_brands()
    check_hyperframes()
    if findings:
        print(f"FAIL — {len(findings)} finding(s):")
        for f in findings:
            print(f"  - {f}")
        sys.exit(1)
    n = len([d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d))])
    print(f"PASS — {n} skills, {len(COLUMNS)} columns, brands and templates consistent with SPEC.md")


if __name__ == "__main__":
    main()
