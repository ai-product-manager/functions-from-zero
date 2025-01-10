import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from mylib.logistics import distance_between_two_points, time_between_two_points

app = FastAPI()


class CityRequest(BaseModel):
    city1: str
    city2: str


@app.get("/")
async def root():
    """Home page with GET method"""
    return {"message": "Hello Functions"}


@app.post("/distance")
async def distance(request: CityRequest):
    """Calculate the distance between two cities

    Returns back the distance in kilometers
    """

    dist = distance_between_two_points(request.city1, request.city2)
    return {"distance": dist}


@app.post("/time")
async def time(request: CityRequest):
    """Calculate the time between two cities

    Returns back the time in hours
    """

    dist = time_between_two_points(request.city1, request.city2)
    return {"time": dist}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
