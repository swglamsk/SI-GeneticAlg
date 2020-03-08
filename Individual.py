import math
import random

from Map import Map, loadFromFile
from City import City, calculate_distance


class Individual:
    map: Map

    def __init__(self, filename):
        self.map = loadFromFile(filename)

    def calculate_fitness(self):
        fitness = 0
        for i in range(len(self.map.towns) - 1):
            fitness += calculate_distance(self.map.towns[i], self.map.towns[i + 1])

        fitness += calculate_distance(self.map.towns[0], self.map.towns[len(self.map.towns) - 1])

        return fitness

    def random_alg(self):
        random.shuffle(self.map.towns)
        print("Najlepszy wynik dla losowego algorytmu:{0} ".format(self.calculate_fitness()))

    def greedy_alg(self):
        starting_town = self.map.towns[0]
        visited = [starting_town]
        current_town = starting_town

        while len(visited) < len(self.map.towns):
            min_distance = float('inf')
            closest_town = City
            for town in self.map.towns:
                if town in visited:
                    continue
                distance = calculate_distance(current_town, town)
                if distance < min_distance:
                    min_distance = distance
                    closest_town = town
            visited.append(closest_town)
            current_town = closest_town

        self.map.towns = visited

        print("Najlepszy wynik dla zachłannego algorytmu:{0} ".format(self.calculate_fitness()))


Individual.greedy_alg(Individual("TSP/berlin11_modified.tsp"))
