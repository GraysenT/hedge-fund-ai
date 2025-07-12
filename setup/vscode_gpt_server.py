import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI, Request
import uvicorn
from editor_hooks.vscode_socket import fetch_code_from_editor, send_code_to_editor

app = FastAPI()

@app.post("/fetch_code/")
async def fetch_code(req: Request):
    data = await req.json()
    filepath = data.get("path")
    content = fetch_code_from_editor(filepath)
    return {"code": content}

@app.post("/write_code/")
async def write_code(req: Request):
    data = await req.json()
    path = data.get("path")
    content = data.get("content")
    result = send_code_to_editor(path, content)
    return {"status": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)