from fastapi import APIRouter, UploadFile, File
from app.detection import detect_helmet_violation
import shutil
import uuid
import os

router = APIRouter()

@router.post("/detect-helmet/")
async def detect_helmet(file: UploadFile = File(...)):
    temp_filename = f"temp_{uuid.uuid4().hex}.jpg"
    
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = detect_helmet_violation(temp_filename)

    os.remove(temp_filename)

    return result
