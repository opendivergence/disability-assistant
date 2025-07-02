# Disability Advocacy Assistant (Backend)

This is the backend engine for the Workplace Disability Advocacy Assistant. It uses a local LLM (Phi-3 via Ollama) and RAG-ready architecture for privacy-safe legal guidance.

To run:
1. Install requirements: `pip install -r requirements.txt`
2. Run with: `uvicorn main:app --reload`
3. POST to `/chat` with role, state, and question
