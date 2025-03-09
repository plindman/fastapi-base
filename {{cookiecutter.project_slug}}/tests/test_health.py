import pytest
from fastapi.testclient import TestClient
from app.main import app  # Adjust the import path as necessary

client = TestClient(app)

def test_health_check():
    response = client.get("/app/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
