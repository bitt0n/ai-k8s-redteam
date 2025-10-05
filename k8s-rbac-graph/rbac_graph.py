#!/usr/bin/env python3
import os, json, argparse
from rich import print

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def suspicious_rules(rules):
    flags = []
    for r in rules:
        verbs = r.get("verbs", [])
        res = r.get("resources", [])
        if "*" in verbs or "*" in res:
            flags.append("wildcard")
        if any(v in verbs for v in ["impersonate", "bind", "escalate"]):
            flags.append("power_verbs")
    return list(set(flags))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dumpdir", required=True, help="Directory from rbac_dump.sh")
    ap.add_argument("--out", default="rbac.dot")
    args = ap.parse_args()

    role = load_json(os.path.join(args.dumpdir, "role.json"))
    rb   = load_json(os.path.join(args.dumpdir, "rolebinding.json"))
    cr   = load_json(os.path.join(args.dumpdir, "clusterrole.json"))
    crb  = load_json(os.path.join(args.dumpdir, "clusterrolebinding.json"))
    sa   = load_json(os.path.join(args.dumpdir, "sa.json"))

    # Index roles/clusterroles
    roles = {(i["metadata"]["namespace"], i["metadata"]["name"]): i for i in role.get("items", [])}
    croles = {i["metadata"]["name"]: i for i in cr.get("items", [])}

    # Build DOT
    lines = ["digraph RBAC {", 'rankdir=LR;', 'node [shape=box, style=rounded];']
    def add_node(id_, label, color="black"):
        lines.append(f'"{id_}" [label="{label}", color="{color}"];')

    # SA nodes
    for i in sa.get("items", []):
        ns = i["metadata"]["namespace"]
        name = i["metadata"]["name"]
        add_node(f"sa:{ns}:{name}", f"SA\\n{ns}/{name}", color="blue")

    # Role nodes (within ns)
    for (ns, name), obj in roles.items():
        color = "red" if suspicious_rules(obj.get("rules", [])) else "black"
        add_node(f"role:{ns}:{name}", f"Role\\n{ns}/{name}", color=color)

    # ClusterRole nodes
    for name, obj in croles.items():
        color = "red" if suspicious_rules(obj.get("rules", [])) else "black"
        add_node(f"crole::{name}", f"ClusterRole\\n{name}", color=color)

    # Edges via RoleBinding
    for i in rb.get("items", []):
        ns = i["metadata"]["namespace"]
        roleRef = i.get("roleRef", {})
        rname = roleRef.get("name")
        rkind = roleRef.get("kind")
        # Subjects
        for s in i.get("subjects", []):
            if s.get("kind") == "ServiceAccount":
                san = s.get("name")
                sans = s.get("namespace", ns)
                if rkind == "Role":
                    lines.append(f'"sa:{sans}:{san}" -> "role:{ns}:{rname}" [label="RoleBinding"];')
                elif rkind == "ClusterRole":
                    lines.append(f'"sa:{sans}:{san}" -> "crole::{rname}" [label="RoleBinding"];')

    # Edges via ClusterRoleBinding
    for i in crb.get("items", []):
        rname = i.get("roleRef", {}).get("name")
        for s in i.get("subjects", []):
            if s.get("kind") == "ServiceAccount":
                san = s.get("name")
                sans = s.get("namespace", "default")
                lines.append(f'"sa:{sans}:{san}" -> "crole::{rname}" [label="ClusterRoleBinding"];')

    lines.append("}")
    with open(args.out, "w") as f:
        f.write("\n".join(lines))
    print(f"[green]Wrote DOT graph to {args.out}[/]")

if __name__ == "__main__":
    main()
