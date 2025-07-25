# Helmet Violation Detection API 🚨🪖

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-green.svg)](https://fastapi.tiangolo.com/)
[![Dockerized](https://img.shields.io/badge/Dockerized-Yes-blue)](https://www.docker.com/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-ff69b4)](https://docs.ultralytics.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A production-ready computer vision API to detect helmet violations and read number plates using YOLOv8, EasyOCR, and Norfair tracking. Built with FastAPI and Docker for seamless integration and deployment.

---

## 🔍 Features

- 🚀 Real-time helmet violation detection (with/without helmet)
- 🔢 OCR-based number plate extraction
- 🎯 Object tracking using Norfair
- 📁 API endpoints to upload video and get annotated output
- 🐳 Fully dockerized for local or server deployment
- 🧪 Built-in testing via Swagger UI (`/docs`)

---

## 📦 Tech Stack

| Module       | Technology                |
|--------------|---------------------------|
| Model        | YOLOv8 (Ultralytics)      |
| OCR          | EasyOCR                   |
| Tracking     | Norfair                   |
| API Server   | FastAPI                   |
| Deployment   | Docker                    |
| Language     | Python 3.10               |

---

## 🚀 Getting Started

### 🐳 Docker (Recommended)

```bash
git clone https://github.com/Ajinkya-001/helmet-violation-detector.git
cd helmet-violation-detector
docker build -t helmet-api .
docker run -p 8000:8000 helmet-api
```

Open in browser: http://localhost:8000/docs



API Endpoints

Upload a video file and get the output annotated video.

```bash
curl -X 'POST' \
  'http://localhost:8000/upload/' \
  -F 'file=@/path/to/your/video.mp4'
```
Response:

Returns path to the saved annotated video.


PROJECT STRUCTURE 

<img width="733" height="347" alt="image" src="https://github.com/user-attachments/assets/79053b11-21f7-4b03-b0d9-07509799574f" />

Future Work

Live webcam/RTSP stream support

Deployment on edge devices (Jetson, Raspberry Pi)

User dashboard with alert system

Integration with traffic enforcement systems

Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Author 
Ajinkya Patil

B.Tech AI & Robotics @ DSU

GitHub: Ajinkya-001








