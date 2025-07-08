from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

@app.get("/strategies")
def get_strategies():
    with open("strategy_memory/strategy_lineage.json") as f:
        return JSONResponse(json.load(f))

@app.get("/agents")
def get_agents():
    with open("agents/agent_registry.json") as f:
        return JSONResponse(json.load(f))

@app.get("/capital")
def get_capital_allocations():
    path = "memory/scaled_allocations/" + sorted(os.listdir("memory/scaled_allocations"))[-1]
    with open(path) as f:
        return JSONResponse(json.load(f))

@app.get("/orders")
def get_order_log():
    path = "memory/order_logs/" + sorted(os.listdir("memory/order_logs"))[-1]
    with open(path) as f:
        return JSONResponse(json.load(f))
