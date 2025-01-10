from mylib.logistics import distance_between_two_points, time_between_two_points
import pytest
from fastapi.testclient import TestClient
from main import app
import pytest


def test_distance_between_two_points():
    assert distance_between_two_points("Lima", "Arequipa") == 765.3868858019406


# make a test for travel time_between_two_points
def test_time_between_two_points():
    assert time_between_two_points("Lima", "Arequipa") == 9.567336072524258


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


# build a test for distance_between_two_points endpoint
def test_distance_endpoint(client):
    response = client.post(
        "/distance", json={"city1": {"name": "Lima"}, "city2": {"name": "Arequipa"}}
    )
    assert response.status_code == 200
    assert response.json() == {"distance": 765.3868858019406}


# build a test for time_between_two_points endpoint
def test_time_endpoint(client):
    response = client.post(
        "/time", json={"city1": {"name": "Lima"}, "city2": {"name": "Arequipa"}}
    )
    assert response.status_code == 200
    assert response.json() == {"time": 9.567336072524258}


# make test to test fastapi main.py
def test_response(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Functions"}
