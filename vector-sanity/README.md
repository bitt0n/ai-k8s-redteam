# Vector Sanity — RAG Corpus Scanner

Quickly scan your RAG corpus (markdown, txt, JSONL with `text` field) for **secrets** and **PII-like indicators** before indexing.

## Usage
```bash
cd vector-sanity
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scan.py --input ./samples --out report.csv
```
- Supports folders of `.txt`, `.md`, `.jsonl` (expects objects with `text`).
- Uses configurable patterns in `patterns.yaml`.
