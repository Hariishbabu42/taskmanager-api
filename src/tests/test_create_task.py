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
    "title": "Fastapi Project",
    "description": "Project based on fastapi",
    "completed": False
    }

def test_create_user(test_data):
    """Test creating a new user."""
    response = client.post("/tasks/create_task/", json=test_data)  
    assert response.status_code == 200
    assert response.json()["title"] == test_data["title"]


