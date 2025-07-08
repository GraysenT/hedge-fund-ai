from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

from api.security.auth import authorize_request
from compliance.audit_trail_logger import log_audit_event

app = FastAPI()
origins = ["*"]  # change to trusted domains for production

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/report")
def get_latest_investor_report(request: Request):
    user = authorize_request(request, "viewer")
    path = "reports/investor_report.json"
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Report not found.")
    with open(path, "r") as f:
        data = json.load(f)
    log_audit_event("api_access", {"endpoint": "/api/report", "user": user["role"]})
    return data

@app.get("/api/alpha_matrix")
def get_alpha_data(request: Request):
    user = authorize_request(request, "analyst")
    path = "memory/alpha_attribution.json"
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Alpha matrix not found.")
    with open(path, "r") as f:
        data = json.load(f)
    log_audit_event("api_access", {"endpoint": "/api/alpha_matrix", "user": user["role"]})
    return data

@app.get("/api/strategies")
def get_active_strategies(request: Request):
    user = authorize_request(request, "viewer")
    path = "memory/optimized_allocations.json"
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Allocation data missing.")
    with open(path, "r") as f:
        data = json.load(f)
    log_audit_event("api_access", {"endpoint": "/api/strategies", "user": user["role"]})
    return data

@app.get("/api/fund_weights")
def get_fund_weights(request: Request):
    user = authorize_request(request, "viewer")
    path = "memory/fund_weights.json"
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Fund weight data missing.")
    with open(path, "r") as f:
        data = json.load(f)
    log_audit_event("api_access", {"endpoint": "/api/fund_weights", "user": user["role"]})
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)