from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import numpy as np
import cv2
from io import BytesIO
from app.detection import detect_violations
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Helmet Violation Detector API 🚨"}

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    result_img = detect_violations(img)

    # Encode the image back to bytes
    _, encoded_img = cv2.imencode(".jpg", result_img)
    return StreamingResponse(BytesIO(encoded_img.tobytes()), media_type="image/jpeg")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
