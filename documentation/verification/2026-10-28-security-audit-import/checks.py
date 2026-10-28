"""Static checks for the imported security-audit skill: relative links resolve, no em-dashes, and the mirrored promotion block is identical. Usage: python3 -I checks.py REPOSITORY"""
import os
import re
import sys

root = os.path.join(sys.argv[1], "skills/upkeep/security-audit")
references = os.path.join(root, "references")
files = [os.path.join(root, "SKILL.md")] + [os.path.join(references, name) for name in sorted(os.listdir(references))]
failures = 0
for path in files:
    text = open(path).read()
    for target in re.findall(r"\]\(([^)#\s]+)", text):
        if not target.startswith("http") and not os.path.exists(os.path.join(os.path.dirname(path), target)):
            print("BROKEN LINK", os.path.relpath(path, root), "->", target)
            failures += 1
    if "—" in text:
        print("EM-DASH", os.path.relpath(path, root), text.count("—"))
        failures += 1


def promotion_blocks(name):
    text = open(os.path.join(references, name)).read()
    return [block for block in re.findall(r"```[a-z]*\n(.*?)```", text, re.S) if block.startswith("Artifact promotion procedure")]


hunting = promotion_blocks("hunting.md")
validation = promotion_blocks("validation-and-reporting.md")
if len(hunting) != 1 or len(validation) != 1 or hunting[0] != validation[0]:
    print("PROMOTION BLOCK MISMATCH")
    failures += 1
print("links, em-dashes, promotion block:", "FAIL" if failures else "PASS")
sys.exit(1 if failures else 0)
