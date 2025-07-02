from fastapi import FastAPI, Request
from pydantic import BaseModel
from prompt_logic import build_prompt
from model_interface import run_ollama

app = FastAPI()

class ChatRequest(BaseModel):
    role: str
    state: str
    question: str

@app.post("/chat")
def chat(req: ChatRequest):
    prompt = build_prompt(req.role, req.state, req.question)
    response = run_ollama(prompt)
    return {"response": response.strip()}
