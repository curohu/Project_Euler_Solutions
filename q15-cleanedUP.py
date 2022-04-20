# 04/19/2022

# this is a cleaned up version of the script

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# see example at https://projecteuler.net/problem=15

# How many such routes are there through a 20×20 grid?


GRID_SIZE = 20
LEGAL_MOVES = [(1,0),(0,1)] # right and down

def move(startingLocation,moveVector):
    x1,y1 = startingLocation
    x2,y2 = moveVector
    if x1+x2 > GRID_SIZE or y1+y2 > GRID_SIZE:
        return None
    else:
        return ((x1+x2),(y1+y2))

previousMoves = [[(0,0),1]]
for n in range(1,(GRID_SIZE*2)+1):
    currentMoves = list() # 
    for location in previousMoves:
        for vector in LEGAL_MOVES:
            m = move(location[0],vector)
            if m is not None:
                found = False
                for cM in currentMoves:
                    if m == cM[0]:
                        cM[1] += location[1] # to save memory and processing time I am counting the number of times a point is reached and then carrying that over
                        found = True
                        break
                if not found:
                    currentMoves.append([m,location[1]])
    previousMoves = currentMoves
print(previousMoves[0][1])

# 137846528820