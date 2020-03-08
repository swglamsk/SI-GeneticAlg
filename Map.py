from City import City


def load_from_file(path):
    with open(path) as f:
        lines = [line.rstrip('\n') for line in f]

    name = lines[0].split(": ")[1]
    type = lines[1].split(": ")[1]
    comment = lines[2].split(": ")[1]
    dimension = lines[3].split(": ")[1]
    edge_weight_type = lines[4].split(": ")[1]
    towns_list = lines[6:6 + int(dimension)]
    towns = read_towns(towns_list, edge_weight_type)

    return Map(name, type, comment, dimension, edge_weight_type, towns)


def read_towns(towns, edge_weight_type):
    cities = []
    for line in towns:
        newline = line.split(" ")
        city = City(newline[0], float(newline[1]), float(newline[2]), edge_weight_type)
        cities.append(city)
    return cities


class Map(object):
    name: str
    type: str
    comment: str
    dimension: float
    edge_weight_type: str
    towns: [City]

    def __init__(self, name, type, comment, dimension, edge_weight_type, towns):
        self.name = name
        self.type = type
        self.comment = comment
        self.dimension = dimension
        self.edgeWeightType = edge_weight_type
        self.towns = towns

    def __str__(self):
        return "Name:{0}\nType:{1}\nComment:{2}\nDimension:{3}\nEdge Weight Type:{4}".format(self.name, self.type,
                                                                                        self.comment, self.dimension,
                                                                                        self.edgeWeightType)
