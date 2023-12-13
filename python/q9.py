# 04/15/2022

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


from math import prod
import sys

target = 1000
for a in range(1,target):
    for b in range(1,target):
        for c in range(1,target):
            if (a<b<c) and (a+b+c==target) and (a**2 + b**2 == c**2):
                pTriple = (a,b,c)
                print(prod(pTriple),pTriple)
                sys.exit()



    #     if pTriple is not None:
    #         break
    # if pTriple is not None:
    #     break
#print(prod(pTriple),pTriple)

# Solution is: 31875000 (200, 375, 425)




# quantity = 3 # number of Pythag Tripples
# def generatePythag(q):
#     x,y,z = 0,0,0
#     pythagTripples = list()
#     while len(pythagTripples)<q:
#         if x**2 + y**2 == z**2:
#             pythagTripples.append((x,y,z))
#             print((x,y,z))
#             z+=1
#         else:
#             while y<z:
#                 while x<y:
#                     x +=1
#                 y+=1
#             z+=1
#     return pythagTripples

# lst = generatePythag(quantity)
# print(len(lst))
# for l in lst:
#     print(l)



# while a+b+c != target:
#     while b<c:
#         b += 1
#         while a<b:
#             a += 1
#     c += 1

# print(a,b,c,"Target:",target)

