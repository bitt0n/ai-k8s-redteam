#!/usr/bin/env python3
import os, argparse, secrets
from rich import print

def gen_token(prefix="RAGCANARY", n=8):
    alphabet = "abcdef0123456789"
    return f"{prefix}-{''.join(secrets.choice(alphabet) for _ in range(n))}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10)
    ap.add_argument("--prefix", default="RAGCANARY")
    ap.add_argument("--out", default="canaries.txt")
    args = ap.parse_args()

    toks = [gen_token(args.prefix, 8) for _ in range(args.n)]
    with open(args.out, "w") as f:
        for t in toks:
            f.write(t + "\n")
    print(f"[green]Wrote {len(toks)} canaries to {args.out}[/]")

if __name__ == "__main__":
    main()
