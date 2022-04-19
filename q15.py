# 04/19/2022

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# see example at https://projecteuler.net/problem=15

# How many such routes are there through a 20×20 grid?

import numpy as np

GRID_SIZE = 2 #20
LEGAL_MOVES = [(1,0),(0,1)] # right and down
GOAL = (GRID_SIZE,GRID_SIZE) # lower right corner
PLAYFIELD = np.ones((GRID_SIZE+1,GRID_SIZE+1))

routes = list()
location = (0,0)
moves = 0




