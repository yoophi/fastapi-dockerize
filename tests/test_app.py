from fastapi.testclient import TestClient

from sample_app import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello, world"}
