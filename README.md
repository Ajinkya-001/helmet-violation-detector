# Helmet Violation Detection API

This project is an end-to-end helmet violation detection system built using YOLOv8 for object detection, Norfair for object tracking, and EasyOCR for license plate recognition. It provides a FastAPI interface for uploading videos and returning annotated output.



## Features

- YOLOv8-based detection of:
- 
  - Riders with helmets
  - 
  - Riders without helmets
    
- Object tracking using Norfair for consistent identity assignment
  
- License plate recognition using EasyOCR
  
- FastAPI backend with Swagger documentation for testing
  
- Dockerized for seamless deployment
  
- Annotated output video generation



## Project Structure


<img width="383" height="601" alt="image" src="https://github.com/user-attachments/assets/dd6dfbbf-b3f3-4d6e-95fa-170f0506f35e" />



---

## Setup Instructions

### Prerequisites

- Python 3.8 or later
- `ffmpeg` installed on system
- CUDA-enabled GPU (recommended for real-time inference)

### Local Installation

```bash
git clone https://github.com/Ajinkya-001/helmet-violation-detector.git
cd helmet-violation-api
```
```bash
python3 -m venv venv
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```
Running the Application
```bash
uvicorn app.main:app --reload
```
Navigate to http://127.0.0.1:8000/docs to access the Swagger UI and test the /upload/ endpoint. Output videos are saved in the outputs/ directory.

Docker Deployment

```bash

docker build -t helmet-api .
docker run -p 8000:8000 -v $(pwd)/outputs:/app/outputs helmet-api
```

Access via: http://localhost:8000/docs


Model Information

Trained using YOLOv8

Two class labels:

  0: with_helmet
   
  1: without_helmet

Stack 

  YOLOv8 (Ultralytics)

  Norfair (Object Tracking)

  EasyOCR (License Plate Recognition)

  FastAPI (Web Framework)

  Docker (Containerization)

Roadmap

 Export CSV logs of violations
 

 SQLite or NoSQL storage for incidents
 

 Alerting system (email/SMS integration)
 

 Web dashboard for monitoring violations
 

 CI/CD integration (GitHub Actions)

License

 This project is licensed under the MIT License. For academic and research use only. Please ensure compliance with local    laws and privacy regulations when deploying in public environments.

 Author
 Ajinkya Patil
 Github:Ajinkya-001
 









