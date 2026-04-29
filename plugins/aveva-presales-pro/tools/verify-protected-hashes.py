#!/usr/bin/env python3
"""
Compare current SHA-256 of Category 3 protected files against the recorded
baseline in .protected-files-baseline.json. Prints per-file status, exits 0
on full match, 1 on any drift (and 2 on missing baseline / I/O error).

This is a READ-ONLY auditor. It does NOT modify the baseline. To regenerate
the baseline (only legitimate during an authorized release), run the build
script kept outside the distribution.

Usage:
    python3 tools/verify-protected-hashes.py [--root .] [--quiet]
"""
import argparse
import hashlib
import json
import os
import sys

BASELINE_FILENAME = ".protected-files-baseline.json"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--root", default=".", help="Plugin root (default: cwd)")
    parser.add_argument("--quiet", action="store_true", help="Suppress per-file OK lines")
    args = parser.parse_args()

    baseline_path = os.path.join(args.root, BASELINE_FILENAME)
    if not os.path.exists(baseline_path):
        print(f"ERROR: baseline file not found at {baseline_path}", file=sys.stderr)
        return 2

    try:
        with open(baseline_path) as f:
            baseline = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"ERROR: could not read baseline: {e}", file=sys.stderr)
        return 2

    expected = baseline.get("files", {})
    if not expected:
        print(f"ERROR: baseline has no files entry", file=sys.stderr)
        return 2

    print(f"Verifying {len(expected)} protected files against baseline v{baseline.get('version', '?')}")
    print(f"Watermark: {baseline.get('watermark', '?')}")
    print()

    ok = 0
    drift = []
    missing = []
    for rel, exp_hash in sorted(expected.items()):
        p = os.path.join(args.root, rel)
        if not os.path.exists(p):
            missing.append(rel)
            print(f"  MISSING  {rel}")
            continue
        actual = sha256_of(p)
        if actual == exp_hash:
            ok += 1
            if not args.quiet:
                print(f"  OK       {rel}")
        else:
            drift.append((rel, exp_hash, actual))
            print(f"  DRIFT    {rel}")
            print(f"    expected {exp_hash}")
            print(f"    actual   {actual}")

    print()
    print(f"Summary: {ok} OK, {len(drift)} drifted, {len(missing)} missing")

    if drift or missing:
        print()
        print("Action required:")
        if drift:
            print(f"  - {len(drift)} protected file(s) have been modified since the baseline.")
            print("    Per MODIFICATION-POLICY.md, modifying Category 3 files voids the")
            print("    commercial license. If the change was authorized (e.g. a release),")
            print("    rebuild the baseline through the official release process.")
        if missing:
            print(f"  - {len(missing)} protected file(s) are missing from the install.")
            print("    The plugin distribution may be incomplete — re-install from a")
            print("    trusted source.")
        return 1

    print("All protected files match the baseline. Integrity check PASSED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
