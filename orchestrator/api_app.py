from fastapi import FastAPI
from orchestrator import api  # this should already contain your router logic

app = FastAPI(title="Hedge Fund AI Orchestrator")
app.include_router(api.router, prefix="/orchestrator")