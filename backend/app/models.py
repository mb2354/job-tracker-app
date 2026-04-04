from sqlalchemy import Column, Date, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from .database import Base


class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(255), nullable=False)
    role_title = Column(String(255), nullable=False)
    status = Column(String(100), nullable=False, default="applied")
    location = Column(String(255), nullable=True)
    salary = Column(String(100), nullable=True)
    job_link = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    date_applied = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())