#!/usr/bin/env bash
set -euo pipefail
NS=${1:-default}
echo "[*] Context: $(kubectl config current-context)"
echo "[*] WhoAmI:"
kubectl auth can-i --list || true
echo "[*] Namespaces:"
kubectl get ns
echo "[*] Pods in $NS:"
kubectl get pods -n "$NS" -o wide
echo "[*] SAs:"
kubectl get sa -A
echo "[*] RBAC (roles):"
kubectl get role -A
echo "[*] RBAC (rolebindings):"
kubectl get rolebinding -A
echo "[*] RBAC (clusterroles):"
kubectl get clusterrole | head -n 30
echo "[*] RBAC (clusterrolebindings):"
kubectl get clusterrolebinding | head -n 30
