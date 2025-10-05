# AI × Kubernetes Red Teaming — Monorepo

A practical toolkit for authorized testing at the intersection of **AI/LLM security** and **Kubernetes offensive testing**.

## Contents
- `site/` — Documentation (Jekyll) for usage, design notes, and change logs.
- `ai-pentest-harness/` — YAML-driven test harness for prompt injection, RAG leakage, and guardrail validation.
- `vector-sanity/` — Pre-index scanners to detect secrets/PII in RAG corpora.
- `rag-attack-sim/` — Canary token generator and adversarial document builders for RAG pipelines.
- `k8s-redteam-kit/` — Bad-pods and enumeration scripts to validate cluster hardening.
- `k8s-rbac-graph/` — RBAC visualizer (Graphviz DOT) with heuristics for risky bindings.

> **Legal/Ethical**: Use only with explicit authorization (labs or engagements). You are responsible for complying with laws and rules of engagement.

## Getting Started
1. Clone this repository.
2. See each tool’s `README` for quickstart commands.

## Why this repository
This monorepo consolidates small, practical tools and repeatable checks to speed up assessments of LLM/RAG stacks and Kubernetes environments. The focus is reproducibility and minimalism.
