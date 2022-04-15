# 04/14/2022

# -->!THIS SCRIPT IS A FAILURE!<--
# Though I was able to get the logic working (I think) this will take me litterly years to run on my laptop
# considering that this is a logic challenge I guess I will lookup the proper way
# 600billion was probably chosen for exactly this reason

# I mean look at this crap! it takes ~26 seconds to process 1 million. This may be faster on a compiled language. My guess is that there's a trick
# remaining: 600850475144 
# Chunk Size: 1000000 
# time to process chunk: 0:00:25.684303 
# Estimated remaining time: 1786 days, 3:50:56.612925

# Holly Crap it is due to multithreading overhead, one sec
# nope, though it is faster without the thread initiazation overhead, it will still take 100 days. Maybe if I tried this with a GPU instead of a cpu this would be diffrent 


# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600,851,475,143 ?

# lol I do not actally remember how to derive prime factorizations so I will just brute force it
# multithread for the win!




import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

#     with ThreadPoolExecutor(max_workers=10) as executor:
#             return executor.map(tzTask, pointmap, timeout=30)

target = 600851475143

def factorThread(i):
    if i != 0 and (target%i) == 0:
        return i

def factorThreader(rnge): # this feels like cheating...
    with ThreadPoolExecutor(max_workers=4) as executor:
        return executor.map(factorThread, rnge, timeout=30)

def factorChunker(lst,chunkSize):
    for i in range(0, len(lst), chunkSize):
        yield lst[i:i + chunkSize]

# Try without multithread
def getFactors(target):
    factors = list()
    chunkSize = 1000000
    count = len(range(target+1))
    print(count)
    for f in factorChunker(range(target+1),chunkSize):
        # print(f)
        stime = datetime.datetime.now()
        for i in list(factorThreader(f)): # range is exclusive to target
            if i is not None:
                factors.append(i)
        count = count - chunkSize
        delta = datetime.datetime.now()-stime
        print("remaining:",count,"\nChunk Size:",chunkSize,"\ntime to process chunk:",delta,"\nEstimated remaining time:",(count/100000)*delta,'\n')
    return factors

# def getFactors(target):
#     factors = list()
#     chunkSize = 10000000
#     count = len(range(target+1))
#     print(count)
#     for f in factorChunker(range(target+1),chunkSize):
#         # print(f)
#         stime = datetime.datetime.now()
#         for i in f: # range is exclusive to target
#             if i != 0 and (target%i) == 0:
#                 factors.append(i)
#         count = count - chunkSize
#         delta = datetime.datetime.now()-stime
#         print("remaining:",count,"\nChunk Size:",chunkSize,"\ntime to process chunk:",delta,"\nEstimated remaining time:",(count/100000)*delta,'\n')
#     return factors

def getFactors2(target): # weirdaz threading issue that I don't care about figuring out... for some reason nesting these threads breaks everything and I don't know why...
    factors = list()
    for i in range(target+1): # range is exclusive to target
        if i != 0 and (target%i) == 0:
            factors.append(i)
    return factors

def primeThreader(factors): # this feels like cheating...
    with ThreadPoolExecutor() as executor:
            return executor.map(getFactors2, factors, timeout=30)


def getPrimes(factors): # basically I am going to recursivelly brute force this for every factor until only possible are 1 and prime
    primes = list()
    threads = list(primeThreader(factors))
    for i  in threads: 
        if len(i) == 2 and i[1] not in primes:
            primes.append(i[1])
    return primes

def getLargest(primes): # I am sure that there is a command that can give this result but I am too lazy to look it up...
    largest = 0
    for i in primes[0]:
        if i > largest:
            largest = i

    return largest

def primeChunker(factors,chunkSize):
    for i in range(0, len(factors), chunkSize):
        yield factors[i:i + chunkSize]

startTime = datetime.datetime.now()
a = getFactors(target)
b = list()
print(len(a))
chunksize = 1000
for f in primeChunker(a,chunksize):
    b.append(getPrimes(f))
c = getLargest(b)

print(c)

print(datetime.datetime.now()-startTime)


# solution is:
# lol even with multithreading this took