import pygame
import time
import numpy as np
from constants import *
from helpers import *
from agent_and_food import Agent, Food, Obj
from typing import List



def run_episode(screen, agents: List[Agent], foods: List[Food]):
    running = True
    while running:
        print(pygame.time.get_ticks())
        time.sleep(FRAME_TIME)
        if pygame.time.get_ticks() > 20000: running = False
        screen.fill(WHITE)
        new_cords = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        
        to_delete = []
        closest_food_list = {agent_id : [] for agent_id in agents.keys()}
        for id in agents.keys():
            #drawing agents and deleting them if they ran out of energy
            agents[id].move()
            agents[id].draw(screen)
            agents[id].energy -= STEP_ENERGY_LOSS
            if agents[id].energy <= 0: 
                print("delete", id)
                to_delete.append(id)
            
            #finding closest food and eating it if it is coliiding with agent
            if len(foods) == 0: continue
            for food in foods:
                closest_food_list[id].append((agents[id].distance(food), food))
            
            closest_food_list[id] = np.array(closest_food_list[id])
            
            min_id = np.argmin(closest_food_list[id][:, 0])
            closest_food = closest_food_list[id][min_id][1]
            agents[id].closest_food = closest_food

            if agents[id].distance(closest_food) < agents[id].size + FOOD_SIZE:
                agents[id].energy += closest_food.energy
                foods.remove(closest_food)


        #dictionary of lists of tuples (distance, id) of closest agents to each agent
        closest_agents_list = {id : [] for id in agents.keys()}

        #finding closest agents for each agent and eating them if they are coliiding with agent
        agent_pairs = pairs_of_ids(agents.keys())
        for pair in agent_pairs:
            agent, other_agent = agents[pair[0]], agents[pair[1]]
            #not using agent.distance because it is slower due to passing its image
            distance  = np.sqrt((agent.x - other_agent.x)**2 + (agent.y - other_agent.y)**2)
            
            closest_agents_list[pair[0]].append((distance, pair[1]))
            closest_agents_list[pair[1]].append((distance, pair[0]))

            if distance < (agent.size + other_agent.size)/1.5:
                if agent.size > other_agent.size:
                    agent.survives_episode = True
                    agent.size += other_agent.size*EATING_SIZE_CHANGE
                    agent.energy += other_agent.size*EATING_SIZE_CHANGE
                    to_delete.append(pair[1])
                else:
                    other_agent.size += agent.size*EATING_SIZE_CHANGE
                    other_agent.survives_episode = True
                    other_agent.energy += other_agent.size*EATING_SIZE_CHANGE
                    to_delete.append(pair[0])
        
        if len(agents) > 1:
            for agent_id in agents.keys():
                closest_agents_list[agent_id] = np.array(closest_agents_list[agent_id])
                closest_agent_list_id = np.argmin(closest_agents_list[agent_id][:, 0])
                closest_agent_id = closest_agents_list[agent_id][closest_agent_list_id][1]
                agents[agent_id].closest_agent = Obj(agents[closest_agent_id].x,  agents[closest_agent_id].y)

        for id in set(to_delete):
            del agents[id]

        for food in foods:
            food.draw(screen)
        

        pygame.display.update()


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bloobs")
    agents = init_x_agents(N_AGENTS)
    foods = init_x_foods(N_FOODS)
    run_episode(screen, agents, foods)


if __name__ == "__main__":
    main()