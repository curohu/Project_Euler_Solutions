# 04/14/2022

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# Test example
target = 1000 # note the question is ints below target. Range covers n-1 so it is exclusive of target
multi = list()
for i in range(target):
    if (i%3) == 0 or (i%5) == 0:
        multi.append(i)

print(multi)
sum = 0
for i in multi:
    sum += i

print(sum)

# solution is: 233168