from pydantic.v1 import BaseModel
from sqlalchemy.orm import Session
from app.api.models import JobProfileModel
import uuid


class JobProfileCreate(BaseModel):
    description: str


def create_job_profile(db: Session, job_profile: JobProfileCreate):
    db_job_profile = JobProfileModel(id=str(uuid.uuid4()), **job_profile.dict())
    db.add(db_job_profile)
    db.commit()
    db.refresh(db_job_profile)
    return db_job_profile


def get_job_profile(db: Session, job_id: str):
    return db.query(JobProfileModel).filter(id=job_id).first()
