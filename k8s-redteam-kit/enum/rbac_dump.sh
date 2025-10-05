#!/usr/bin/env bash
set -euo pipefail
OUT=${1:-rbac_dump}
mkdir -p "$OUT"
kubectl get sa -A -o json > "$OUT/sa.json"
kubectl get role -A -o json > "$OUT/role.json"
kubectl get rolebinding -A -o json > "$OUT/rolebinding.json"
kubectl get clusterrole -o json > "$OUT/clusterrole.json"
kubectl get clusterrolebinding -o json > "$OUT/clusterrolebinding.json"
echo "[+] RBAC JSON dumped to $OUT/"
