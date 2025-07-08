from fastapi import FastAPI, UploadFile, Form
import os

app = FastAPI()
USER_DATA = "saas/user_data"

@app.post("/submit_strategy/")
async def submit_strategy(username: str = Form(...), file: UploadFile = None):
    path = f"{USER_DATA}/{username}"
    os.makedirs(path, exist_ok=True)
    code = await file.read()
    with open(f"{path}/{file.filename}", "wb") as f:
        f.write(code)
    return {"status": "success", "user": username, "file": file.filename}
