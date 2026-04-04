from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class JobApplicationCreate(BaseModel):
    company_name: str
    role_title: str
    status: str
    location: Optional[str] = None
    salary: Optional[str] = None
    job_link: Optional[str] = None
    notes: Optional[str] = None
    date_applied: Optional[date] = None


class JobApplicationResponse(BaseModel):
    id: int
    company_name: str
    role_title: str
    status: str
    location: Optional[str] = None
    salary: Optional[str] = None
    job_link: Optional[str] = None
    notes: Optional[str] = None
    date_applied: Optional[date] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)