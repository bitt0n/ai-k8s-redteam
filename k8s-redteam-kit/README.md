# Kubernetes Red Team Kit

**Bad Pods** to validate admission control, **enum scripts** to understand your position, and **RBAC dumpers**.

> Use only in *authorized* clusters. Many examples will fail if controls are correctly configured - that's the point.

## Quickstart
```bash
# Try to create a privileged pod (should be blocked by PSP/OPA/Kyverno/PSA)
kubectl apply -f bad-pods/privileged.yaml
kubectl apply -f bad-pods/hostpath.yaml
kubectl apply -f bad-pods/hostnetwork.yaml

# Quick enumeration
bash enum/quick_enum.sh
bash enum/rbac_dump.sh
```
