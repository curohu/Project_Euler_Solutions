# 04/19/2022

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


from datetime import datetime
from numba import jit, numba, prange
from numpy import maximum

MAXIMUM = 1000000

@numba.jit(nopython=True)
def getChain(startingNumber):
    chain = 0
    workingNumber = int(startingNumber)
    while workingNumber != 1:
        if workingNumber%2 == 0:
            chain += 1
            workingNumber = workingNumber/2
        else:
            chain += 1
            workingNumber = (3*workingNumber)+1
    return chain

@numba.jit(nopython=True)
def issueChains(max):
    index = 1
    largestChainLength = 1
    for n in prange(2,max+1):
        chain = getChain(n)
        if chain > largestChainLength:
            largestChainLength = chain
            index = n
    return index, largestChainLength

@numba.jit(nopython=True)
def findLargestChain():
    index, chainLength = list(issueChains(MAXIMUM))
    print(index, chainLength)

if __name__ == "__main__":
    sTime = datetime.now()
    findLargestChain()
    print(datetime.now()-sTime)

# 837799 524
# 0:00:04.951380

