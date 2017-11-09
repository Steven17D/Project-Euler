""" #50 Consecutive prime sum"""

import cPickle as pickle

def isPrime(n):
    if not hasattr(isPrime,"primes"):
        isPrime.primes = pickle.load(open("primesTillMillion.p","rb"))
    if n in isPrime.primes:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    isPrime.primes.append(n)
    return True

isPrime(2)
primes = isPrime.primes[:]

result = [0,0]
for start in xrange(1,len(primes)-1):
    for end in xrange(start,len(primes)-1):
        ps = primes[start:end]
        if result[1] >= len(ps):
            continue
        s = sum(ps)
        if s < 1000000 and isPrime(s):
            found = [s,len(ps)]
        elif s > 1000000:
            result = found
            break

print result[0]