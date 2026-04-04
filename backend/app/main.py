from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import JobApplication
from .schemas import JobApplicationCreate, JobApplicationResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Job Tracker API is running"}


@app.post("/applications", response_model=JobApplicationResponse)
def create_application(
    application: JobApplicationCreate,
    db: Session = Depends(get_db)
):
    db_application = JobApplication(**application.model_dump())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application


@app.get("/applications", response_model=List[JobApplicationResponse])
def get_applications(db: Session = Depends(get_db)):
    applications = db.query(JobApplication).all()
    return applications