from fastapi import FastAPI
import json
import hashlib
import os
from datetime import datetime

app = FastAPI()

@app.get("/alpha/audit")
def get_alpha_snapshot():
    perf = json.load(open("memory/performance/" + sorted(os.listdir("memory/performance"))[-1]))
    snapshot = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "pnl": {k: round(v["pnl"], 2) for k, v in perf.items()}
    }
    snapshot["checksum"] = hashlib.sha256(json.dumps(snapshot).encode()).hexdigest()
    return snapshot
    