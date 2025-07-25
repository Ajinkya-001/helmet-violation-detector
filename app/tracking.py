# app/tracker.py

from ultralytics import YOLO
import cv2
import os
import supervision as sv
from typing import List
import numpy as np

# Load YOLOv8 model with tracking
model = YOLO("best.pt")  # Replace with helmet-trained model path
model.fuse()

# Supervision Annotator
annotator = sv.BoxAnnotator(thickness=2, text_thickness=1, text_scale=0.5)

# app/tracking.py
from sort import Sort

tracker = Sort()  # init once


def track_helmets(video_path: str, output_path: str = "static/outputs/tracked.mp4"):
    # Setup video IO
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Tracker
    tracker = sv.ByteTrack()  # Or sv.DeepSort() / sv.StrongSort()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]
        detections = sv.Detections.from_ultralytics(results)
        detections = tracker.update_with_detections(detections)

        # Annotate and write frame
        labels = [f"ID {tracker_id}" for tracker_id in detections.tracker_id]
        annotated_frame = annotator.annotate(scene=frame.copy(), detections=detections, labels=labels)
        out.write(annotated_frame)

    cap.release()
    out.release()
    return output_path
