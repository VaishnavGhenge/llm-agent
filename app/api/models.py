from pydantic import BaseModel, Field
from typing import List, Optional


class JobProfile(BaseModel):
    description: str = Field(..., min_length=10, max_length=300)


class ChatMessage(BaseModel):
    content: str = Field(..., min_length=1, max_length=500)


class Resume(BaseModel):
    id: str
    filename: str
    name: str
    experience_years: int
    skills: List[str]
    education: Optional[str] = None
    summary: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "filename": "resume.pdf",
                "name": "John Doe",
                "experience_years": 5,
                "skills": ["Python", "Django", "SQL"],
                "education": "B.Sc. in Computer Science",
                "summary": "Experienced software developer with a passion for building scalable applications.",
            }
        }
