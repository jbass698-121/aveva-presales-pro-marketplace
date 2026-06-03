#!/usr/bin/env python3
"""
One-command release build for aveva-presales-pro.

Run from the marketplace repo root:  python3 build.py [--version X.Y.Z]

Steps (in order):
  1. Bump version in plugins/aveva-presales-pro/.claude-plugin/plugin.json
     AND .claude-plugin/marketplace.json (the two places that must agree).
  2. Recompute .protected-files-baseline.json (SHA-256 of the 26 Category-3 files).
  3. Regenerate artifacts/battlecards-snapshot.json from the competitor MD frontmatter+body.
  4. Regenerate artifacts/content-health-snapshot.json from the content file tree.
  5. Inline both snapshots into their HTML artifacts (between the build markers) so the
     dashboards work as self-contained Cowork artifacts with NO sibling-file fetch.
  6. Verify the hash baseline matches and print a summary.

This replaces the old manual multi-step release (bump-in-two-places + ad-hoc snapshot
regeneration) that caused version/snapshot/doc drift.
"""
import argparse, datetime, hashlib, json, os, re, sys

DEFAULT_VERSION = "0.3.2"
PLUGIN = "plugins/aveva-presales-pro"
FULL_THRESHOLD = 1500  # bytes; >= is "full", below is "stub" (reproduces historical classification)
WATERMARK = "appro-ca96e5c3-e535-40b4-a502-9e85523f608e"

PROTECTED = [
    ".claude-plugin/plugin.json",
    "skills/orchestrator/SKILL.md", "skills/account-memory/SKILL.md",
    "skills/win-loss-loop/SKILL.md", "skills/content-health/SKILL.md",
    "skills/onboarding/SKILL.md", "skills/portfolio-narrative/SKILL.md",
    "skills/strategic-account/SKILL.md", "skills/deck-generator/SKILL.md",
    "skills/enablement-podcast/SKILL.md", "skills/quick-reference/SKILL.md",
    "skills/pipeline-health/SKILL.md",
    "agents/researcher.md", "agents/analyst.md", "agents/writer.md",
    "agents/verifier.md", "agents/formatter.md",
    "pipelines/opportunity-briefing.yaml", "pipelines/strategic-account-brief.yaml",
    "pipelines/industry-playbook.yaml", "pipelines/executive-deck.yaml",
    "pipelines/enablement-podcast.yaml", "pipelines/quick-reference.yaml",
    "content/public-sources.yaml", "LICENSE.md", "MODIFICATION-POLICY.md",
]

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml --break-system-packages")


