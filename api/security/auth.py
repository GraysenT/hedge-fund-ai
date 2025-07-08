import os
from fastapi import Request, HTTPException
import json

KEY_DB = "secrets/api_keys.json"

def load_keys():
    if not os.path.exists(KEY_DB):
        return {}
    with open(KEY_DB) as f:
        return json.load(f)

def authorize_request(request: Request, required_role="viewer"):
    keys = load_keys()
    token = request.headers.get("x-api-key")
    if not token or token not in keys:
        raise HTTPException(status_code=401, detail="Unauthorized")

    role = keys[token]["role"]
    allowed_roles = ["admin", "analyst", "viewer"]
    if allowed_roles.index(role) < allowed_roles.index(required_role):
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    return keys[token]