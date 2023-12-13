# 04/19/2022

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# see example at https://projecteuler.net/problem=15

# How many such routes are there through a 20×20 grid?

from datetime import datetime
from numba import jit, numba, prange


GRID_SIZE = 20
LEGAL_MOVES = [(1,0),(0,1)] # right and down
GOAL = (GRID_SIZE,GRID_SIZE) # lower right corner
# grid = []

@numba.jit(nopython=True)
def move(startingLocation,moveVector,GRID_SIZE):
    x1,y1 = startingLocation
    x2,y2 = moveVector
    if x1+x2 > GRID_SIZE or y1+y2 > GRID_SIZE:
        return None
    else:
        return ((x1+x2),(y1+y2))



def main():
    previousMoves = [[(0,0),1]]
    routes = 0
    for n in range(1,(GRID_SIZE*2)+1):
        currentMoves = list() # 
        for location in previousMoves:

            # for abridgedRoutes in range(location[1]):
            for vector in LEGAL_MOVES:
                m = move(location[0],vector,GRID_SIZE)
                if m is not None:
                    # if m == GOAL:
                    #     routes += 1
                    # else:
                    found = False
                    for cM in currentMoves:
                        if m == cM[0]:
                            cM[1] += location[1] # to save memory and processing time I am counting the number of times a point is reached and then carrying that over
                            found = True
                            break
                    if not found:
                        currentMoves.append([m,location[1]])
        # print(currentMoves)
        previousMoves = currentMoves
        print(len(previousMoves),end='\r') # will hit peak and then reconverge to 1; each step will take exponentially longer... 
    print(previousMoves[0][1])

# moveQueue = []
# count = 1
# for n in range(1,(GRID_SIZE*2)+1):
#     moveQueue.append((1,0))

# for m in moveQueue:
#     pass

# print(count)

# for y in range(GRID_SIZE+1):
#     grid.append([])
#     for x in range(GRID_SIZE+1):
#         grid[y].append((x,y))

# for line in grid:
#     print(line)

# goalPoints = [[GOAL,(0,0)]]
# SuccessfulPaths = 0

# moves = 0

# grid.reverse()
# for turn in range(1,(GRID_SIZE*2)+1):
#     for line in grid:
#         line.reverse()
#         for point in line:
#             x1,y1 = point
#             x2,y2 = GOAL
#             moves += x2-x1
#             moves += y2-y1
#             #print(x2-x1,y2-y1)
# print(moves)   




            # for move in LEGAL_MOVES:
            #     location = testMove(point,move,GRID_SIZE)
            #     if location is not None:
            #         for p in goalPoints:
            #             # input(p[0])
            #             if location in p[0]:
            #                 SuccessfulPaths += 1
            #                 goalPoints.append([point,move])


# print(goalPoints)
# print(SuccessfulPaths)



    

sTime = datetime.now()
main()
print(datetime.now()-sTime)


# 137846528820
# 0:00:00.118958