# 04/15/2022

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from datetime import datetime

stime = datetime.now()
primes = [2,3,5,7]
target = 2000000
p = primes[-1] + 2
while  True:
    for x in range(2,int(p/2)+1):
        if (p%x) == 0:
            p += 2
            break
    else:
        if p < target:
            primes.append(p)
            print(p,end='\r',flush=True)
            p += 2
        else:
            break
print(sum(primes))
print(datetime.now()-stime)

# 142913828922
# 2:34:50.870747 <-- not multithreaded

with open('primes_below_2mill','w') as file:
    for p in primes:
        file.write(str(p)+'\n')
    file.close()

