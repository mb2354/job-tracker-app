from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ApplicationStatus(str, Enum):
    applied = "applied"
    interview = "interview"
    rejected = "rejected"
    offer = "offer"


class JobApplicationBase(BaseModel):
    company_name: str
    role_title: str
    status: ApplicationStatus
    location: Optional[str] = None
    salary: Optional[str] = None
    job_link: Optional[str] = None
    notes: Optional[str] = None
    date_applied: Optional[date] = None


class JobApplicationCreate(JobApplicationBase):
    pass


class JobApplicationUpdate(JobApplicationBase):
    pass


class JobApplicationResponse(JobApplicationBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)