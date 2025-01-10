"""
This module deals with logistics and calculates distances between two points
and the time it takes to travel between them.

"""

from geopy import distance

# build a list of 10 cities in Peru and their coordinates
cities = {
    "Lima": (-12.046374, -77.042793),
    "Arequipa": (-16.409047, -71.537451),
    "Cusco": (-13.531950, -71.967463),
    "Trujillo": (-8.109052, -79.021533),
    "Chiclayo": (-6.771428, -79.840883),
    "Iquitos": (-3.749122, -73.253830),
    "Piura": (-5.194493, -80.632820),
    "Chimbote": (-9.085305, -78.578251),
    "Huancayo": (-12.065144, -75.204589),
    "Tacna": (-18.011814, -70.253859),
}

# build a function to calculate the distance between two cities
def distance_between_two_points(city1, city2):
    """
    Calculate the distance between two cities in kilometers.

    :param city1: The first city.
    :param city2: The second city.
    :return: The distance between the two cities in kilometers.
    """
    coords_1 = cities[city1]
    coords_2 = cities[city2]
    return distance.distance(coords_1, coords_2).km

