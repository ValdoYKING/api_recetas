# tests/test_recipes.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_recipe():
    response = client.post("/recipes/", json={
        "title": "Papata",
        "description": "Delicious potato recipe",
        "ingredients": "Potatoes, oil, salt",
        "instructions": "Fry the potatoes until golden brown."
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Papata"

def test_read_recipes():
    response = client.get("/recipes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
