# Tlearn API Backend (FastAPI)

This is the backend server to connect the Tlearn GPT with your automated video pipeline.

## Features
- Run video generation pipeline for NEET subjects
- Upload videos to YouTube
- Sync dashboard metadata

## How to Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoints
- POST /run_pipeline
- POST /upload_to_youtube
- POST /sync_dashboard
