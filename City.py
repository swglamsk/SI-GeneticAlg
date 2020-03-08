import geopy.distance as gp
import math


class City:
    x: float
    y: float

    def __init__(self, name, x, y, weight_type):
        self.name = name
        self.x = x
        self.y = y
        self.weightType = weight_type

    def __str__(self):
        return "Name:{0}\tx:{1}\ty:{2}".format(self.name, self.x, self.y)


def calculate_distance(town1, town2):
    if town1.weightType == "GEO":
        return float(gp.great_circle((town1.x, town1.y), (town2.x, town2.y)).km)
    else:

        return float(math.sqrt((town1.x - town2.x) ** 2 + (town1.y - town2.y) ** 2))
