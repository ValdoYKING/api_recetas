# tests/test_users.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "Password123"
    })
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
