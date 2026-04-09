from fastapi import FastAPI

from .database import Base, engine
from .routers.applications import router as applications_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(applications_router)


@app.get("/")
def read_root():
    return {"message": "Job Tracker API is running"}