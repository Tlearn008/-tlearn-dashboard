from fastapi import FastAPI, Request
from pydantic import BaseModel
import subprocess

app = FastAPI()

class RunPipelineRequest(BaseModel):
    subject: str
    video_type: str  # 'short' or 'long'

class UploadRequest(BaseModel):
    video_path: str

@app.post("/run_pipeline")
async def run_pipeline(req: RunPipelineRequest):
    subprocess.Popen(["python3", "run_pipeline.py", req.subject, req.video_type])
    return {"status": "Pipeline started", "subject": req.subject, "type": req.video_type}

@app.post("/upload_to_youtube")
async def upload_video(req: UploadRequest):
    return {"status": f"Upload triggered for {req.video_path}"}

@app.post("/sync_dashboard")
async def sync_dashboard():
    return {"status": "Dashboard sync triggered"}