def jdefault(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    return str(o)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def split_frontmatter(text):
    """Return (frontmatter_dict, body_str)."""
    if text.startswith("---"):
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
        if m:
            try:
                fm = yaml.safe_load(m.group(1)) or {}
            except yaml.YAMLError:
                fm = {}
            return fm, m.group(2)
    return {}, text


def parse_sections(body):
    """Parse '## Heading' sections -> {heading: body_text}."""
    sections, cur, buf = {}, None, []
    for line in body.splitlines():
        m = re.match(r"^##\s+(.*\S)\s*$", line)
        if m:
            if cur is not None:
                sections[cur] = "\n".join(buf).strip()
            cur, buf = m.group(1), []
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        sections[cur] = "\n".join(buf).strip()
    return sections


def bump_version(root, version):
    pj = os.path.join(root, PLUGIN, ".claude-plugin", "plugin.json")
    with open(pj) as f:
        data = json.load(f)
    data["version"] = version
    with open(pj, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    changed = ["plugin.json"]
    mp = os.path.join(root, ".claude-plugin", "marketplace.json")
    if os.path.exists(mp):
        with open(mp) as f:
            m = json.load(f)
        for p in m.get("plugins", []):
            if p.get("name") == "aveva-presales-pro":
                p["version"] = version
        with open(mp, "w") as f:
            json.dump(m, f, indent=2)
            f.write("\n")
        changed.append("marketplace.json")
    return changed


def build_baseline(root, version):
    base = os.path.join(root, PLUGIN)
    files = {}
    missing = []
    for rel in PROTECTED:
        p = os.path.join(base, rel)
        if os.path.exists(p):
            files[rel] = sha256(p)
        else:
            missing.append(rel)
    out = {"files": files, "version": version, "watermark": WATERMARK}
    with open(os.path.join(base, ".protected-files-baseline.json"), "w") as f:
        json.dump(out, f, indent=2)
        f.write("\n")
    return files, missing


def watermark_count(base):
    n = 0
    for dp, _, fns in os.walk(base):
        for fn in fns:
            if fn.endswith((".md", ".yaml")):
                try:
                    with open(os.path.join(dp, fn), encoding="utf-8", errors="ignore") as f:
                        if WATERMARK in f.read():
                            n += 1
                except OSError:
                    pass
    return n


def build_battlecards(base, version):
    cdir = os.path.join(base, "content", "competitors")
    cards = {}
    for fn in sorted(os.listdir(cdir)):
        if not fn.endswith(".md") or fn == "_template.md":
            continue
        slug = fn[:-3]
        path = os.path.join(cdir, fn)
        size = os.path.getsize(path)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        fm, body = split_frontmatter(text)
        is_stub = (str(fm.get("status", "")).lower() == "stub") or (size < FULL_THRESHOLD)
        cards[slug] = {
            "name": fm.get("competitor") or slug.replace("-", " ").title(),
            "threat_tier": fm.get("threat_tier", "unknown"),
            "verticals": fm.get("verticals_active_in", []) or [],
            "last_validated": fm.get("last_validated"),
            "audience_signals": fm.get("audience_signals", {}) or {},
            "their_AI_offering": fm.get("their_AI_offering"),
            "recent_corporate_change": fm.get("recent_corporate_change"),
            "sources": fm.get("sources", []) or [],
            "sections": {} if is_stub else parse_sections(body),
            "is_stub": is_stub,
            "path": f"content/competitors/{fn}",
        }
    snap = {"plugin_version": version, "watermark": WATERMARK, "cards": cards}
    out = os.path.join(base, "artifacts", "battlecards-snapshot.json")
    with open(out, "w") as f:
        json.dump(snap, f, indent=2, default=jdefault)
        f.write("\n")
    full = sum(1 for c in cards.values() if not c["is_stub"])
    return snap, full, len(cards) - full


def _slot(base, relglob, dated):
    """relglob: (subdir, predicate). Returns list of slot dicts."""
    subdir, pred = relglob
    d = os.path.join(base, subdir)
    items = []
    if not os.path.isdir(d):
        return items
    for fn in sorted(os.listdir(d)):
        full = os.path.join(d, fn)
        if not os.path.isfile(full) or not pred(fn):
            continue
        size = os.path.getsize(full)
        items.append({
            "path": f"{subdir}/{fn}",
            "size_bytes": size,
            "status": "full" if size >= FULL_THRESHOLD else "stub",
            "last_validated": "2026-06-03" if dated else None,
        })
    return items


def build_content_health(base, version, baseline_files):
    md = lambda fn: fn.endswith(".md") and fn != "_template.md"
    slots = {
        "industry_playbooks": _slot(base, ("content/industries", md), True),
        "competitor_battlecards": _slot(base, ("content/competitors", md), True),
        "case_studies": _slot(base, ("content/case-studies", md), True),
        "objection_scripts": _slot(base, ("content/objections", md), True),
        "product_positioning": _slot(base, ("content/products", md), True),
        "pricing_book": _slot(base, ("content/pricing", lambda fn: fn.endswith(".yaml")), False),
        "discovery": _slot(base, ("content/discovery", md), False),
        "canonical_references": _slot(
            base, ("content", lambda fn: fn in (
                "aveva-canonical.yaml", "aveva-industry-positioning.yaml",
                "aveva-regulatory-mapping.yaml", "whats-new-2026H1.md")), False),
    }
    # live baseline verification
    matches, mismatches = 0, []
    for rel, expected in baseline_files.items():
        p = os.path.join(base, rel)
        if os.path.exists(p) and sha256(p) == expected:
            matches += 1
        else:
            mismatches.append(rel)
    snap = {
        "generated_at": datetime.datetime.now().isoformat(),
        "plugin_version": version,
        "watermark": WATERMARK,
        "slots": slots,
        "baseline_status": {
            "baseline_version": version,
            "files_in_baseline": len(baseline_files),
            "matches": matches,
            "mismatches": mismatches,
        },
        "watermark_count": watermark_count(base),
    }
    out = os.path.join(base, "artifacts", "content-health-snapshot.json")
    with open(out, "w") as f:
        json.dump(snap, f, indent=2, default=jdefault)
        f.write("\n")
    return snap


def inline_snapshot(html_path, snap):
    with open(html_path, encoding="utf-8") as f:
        html = f.read()
    # escape </ to keep the JSON from breaking out of the <script> tag
    js = json.dumps(snap, default=jdefault).replace("<", "\\u003c")
    repl = "/*__SNAPSHOT_INLINE_START__*/" + js + "/*__SNAPSHOT_INLINE_END__*/"
    new, n = re.subn(
        r"/\*__SNAPSHOT_INLINE_START__\*/.*?/\*__SNAPSHOT_INLINE_END__\*/",
        lambda _m: repl, html, flags=re.S)
    if n == 0:
        raise SystemExit(f"ERROR: inline markers not found in {html_path}")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new)
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default=DEFAULT_VERSION)
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    base = os.path.join(root, PLUGIN)
    if not os.path.isdir(base):
        sys.exit(f"ERROR: {base} not found. Run from the marketplace repo root.")
    v = args.version

    print(f"== aveva-presales-pro build → v{v} ==")
    changed = bump_version(root, v)
    print(f"  1. version bumped in: {', '.join(changed)}")

    bfiles, missing = build_baseline(root, v)
    print(f"  2. hash baseline: {len(bfiles)} files" + (f"  (MISSING: {missing})" if missing else ""))

    bc_snap, full, stub = build_battlecards(base, v)
    print(f"  3. battlecards-snapshot.json: {full} full + {stub} stub = {len(bc_snap['cards'])} cards")

    ch_snap = build_content_health(base, v, bfiles)
    bs = ch_snap["baseline_status"]
    print(f"  4. content-health-snapshot.json: {sum(len(x) for x in ch_snap['slots'].values())} slots; "
          f"watermark_count={ch_snap['watermark_count']}; baseline {bs['matches']}/{bs['files_in_baseline']}")

    n1 = inline_snapshot(os.path.join(base, "artifacts", "battlecard-viewer.html"), bc_snap)
    n2 = inline_snapshot(os.path.join(base, "artifacts", "content-health-dashboard.html"), ch_snap)
    print(f"  5. inlined snapshots into artifacts (battlecard-viewer x{n1}, content-health-dashboard x{n2})")

    ok = bs["matches"] == bs["files_in_baseline"] and not bs["mismatches"] and not missing
    print(f"  6. integrity: {'PASS' if ok else 'FAIL — ' + str(bs['mismatches'] + missing)}")
    print("== done ==")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
