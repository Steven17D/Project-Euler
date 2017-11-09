import cPickle as pickle

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

for i in range(2,1000000):
    isPrime(i)

pickle.dump(isPrime.primes,open("primesTillMillion.p","wb"))