# RAG Attack Simulator

Generate **canary tokens** and adversarial documents to test RAG pipelines for leakage and unsafe retrieval.

## Usage
```bash
cd rag-attack-sim
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python generate_canaries.py --n 10 --prefix RAGCANARY --out ./canaries.txt
```
