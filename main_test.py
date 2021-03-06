import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_404():
    response = client.get("/welcome")
    assert response.status_code == 200
    response = client.get("/")
    assert response.status_code == 200