import numpy as np
from constants import *
from typing import List
import math, random
from agent_and_food import Agent, Food


def random_point_in_circle():
    t = random.random()
    u = random.random()
    x = math.sqrt(t) * math.cos(2 * math.pi * u)
    y = math.sqrt(t) * math.sin(2 * math.pi * u)
    return x, y



def pairs_of_ids(ids):
    """returns a list of all possible pairs of ids, without duplicates"""
    y = []
    for i in ids:
        for j in ids:
            if i != j and (i, j) not in y and (j, i) not in y:
                y.append((i, j))
    return y


def init_x_agents(n):
    agents = {}
    for i in range(n):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        agent = Agent(x, y, color)
        agents[i] = agent
    return agents


def init_x_foods(n):
    foods = []
    for i in range(n):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        food = Food(x, y)
        foods.append(food)
    return foods


def distances_matrix(agents: List[Agent]):
    distances = np.zeros((len(agents), len(agents)))
    pairs = pairs(len(agents))

    for i, j in pairs:
        distances[i, j] = agents[i].distance(agents[j])
    return distances



# if __name__ == "__main__":
#     print("helpers.py")
