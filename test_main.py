from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_missing_api_key(monkeypatch):
    monkeypatch.setenv("API_KEY", "test-key")

    response = client.get("/tasks")
    assert response.status_code == 401


def test_valid_api_key(monkeypatch):
    monkeypatch.setenv("API_KEY", "test-key")

    response = client.get(
        "/tasks",
        headers={"X-API-Key": "test-key"}
    )

    assert response.status_code == 200


def test_invalid_input(monkeypatch):
    monkeypatch.setenv("API_KEY", "test-key")

    response = client.post(
        "/tasks",
        headers={"X-API-Key": "test-key"},
        json={"title": ""}
    )

    assert response.status_code == 422


def test_create_task(monkeypatch):
    monkeypatch.setenv("API_KEY", "test-key")

    response = client.post(
        "/tasks",
        headers={"X-API-Key": "test-key"},
        json={"title": "Learn Python"}
    )

    assert response.status_code == 201
