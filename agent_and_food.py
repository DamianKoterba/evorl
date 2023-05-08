from helpers import *
from constants import *
import pygame
import numpy as np

bacteria1 = pygame.image.load('images/bacteria1.png')

class Obj:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

class Agent(Obj):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = size_initializer()
        self.speed = 3
        self.last_direction = 0
        self.survives_episode = False
        self.energy = 10
        self.angle = np.random.randint(0, 360)
        self.image = pygame.transform.scale(bacteria1, (self.size*2, self.size*2))

    def draw(self, screen):
        screen.blit(self.image, (self.x-self.size,self.y-self.size))
        # for future correction of agent image placement
        # pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    

    def move(self):
        self.angle += np.random.randint(-60, 60)
        self.x = np.clip(self.x + self.speed * np.cos(np.deg2rad(self.angle)), 0, WIDTH)
        self.y = np.clip(self.y + self.speed * np.sin(np.deg2rad(self.angle)), 0, HEIGHT)



    def border_distances(self):
        border_distances = dict()
        border_distances["up"] = self.y
        border_distances["down"] = HEIGHT - self.y
        border_distances["left"] = self.x
        border_distances["right"] = WIDTH - self.x
        return border_distances
    
        
    def distance(self, other_object):
        return math.sqrt((self.x - other_object.x)**2 + (self.y - other_object.y)**2)
    

    def get_angle_to(self, other):
        dx = other.x - self.x
        dy = self.y - other.y
        radians = np.arctan2(dy, dx)
        degrees = np.degrees(radians)
        return (degrees + 180) % 360


    def get_state(self, return_list=False):
        """returns state of the agent as a dictionary or list,
        including: distance and angle from closest agent and food,
        energy level, distance from borders"""
        state = dict()
        # - distance to closest agent
        state["agent_dist"] = self.distance(self.closest_agent)
        # - angle to closest agent
        state["agent_angle"] = self.get_angle_to(self.closest_agent)
        # - distance to closest food
        state["food_dist"] = self.distance(self.closest_food)
        # - angle to closest food
        state["food_angle"] = self.get_angle_to(self.closest_food)
        # - energy level
        state["energy"] = self.energy
        # - distance to borders
        state.update(self.border_distances())
        if return_list: state = np.array([state[key] for key in state.keys()])

        return np.array(state)

    def print_cords(self):
        print(f"cords: {self.x} {self.y} {self.size}")


class Food():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 10

    def draw(self, screen):
        pygame.draw.circle(screen, GREEN, (self.x, self.y), FOOD_SIZE)
