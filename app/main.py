from fastapi import FastAPI, UploadFile, File
import shutil
import os
from app.detection import detect_helmet_violation

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Helmet Violation API is up 🎯"}

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)
    file_path = f"uploads/{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    output_path = detect_helmet_violation(file_path)
    return {"message": "Processing done", "video_path": output_path}
