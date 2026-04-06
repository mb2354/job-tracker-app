from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


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
    response = client.get("/applications")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)