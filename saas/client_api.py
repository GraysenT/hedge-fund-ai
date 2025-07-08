from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
import os
import json
from saas.auth_middleware import api_key_auth

app = FastAPI(title="Hedge Fund AI - Client API", version="1.0")

# Load latest file from directory
def load_latest_json(folder: str) -> dict:
    try:
        files = sorted(os.listdir(folder))
        if not files:
            raise FileNotFoundError("No files found in folder.")
        path = os.path.join(folder, files[-1])
        with open(path) as f:
            return json.load(f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading data: {e}")

@app.get("/")
def root():
    return {"status": "online", "message": "Hedge Fund AI Client API"}

@app.get("/client/{client_id}/portfolio")
async def get_client_portfolio(client_id: str, _: str = Depends(api_key_auth)):
    data = load_latest_json("memory/client_allocations")
    return JSONResponse(content=data.get(client_id, {}))

@app.get("/client/{client_id}/signals")
async def get_signals(client_id: str, _: str = Depends(api_key_auth)):
    return JSONResponse(content=load_latest_json("memory/signal_history"))

@app.get("/client/{client_id}/performance")
async def get_performance(client_id: str, _: str = Depends(api_key_auth)):
    return JSONResponse(content=load_latest_json("memory/performance"))

@app.get("/client/{client_id}/capital")
async def get_capital_allocation(client_id: str, _: str = Depends(api_key_auth)):
    return JSONResponse(content=load_latest_json("memory/scaled_allocations"))

@app.get("/client/{client_id}/orders")
async def get_order_log(client_id: str, _: str = Depends(api_key_auth)):
    return JSONResponse(content=load_latest_json("memory/order_logs"))