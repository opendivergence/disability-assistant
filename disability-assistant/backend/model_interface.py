import requests

def run_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "phi3", "prompt": prompt, "stream": False}
    )
    return response.json().get("response", "Error: No response")
