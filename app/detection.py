import cv2
import os
import numpy as np
from ultralytics import YOLO
from norfair import Detection, Tracker
import easyocr
from datetime import datetime

# Load YOLOv8 model (helmet detection)
helmet_model = YOLO("/home/ajinkya/helmet-violation-api/best.pt")  # Replace with your custom model path
# Load EasyOCR
ocr_reader = easyocr.Reader(['en'])

# Class IDs (update if your model has different mappings)
CLASS_WITH_HELMET = 0
CLASS_WITHOUT_HELMET = 1

# Setup Norfair Tracker
tracker = Tracker(
    distance_function="euclidean",
    distance_threshold=30
)

# Create output directory if not exists
os.makedirs("outputs", exist_ok=True)


def detect_helmet_violation(video_path: str) -> str:
    cap = cv2.VideoCapture(video_path)
    frame_width, frame_height = int(cap.get(3)), int(cap.get(4))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Output path
    filename = os.path.basename(video_path).split(".")[0]
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_path = f"outputs/{filename}_helmet_violation_{timestamp}.mp4"

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_writer = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run helmet detection
        results = helmet_model.track(source=frame, persist=True, stream=True)

        for result in results:
            if result.boxes is None:
                continue

            annotated_frame = frame.copy()
            detections = []

            for box in result.boxes:
                cls = int(box.cls[0].item())
                conf = float(box.conf[0].item())
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

                # Norfair tracking input
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                detections.append(Detection(points=np.array([cx, cy])))

                label = "With Helmet" if cls == CLASS_WITH_HELMET else "Without Helmet"
                color = (0, 255, 0) if cls == CLASS_WITH_HELMET else (0, 0, 255)

                # OCR: try to read number plate inside bounding box
                roi = frame[y1:y2, x1:x2]
                ocr_result = ocr_reader.readtext(roi)
                plate_text = ocr_result[0][1] if ocr_result else "N/A"

                # Annotate frame
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(annotated_frame, f"{label} | {plate_text}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

            # Norfair tracking update
            tracked_objects = tracker.update(detections)
            for obj in tracked_objects:
                x, y = map(int, obj.estimate[0])
                cv2.circle(annotated_frame, (x, y), 5, (255, 0, 0), -1)
                cv2.putText(annotated_frame, f'ID: {obj.id}', (x + 10, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

            out_writer.write(annotated_frame)

    cap.release()
    out_writer.release()
    return output_path
