from fastapi import FastAPI
from pydantic import BaseModel
from control.override_manager import set_override, load_overrides

app = FastAPI()

class OverrideRequest(BaseModel):
    key: str
    value: bool

@app.get("/overrides")
def get_all_overrides():
    return load_overrides()

@app.post("/overrides")
def update_override(req: OverrideRequest):
    set_override(req.key, req.value)
    return {"status": "success", "override": {req.key: req.value}}