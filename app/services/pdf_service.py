import PyPDF2
import io
from sqlalchemy.orm import Session
from app.services import resume_service


def extract_text_from_pdf(content: bytes) -> str:
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(content))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def process_pdf(db: Session, content: bytes, filename: str):
    text = extract_text_from_pdf(content)
    resume_service.create_resume(db, text, filename)
