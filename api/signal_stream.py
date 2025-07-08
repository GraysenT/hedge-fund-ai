from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
import json
import os
import asyncio

app = FastAPI()

@app.get("/signals")
def get_signals():
    with open("memory/signal_history.json") as f:
        return JSONResponse(json.load(f))

@app.websocket("/ws/signals")
async def signal_socket(websocket: WebSocket):
    await websocket.accept()
    last_sent = ""
    while True:
        with open("memory/signal_history.json") as f:
            data = f.read()
        if data != last_sent:
            await websocket.send_text(data)
            last_sent = data
        await asyncio.sleep(2)
