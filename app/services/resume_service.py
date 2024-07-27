from sqlalchemy.orm import Session
from app.api.models import Resume
import uuid


def parse_resume(text: str) -> dict:
    # This is a placeholder. Implement proper resume parsing logic.
    return {
        "full_text": text,
        "name": "Extracted Name",
        "experience": "Extracted Experience",
        "education": "Extracted Education",
        "skills": "Extracted Skills",
    }


def create_resume(db: Session, text: str, filename: str):
    parsed_resume = parse_resume(text)
    resume = Resume(id=str(uuid.uuid4()), filename=filename, **parsed_resume)
    db.add(resume)
    db.commit()
    db.refresh(resume)
    return resume
