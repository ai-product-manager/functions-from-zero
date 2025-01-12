import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from mylib.logistics import distance_between_two_points, time_between_two_points

from mylib.wiki import get_wiki_keywords

app = FastAPI()


class CityRequest(BaseModel):
    name: str


@app.get("/")
async def root():
    """Home page with GET method"""
    return {"message": "Hello Functions"}


@app.post("/distance")
async def distance(city1: CityRequest, city2: CityRequest):
    """Calculate the distance between two cities

    Returns back the distance in kilometers
    """

    dist = distance_between_two_points(city1.name, city2.name)
    return {"distance": dist}


@app.post("/time")
async def time(city1: CityRequest, city2: CityRequest):
    """Calculate the time between two cities

    Returns back the time in hours
    """

    dist = time_between_two_points(city1.name, city2.name)
    return {"time": dist}


@app.post("/keywords")
async def keywords(page: CityRequest):
    """Get keywords from a wikipedia page

    Returns back a list of keywords
    """
    return {"list": get_wiki_keywords(page.name)}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
