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
def task_id()-> int:
    return int(106)

def test_get_task(task_id):
    response = client.get(f"/tasks/{task_id}") 
    assert response.status_code == 200
    assert response.json()["id"] == task_id


