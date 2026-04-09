import os

from fastapi.testclient import TestClient

from backend.app.database import Base, get_db
from backend.app.main import app
from tests.test_database import engine, override_get_db

Base.metadata.create_all(bind=engine)

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def setup_function():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def teardown_module():
    engine.dispose()
    if os.path.exists("test.db"):
        try:
            os.remove("test.db")
        except PermissionError:
            pass


def test_create_application():
    response = client.post(
        "/applications",
        json={
            "company_name": "Microsoft",
            "role_title": "Backend Developer",
            "status": "applied",
            "location": "London",
            "salary": "£40000",
            "job_link": "https://example.com/job",
            "notes": "Test application",
            "date_applied": "2026-04-05"
        },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["company_name"] == "Microsoft"
    assert data["role_title"] == "Backend Developer"
    assert data["status"] == "applied"


def test_get_applications():
    client.post(
        "/applications",
        json={
            "company_name": "Meta",
            "role_title": "Software Engineer",
            "status": "interview",
            "location": "London",
            "salary": "£50000",
            "job_link": "https://example.com/meta-job",
            "notes": "Test listing",
            "date_applied": "2026-04-05"
        },
    )

    response = client.get("/applications")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["company_name"] == "Meta"

    