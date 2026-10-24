"""Drift check for the cost example (plugin backlog story 49).

    python -I _tools/check_cost_copy.py [--source PATH] [--readme PATH] [--docs PATH] [--index PATH]

Reads the fenced ```cost-figures block of the plugin repository's docs/cost-example.md (the source of the
figures) and asserts that the three copies carry the same values: the documentation FAQ's cost answer
(docs.md, the <details id="cost"> element), the home page's "Your own AI bill" item (index.html) and the plugin's
readme.txt FAQ entry. Prints NO PROBLEMS and exits 0, or one line per difference and exits 1.

Defaults assume the two clones side by side: ../post-quality-manager/ holds the plugin repository.
Standard library only; Jekyll does not publish _tools/.
"""
import argparse
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
SITE = Path(__file__).resolve().parents[1]
PLUGIN = SITE.parent / "post-quality-manager"

ap = argparse.ArgumentParser()
ap.add_argument("--source", default=PLUGIN / "docs" / "cost-example.md")
ap.add_argument("--readme", default=PLUGIN / "post-quality-manager" / "readme.txt")
ap.add_argument("--docs", default=SITE / "docs.md")
ap.add_argument("--index", default=SITE / "index.html")
args = ap.parse_args()

problems = []


def read(p):
    p = Path(p)
    if not p.is_file():
        raise SystemExit(f"PROBLEM: {p} not found")
    return p.read_text(encoding="utf-8")


source = read(args.source)
m = re.search(r"```cost-figures\n(.*?)\n```", source, re.S)
if not m:
    raise SystemExit(f"PROBLEM: no ```cost-figures block in {args.source}")
figures = {}
for line in m.group(1).splitlines():
    k, _, v = line.partition(":")
    figures[k.strip()] = v.strip()
NEEDED = ("model", "measured", "price_input", "price_output", "short", "average", "long",
          "month_20_low", "month_20_high", "month_80_low", "month_80_high")
missing = [k for k in NEEDED if k not in figures]
if missing:
    raise SystemExit(f"PROBLEM: cost-figures block lacks {missing}")

# the region of each copy that must carry the figures
docs = read(args.docs)
dm = re.search(r'<details class="faq" id="cost">(.*?)</details>', docs, re.S)
if not dm:
    raise SystemExit("PROBLEM: docs.md has no <details class=\"faq\" id=\"cost\">")
docs_faq = dm.group(1)

readme = read(args.readme)
rm = re.search(r"= What does it cost me in AI calls\? =\n(.*?)(?:\n= |\n== )", readme + "\n== ", re.S)
if not rm:
    raise SystemExit("PROBLEM: readme.txt has no FAQ entry 'What does it cost me in AI calls?'")
readme_faq = rm.group(1)

index = read(args.index)
im = re.search(r"<h3>Your own AI bill</h3>\s*<p>(.*?)</p>", index, re.S)
if not im:
    raise SystemExit("PROBLEM: index.html has no 'Your own AI bill' item")
index_item = im.group(1)


def want(copy_name, text, label, pattern):
    if not re.search(pattern, text):
        problems.append(f"{copy_name}: {label} ({pattern}) not found")


def money(v):
    return r"\$" + re.escape(v) + r"(?!\d)"


FULL = {"model": re.escape(figures["model"]), "measured": re.escape(figures["measured"]),
        "price_input": money(figures["price_input"]), "price_output": money(figures["price_output"]),
        "short": money(figures["short"]), "average": money(figures["average"]), "long": money(figures["long"]),
        "month_20_low": money(figures["month_20_low"]), "month_20_high": money(figures["month_20_high"]),
        "month_80_low": money(figures["month_80_low"]), "month_80_high": money(figures["month_80_high"])}
for name, text in (("docs.md #cost", docs_faq), ("readme.txt FAQ", readme_faq)):
    for label, pattern in FULL.items():
        want(name, text, label, pattern)
    if "coming" in text.lower():
        problems.append(f"{name}: says 'coming'")
# the home page item carries the per-review range only
for label in ("short", "long"):
    want("index.html Your own AI bill", index_item, label, FULL[label])

# every dollar figure in a copy must be one of the source's (a stale figure left behind is drift too)
allowed = {figures[k] for k in NEEDED if k not in ("model", "measured")}
for name, text in (("docs.md #cost", docs_faq), ("readme.txt FAQ", readme_faq), ("index.html Your own AI bill", index_item)):
    for v in re.findall(r"\$(\d+(?:\.\d+)?)", text):
        if v not in allowed:
            problems.append(f"{name}: ${v} is not in the source's cost-figures block")

# the two full copies say the same thing: their first sentences are word for word the source's one paragraph
para = re.search(r"## In one paragraph\n\n(.*?)\n\n", source, re.S)
if para:
    sentence = para.group(1).split(". ")[0] + "."
    for name, text in (("docs.md #cost", docs_faq), ("readme.txt FAQ", readme_faq)):
        if sentence not in text:
            problems.append(f"{name}: the source's opening sentence is not in it: {sentence!r}")

if problems:
    print("\n".join("PROBLEM: " + p for p in problems))
    sys.exit(1)
print("NO PROBLEMS")
