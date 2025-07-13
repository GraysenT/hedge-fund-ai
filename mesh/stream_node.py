from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
mesh_signals: List[dict] = []

class SignalMessage(BaseModel):
    market: str
    signal: str
    strategy: str
    source_node: str

@app.post("/mesh/signal")
def receive_signal(msg: SignalMessage):
    mesh_signals.append(msg.dict())
    return {"status": "received"}

@app.get("/mesh/signals")
def get_signals():
    return mesh_signals[-50:]