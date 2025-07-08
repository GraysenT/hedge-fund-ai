from fastapi import FastAPI, WebSocket
from fastapi.responses import JSONResponse
import os
import json
import asyncio

app = FastAPI()

@app.websocket("/ws/trades")
async def trade_socket(websocket: WebSocket):
    await websocket.accept()
    last_file = ""
    while True:
        files = sorted(os.listdir("memory/order_logs"))
        latest = files[-1] if files else ""
        if latest != last_file:
            path = os.path.join("memory/order_logs", latest)
            with open(path) as f:
                data = json.load(f)
            await websocket.send_json(data)
            last_file = latest
        await asyncio.sleep(3)
