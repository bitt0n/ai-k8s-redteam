# AI × Kubernetes Red Teaming — Monorepo

**Purpose:** A practical, legally safe starter kit for building an elite niche at the intersection of **AI/LLM pentesting** and **Kubernetes offensive security**.

> ⚠️ **Legal/Ethical**: All tools here are for **authorized testing in lab or client-approved environments** only. You are responsible for following the law and your engagement’s rules of engagement.

## Contents
- `site/` — GitHub Pages docs (Jekyll) so your profile quietly showcases research without self‑promotion.
- `ai-pentest-harness/` — Pluggable YAML-driven test harness for prompt-injection, data-leak, and RAG fuzzing.
- `vector-sanity/` — Fast scanners for secrets/PII in RAG corpora and embeddings metadata.
- `rag-attack-sim/` — Canary generators and adversarial content builders for RAG pipelines.
- `k8s-redteam-kit/` — Bad-pods, fast enumeration, and practical checks for K8s misconfig & escalation.
- `k8s-rbac-graph/` — Build a DOT graph of RBAC relationships and highlight likely privesc paths.

## Getting Started
1. Create a new GitHub repository and upload this folder (or split into separate repos later).
2. Enable **GitHub Pages** to publish from `site/` (Settings ▸ Pages ▸ Build and deployment ▸ Source: GitHub Actions or "Deploy from a branch" with `/site` as root).
3. Customize `site/index.md` and commit. Your personal site becomes your quiet living portfolio.

## Why this approach?
You don’t need YouTube or personal branding. A living, useful **body of work** is enough. This repo keeps you shipping: small tools, docs, and experiments every week.
