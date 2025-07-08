from fastapi import Request, HTTPException

VALID_KEYS = {
    "clientA": "abc123",
    "clientB": "def456"
}

async def api_key_auth(request: Request):
    key = request.headers.get("X-API-Key")
    if not key or key not in VALID_KEYS.values():
        raise HTTPException(status_code=403, detail="Unauthorized")
    