from sqlalchemy.orm import Session
from app.api.models import JobProfile
import uuid


def create_job_profile(db: Session, job_profile: JobProfile):
    db_job_profile = JobProfile(id=str(uuid.uuid4()), **job_profile.dict())
    db.add(db_job_profile)
    db.commit()
    db.refresh(db_job_profile)
    return db_job_profile


def get_job_profile(db: Session, job_id: str):
    return db.query(JobProfile).filter(JobProfile.id == job_id).first()
