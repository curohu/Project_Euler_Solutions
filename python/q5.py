# 04/15/2022

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n = 2520
def func(i):
    return (n%i)==0
while not all(func(i) for i in range(1,21)):
    n += 20
print(n)


# the solution is 232792560