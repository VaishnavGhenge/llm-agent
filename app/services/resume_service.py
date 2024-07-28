import uuid

from sqlalchemy.orm import Session
from typing import TypedDict, List, Optional

from app.api.models import Resume
from app.services.logging_service import logger


class ResumeDict(TypedDict):
    name: str
    filename: str
    experience_years: int
    original_text: str
    skills: List[str]
    education: Optional[str]
    summary: Optional[str]


def parse_resume(text: str):
    logger.info(text)


def create_resume(db: Session, text: str, filename: str):
    parsed_resume = parse_resume(text)
    # resume = Resume(id=str(uuid.uuid4()), filename=filename, **parsed_resume)
    # db.add(resume)
    # db.commit()
    # db.refresh(resume)
    # return parsed_resume


def get_all_resumes(db: Session):
    return db.query(Resume).all()
