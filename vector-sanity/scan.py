#!/usr/bin/env python3
import os, sys, argparse, yaml, csv, json
import regex as cregex
from rich import print

def iter_texts(path):
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for f in files:
                p = os.path.join(root, f)
                if f.endswith((".txt", ".md")):
                    with open(p, "r", errors="ignore") as fh:
                        yield p, fh.read()
                elif f.endswith(".jsonl"):
                    with open(p, "r", errors="ignore") as fh:
                        for i, line in enumerate(fh, 1):
                            try:
                                obj = json.loads(line)
                                txt = obj.get("text") or ""
                                yield f"{p}:{i}", txt
                            except Exception:
                                continue
    else:
        with open(path, "r", errors="ignore") as fh:
            yield path, fh.read()

def load_patterns(pfile):
    with open(pfile, "r") as f:
        data = yaml.safe_load(f)
    pats = []
    for p in data.get("patterns", []):
        pats.append((p["name"], cregex.compile(p["regex"])))
    return pats

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="File or directory of corpus (.txt, .md, .jsonl)")
    ap.add_argument("--patterns", default="patterns.yaml")
    ap.add_argument("--out", default="report.csv")
    args = ap.parse_args()

    pats = load_patterns(args.patterns)
    findings = []
    for src, text in iter_texts(args.input):
        for name, rx in pats:
            for m in rx.finditer(text):
                span = m.group(0)
                excerpt = text[max(0,m.start()-40): m.end()+40].replace("\n"," ")
                findings.append((src, name, span[:120], excerpt[:200]))

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["source","pattern","match","excerpt"])
        w.writerows(findings)

    print(f"[green]Wrote {len(findings)} findings to {args.out}[/]")

if __name__ == "__main__":
    main()
