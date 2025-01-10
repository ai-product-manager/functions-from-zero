from mylib.logistics import distance_between_two_points
import pytest
from fastapi.testclient import TestClient
from main import app
import pytest


def test_distance_between_two_points():
    assert distance_between_two_points("Lima", "Arequipa") == 765.3868858019406


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


# make test to test fastapi main.py
def test_response(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Functions"}
