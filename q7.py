# 04/15/2022

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

p = 3
i = 2
t = 10001
while i <= t:
    p += 2
    prime = True
    for i in range(2,int(p/2)+1):
        if (p%i) == 0:
            prime = False
    if prime:
        i += 1
        print(i)
print(p)
        