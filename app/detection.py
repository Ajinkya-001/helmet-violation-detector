import cv2
import numpy as np
from ultralytics import YOLO
from norfair import Detection, Tracker
import easyocr

# Load YOLOv8 model (custom helmet detection model)
helmet_model = YOLO("best.pt")  # Adjust path if needed

# Load EasyOCR reader
ocr_reader = easyocr.Reader(['en'])

# Define class IDs
CLASS_WITH_HELMET = 0
CLASS_WITHOUT_HELMET = 1

# Norfair tracker setup
tracker = Tracker(
    distance_function="euclidean",
    distance_threshold=30
)


def detect_violations(frame: np.ndarray) -> np.ndarray:
    results = helmet_model.predict(source=frame, conf=0.3)[0]

    if results.boxes is None:
        return frame

    detections = []
    annotated_frame = frame.copy()

    for box in results.boxes:
        cls = int(box.cls[0].item())
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        detections.append(Detection(points=np.array([cx, cy])))

        label = "With Helmet" if cls == CLASS_WITH_HELMET else "Without Helmet"
        color = (0, 255, 0) if cls == CLASS_WITH_HELMET else (0, 0, 255)

        roi = frame[y1:y2, x1:x2]
        ocr_result = ocr_reader.readtext(roi)
        plate_text = ocr_result[0][1] if ocr_result else "N/A"

        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(annotated_frame, f"{label} | {plate_text}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    tracked_objects = tracker.update(detections)
    for obj in tracked_objects:
        x, y = map(int, obj.estimate[0])
        cv2.circle(annotated_frame, (x, y), 5, (255, 0, 0), -1)
        cv2.putText(annotated_frame, f"ID: {obj.id}", (x + 10, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    return annotated_frame

