# K8s RBAC Graph

Builds a **Graphviz DOT** graph of ServiceAccounts → (Role|ClusterRole) via (RoleBinding|ClusterRoleBinding), highlights suspicious wildcard verbs/resources.

## Usage
```bash
cd k8s-rbac-graph
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python rbac_graph.py --dumpdir ../k8s-redteam-kit/rbac_dump --out rbac.dot
# Then render: dot -Tpng rbac.dot -o rbac.png
```
