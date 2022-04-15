# 04/15/2022
# Problems are now imbedding equations see link: https://projecteuler.net/problem=6

num = 100
def sqr(i):
    return i**2
a = sum(map(sqr,range(1,num+1)))
b = sum(range(1,num+1))**2

print(b-a)

# The Solution is : 25164150