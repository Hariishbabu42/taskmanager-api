import sys
import os
import pytest
from fastapi.testclient import TestClient


current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from src.tasks_main import app  

client = TestClient(app)

@pytest.fixture
def test_data():
    return {
    "title": "abc",
    "description": "def",
    "completed": True
    }

def test_create_user(test_data):
    """Test creating a new user."""
    response = client.post("/tasks/create_task/", json=test_data)  # Replace "/users/" with your actual endpoint
    assert response.status_code == 200
    assert response.json()["title"] == test_data["title"]


