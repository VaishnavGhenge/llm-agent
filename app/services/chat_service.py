from typing import cast, Type

from langchain_core.messages import AIMessage
from langchain_openai import ChatOpenAI
from pydantic.v1 import BaseModel
from sqlalchemy.orm import Session

from app.api.models import ResumeModel
from app.core.config import settings
from app.services import job_service, resume_service


class ChatMessageCreate(BaseModel):
    content: str


def get_matching_resumes(db: Session, job_description: str) -> list[Type[ResumeModel]]:
    # Implement matching logic
    return resume_service.get_all_resumes(db)


def create_context(job_description: str, resumes) -> str:
    context = f"Job Description: {job_description}\n\nRelevant Resumes:\n"
    for resume in resumes:
        context += f"Name: {resume.name}\nExperience: {resume.experience}\nEducation: {resume.education}\nSkills: {resume.skills}\n\n"
    return context


def process_chat_message(db: Session, job_id: str, message: str) -> dict[str, str]:
    job_profile = job_service.get_job_profile(db, job_id)
    if not job_profile:
        return {"error": "Job profile not found"}

    matching_resumes: list[Type[ResumeModel]] = get_matching_resumes(
        db, job_profile.description
    )
    context: str = create_context(job_profile.description, matching_resumes)

    llm = ChatOpenAI(temperature=0, openai_api_key=settings.OPENAI_API_KEY)

    prompt = [
        ("system", "You are an AI assistant helping with job candidate selection."),
        ("human", f"{context}\n\nUser Query: {message}"),
    ]

    response: AIMessage = cast(AIMessage, llm.invoke(prompt))

    return {"text": response.content}
