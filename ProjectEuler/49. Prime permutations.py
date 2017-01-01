""" #49 Prime permutations"""

import itertools

def isPrime(n):
    if not hasattr(isPrime,"primes"):
        isPrime.primes = []
    if n in isPrime.primes:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    isPrime.primes.append(n)
    return True

def hasARule(nList):
    if not hasattr(hasARule,"found"):
        hasARule.found = []
    combs = list(itertools.combinations(nList,3))
    for comb in combs:
        if comb[2] - comb[1] == comb[1] - comb[0]:
            res = int(reduce(lambda x,y: x+y ,map(str,comb)))
            if not res in hasARule.found:
                hasARule.found.append(res)
                print res
            return True
    return False


def hasPermutationsPrimes(n):
    if not isPrime(n):
        return False
    prems = sorted(set(filter(lambda x: x > 1000 and isPrime(x),map(lambda x: int(reduce(lambda a,b: str(a) + str(b),x)),list(itertools.permutations(map(int,list(str(n))),4))))))
    if len(prems) >= 3:
        if hasARule(prems):
            return True

for num in xrange(1000,10000):
    if hasPermutationsPrimes(num):
        pass