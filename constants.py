from numpy.random import randn


WIDTH = 1200
HEIGHT = 1200
N_AGENTS = 100
N_FOODS = 7
#Time a frame is shown
FRAME_TIME = 0.15




#BLOOB CONSTANTS
BLOOB_START_SIZE = 20
SIZE_SPREAD_SIZE = 8
size_initializer = lambda : (randn(1)[0]/SIZE_SPREAD_SIZE + 1) * BLOOB_START_SIZE

# currently not used
# SPEED_SPREAD_SIZE = 0.7
# speed_initializer = lambda : (randn(1)[0]/SPEED_SPREAD_SIZE + 1) * BLOOB_START_SIZE

# BLOOB_START_SPEED = 100
EATING_SIZE_CHANGE = 0.05
STEP_ENERGY_LOSS = 0.02

#FOOD CONSTANTS
FOOD_SIZE = 7




#color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)