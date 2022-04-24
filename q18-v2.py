# 04/20/2022

# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# # NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

raw = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

trigon = []
for line in raw.split('\n'):
    row = []
    for number in line.split(' '):
        if number != '':
            row.append(int(number))
    trigon.append(row)

options = [0,1]
points = []

class POINT(object):
    def __init__(self):
        self.origin = (0,0)
        self.origin_value = 0
        self.possibilities = {} # dict
        self.choice = (0,0)
        self.choice_value = 0

def treeSum(trigon,point,points):
    tree = {}
    treeSm = 0
    choices = True
    
    while choices:
        for p in points:
            if len(tree) == 0:
                if p.origin == point:
                    for choice in p.possibilities:
                        x,y = choice
                        tree[choice] = trigon[x][y]
            temp = tree.copy()
            for branch in temp:
                opt = branch
                if p.origin == opt:
                    if len(p.possibilities) == 0:
                        choices = False
                    else:
                        for choice in p.possibilities:
                            x,y = choice
                            tree[choice] = trigon[x][y]
    
    for branch in tree:
        treeSm += tree[branch]
    print(treeSm)
    return treeSm





for row in trigon:
    x1 = trigon.index(row)
    for number in row:
        y1 = row.index(number)
        p = POINT()
        p.origin = (x1,y1)
        p.origin_value = number
        x2 = x1+1
        try:
            for opt in options:
                y2 = y1+opt
                p.possibilities[(x2,y2)] = trigon[x2][y2]
        except IndexError as e:
            pass
        points.append(p)
 
route = []
start = (0,0)
next = start
# to define all posibilities for right add 1 to lowest y and for right subtract 1 from highest y

for p in points:
    if p.origin == next:
        route.append(p)
        print(p.origin,p.origin_value,p.possibilities)
        x1,y1 = p.origin
        choice = None
        choice_total = 0
        for option in p.possibilities:
            x2,y2 = option
            if y1 == y2: # "going left"
                treeSm = treeSum(trigon,option,points)
                if treeSm > choice_total:
                    choice_total = treeSm
                    choice = option
            if y2 == y1+1: # "going right"
                treeSm = treeSum(trigon,option,points)
                if treeSm > choice_total:
                    choice_total = treeSm
                    choice = option
        if choice != None:
            next = choice

if len(route) != 0:
    for point in route:
        print(p.origin_value)
else:
    print('error')