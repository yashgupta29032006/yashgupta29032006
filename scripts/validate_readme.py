#!/usr/bin/env python3
"""
validate_readme.py
Repository Link & Asset Validator for Yash Gupta's GitHub Profile Repository.

Performs deterministic local and remote link validation:
1. Local relative markdown links [text](path) and <a href="path">
2. Local image references <img src="path"> and ![alt](path)
3. Strict case-sensitive path existence verification on disk
4. Mandatory case study coverage check (Rudra, Sentinel AI, MediBridge AI, EchoVault)
5. Optional remote URL status checks (HTTP HEAD/GET)
"""

import os
import re
import sys
import urllib.request
import urllib.error

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
README_PATH = os.path.join(REPO_ROOT, "README.md")

REQUIRED_CASE_STUDIES = [
    "project-showcase/projects/rudra.md",
    "project-showcase/projects/sentinel-ai.md",
    "project-showcase/projects/medibridge-ai.md",
    "project-showcase/projects/echovault.md",
]

def check_case_sensitive_path(base_dir, relative_path):
    """
    Verifies that a relative path exists with exact case matching,
    even on case-insensitive filesystems like macOS APFS.
    """
    clean_rel = relative_path.split("#")[0].split("?")[0]
    parts = os.path.normpath(clean_rel).split(os.sep)
    current = base_dir

    for part in parts:
        if part in (".", ""):
            continue
        try:
            entries = os.listdir(current)
        except OSError:
            return False, f"Directory not found: {current}"
        
        if part not in entries:
            # Check if it exists with different case
            lower_matches = [e for e in entries if e.lower() == part.lower()]
            if lower_matches:
                return False, f"Case mismatch: '{part}' vs disk entry '{lower_matches[0]}'"
            return False, f"File or directory '{part}' not found in '{current}'"
        
        current = os.path.join(current, part)

    return True, current

def extract_links_and_images(content):
    """
    Extracts markdown links, image links, HTML hrefs, and HTML img srcs.
    """
    links = []
    
    # Markdown links: [text](target)
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content):
        links.append(("md_link", match.group(1), match.group(2).strip()))
        
    # Markdown images: ![alt](target)
    for match in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', content):
        links.append(("md_img", match.group(1), match.group(2).strip()))
        
    # HTML <a href="...">
    for match in re.finditer(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', content, re.IGNORECASE | re.DOTALL):
        links.append(("html_link", match.group(2).strip(), match.group(1).strip()))
        
    # HTML <img src="...">
    for match in re.finditer(r'<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*>', content, re.IGNORECASE):
        links.append(("html_img", "", match.group(1).strip()))
        
    return links

def validate_external_url(url):
    """
    Verifies that an external URL responds with 200/300 status code.
    """
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) LinkValidator/1.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=8) as response:
            return True, response.status
    except urllib.error.HTTPError as e:
        # Some servers block HEAD or custom user-agents with 403 or 999 (LinkedIn)
        if e.code in (403, 999):
            return True, f"HTTP {e.code} (Anti-scraping protection; domain reachable)"
        return False, f"HTTP {e.code}: {e.reason}"
    except Exception as e:
        return False, str(e)

def main():
    check_remote = "--check-remote" in sys.argv
    print("=" * 70)
    print("🔍 Yash Gupta GitHub Profile — Link & Architecture Validator")
    print(f"📁 Repository Root: {REPO_ROOT}")
    print(f"📄 README Path:     {README_PATH}")
    print("=" * 70)

    if not os.path.exists(README_PATH):
        print(f"❌ Error: README file not found at {README_PATH}")
        sys.exit(1)

    with open(README_PATH, "r", encoding="utf-8") as f:
        readme_content = f.read()

    extracted = extract_links_and_images(readme_content)
    print(f"✅ Found {len(extracted)} total links and image references in README.md\n")

    local_references = []
    external_references = []

    for kind, text, target in extracted:
        if target.startswith(("http://", "https://", "mailto:")):
            external_references.append((kind, text, target))
        else:
            local_references.append((kind, text, target))

    # 1. Validate Local References
    print(f"--- 1. Validating Local References ({len(local_references)} entries) ---")
    local_errors = 0
    checked_local_targets = set()

    for kind, text, target in local_references:
        clean_target = target.split("#")[0].split("?")[0]
        if not clean_target:
            continue
        checked_local_targets.add(clean_target)
        ok, detail = check_case_sensitive_path(REPO_ROOT, clean_target)
        if ok:
            print(f"  [PASS] ({kind:9}) {clean_target}")
        else:
            print(f"  [FAIL] ({kind:9}) {clean_target} -> {detail}")
            local_errors += 1

    # 2. Check Mandatory Case Studies Coverage
    print(f"\n--- 2. Checking Mandatory Case Studies Coverage ({len(REQUIRED_CASE_STUDIES)} required) ---")
    missing_case_studies = 0
    for req_cs in REQUIRED_CASE_STUDIES:
        if req_cs in checked_local_targets:
            ok, detail = check_case_sensitive_path(REPO_ROOT, req_cs)
            if ok:
                size = os.path.getsize(detail)
                print(f"  [PASS] {req_cs} (Exists, exact case, {size} bytes)")
            else:
                print(f"  [FAIL] {req_cs} -> {detail}")
                missing_case_studies += 1
        else:
            print(f"  [FAIL] Mandatory case study '{req_cs}' is NOT referenced in README.md")
            missing_case_studies += 1

    # 3. Remote URLs Check
    print(f"\n--- 3. External References ({len(external_references)} entries) ---")
    if check_remote:
        print("Validating live HTTP endpoints...")
        remote_errors = 0
        for kind, text, target in external_references:
            if target.startswith("mailto:"):
                continue
            ok, status = validate_external_url(target)
            if ok:
                print(f"  [PASS] {target[:50]:<50} -> {status}")
            else:
                print(f"  [WARN] {target[:50]:<50} -> {status}")
                remote_errors += 1
    else:
        print("  ℹ️  Remote check skipped by default. Run with --check-remote to verify HTTP endpoints.")

    # 4. Final Verdict
    print("\n" + "=" * 70)
    total_failures = local_errors + missing_case_studies
    if total_failures == 0:
        print("🎉 ALL LOCAL VALIDATION CHECKS PASSED!")
        print("   All internal files, relative paths, case sensitivity, and case studies are 100% verified.")
        print("=" * 70)
        sys.exit(0)
    else:
        print(f"❌ VALIDATION FAILED WITH {total_failures} ERRORS.")
        print("=" * 70)
        sys.exit(1)

if __name__ == "__main__":
    main()
