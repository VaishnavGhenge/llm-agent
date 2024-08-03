import uuid

from langchain_openai import ChatOpenAI
from pydantic.v1 import BaseModel, Field
from sqlalchemy.orm import Session
from typing import cast, Type

from app.api.models import ResumeModel
from app.core.config import settings


class Resume(BaseModel):
    name: str = Field(description="Candidate's name mentioned")
    experience_years: float = Field(
        description="Total years of experience of candidate across all job profiles (note: be confident about)"
    )
    skills: list[str] = Field(description="Skills of candidate across all job profiles")
    education: list[str] = Field(
        description="Educational titles of candidate holding or achieved"
    )
    summary: str = Field(description="Summary of candidates profile with pros and cons of candidate")


def parse_resume(text: str) -> Resume:
    llm = ChatOpenAI(temperature=0, openai_api_key=settings.OPENAI_API_KEY)

    prompt = [
        (
            "system",
            "You are a resume text parser which extracts given structured fields from the resume text",
        ),
        ("human", text),
    ]

    structured_llm = llm.with_structured_output(Resume)
    parsed_resume: Resume = cast(Resume, structured_llm.invoke(prompt))

    return parsed_resume


def create_resume(db: Session, text: str, filename: str) -> ResumeModel:
    parsed_resume: Resume = parse_resume(text)
    resume = ResumeModel(
        id=str(uuid.uuid4()),
        original_text=text,
        filename=filename,
        **parsed_resume.dict(),
    )
    db.add(resume)
    db.commit()
    db.refresh(resume)
    return resume


def get_all_resumes(db: Session) -> list[Type[ResumeModel]]:
    return db.query(ResumeModel).all()
