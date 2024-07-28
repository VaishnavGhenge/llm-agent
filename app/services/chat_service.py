from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from sqlalchemy.orm import Session
from app.core.config import settings
from app.services import job_service, resume_service


def get_matching_resumes(db: Session, job_description: str):
    # Implement matching logic
    return resume_service.get_all_resumes(db)


def create_context(job_description: str, resumes):
    context = f"Job Description: {job_description}\n\nRelevant Resumes:\n"
    for resume in resumes:
        context += f"Name: {resume.name}\nExperience: {resume.experience}\nEducation: {resume.education}\nSkills: {resume.skills}\n\n"
    return context


def process_chat_message(db: Session, job_id: str, message: str):
    job_profile = job_service.get_job_profile(db, job_id)
    if not job_profile:
        return {"error": "Job profile not found"}

    matching_resumes = get_matching_resumes(db, job_profile.description)
    context = create_context(job_profile.description, matching_resumes)

    chat = ChatOpenAI(temperature=0, openai_api_key=settings.OPENAI_API_KEY)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an AI assistant helping with job candidate selection."),
            ("human", "{context}\n\nUser Query: {message}"),
        ]
    )

    chain = LLMChain(llm=chat, prompt=prompt)

    response = chain.run(context=context, message=message)

    # Parse the response to extract candidates
    candidates = (
        response.split("Candidates:")[-1].strip().split(", ")
        if "Candidates:" in response
        else []
    )

    return {"text": response, "candidates": candidates}
