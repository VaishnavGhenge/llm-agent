from fastapi import APIRouter, UploadFile, File, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services import pdf_service, job_service, chat_service
from app.api.models import JobProfile, ChatMessage

router = APIRouter()


@router.post("/upload_resume/")
async def upload_resume(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    content = await file.read()
    background_tasks.add_task(pdf_service.process_pdf, db, content, file.filename)
    return {"message": "Resume uploaded and processing started"}


@router.post("/create_job_profile/")
async def create_job_profile(job_profile: JobProfile, db: Session = Depends(get_db)):
    return job_service.create_job_profile(db, job_profile)


@router.post("/chat/{job_id}")
async def chat(job_id: str, message: ChatMessage, db: Session = Depends(get_db)):
    return chat_service.process_chat_message(db, job_id, message.content)
