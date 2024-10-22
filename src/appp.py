"""
Application
"""

from fastapi import FastAPI  

app = FastAPI()

@app.get("/status")
def health_check() -> dict:
    """Health check"""
    return {"status": "ok"}

@app.get("/print")
def print_name(name : str) -> str:
    """Print Hello name"""
    return f"Hello, {name}"



