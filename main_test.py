from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main_true():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_read_main_fail():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}