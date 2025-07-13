from fastapi import APIRouter, UploadFile
import os

router = APIRouter()

@router.post("/upload-strategy")
async def upload_strategy(file: UploadFile):
    content = await file.read()
    filename = f"plugins/{file.filename}"
    with open(filename, "wb") as f:
        f.write(content)
    return {"status": "uploaded", "filename": filename}