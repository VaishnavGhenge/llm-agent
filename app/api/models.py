from app.core.database import Base

from sqlalchemy import Column, String, Text, ARRAY, Float


class JobProfileModel(Base):
    __tablename__ = "job_profiles"

    id = Column(String, primary_key=True, index=True)
    description = Column(Text)


class ChatMessageModel(Base):
    __tablename__ = "chat_messages"

    id = Column(String, primary_key=True, index=True)
    content = Column(Text)


class ResumeModel(Base):
    __tablename__ = "resumes"

    id = Column(String, primary_key=True, index=True)
    filename = Column(String, index=True)
    name = Column(String, index=True)
    experience_years = Column(Float)
    skills = Column(ARRAY(String))
    education = Column(String, nullable=True)
    summary = Column(Text, nullable=True)
    original_text = Column(Text, nullable=True)
