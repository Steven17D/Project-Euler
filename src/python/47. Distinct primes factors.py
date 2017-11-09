""" #47 Distinct primes factors"""
import itertools

def isPrime(n):
    if not hasattr(isPrime,"primes"):
        isPrime.primes = [1]
    if n in isPrime.primes:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    isPrime.primes.append(n)
    return True

def getPrimes(n):
    if isPrime(n):
        return [n]
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0 and isPrime(i):
                return [i] + getPrimes(n/i)
                break

def isCompositeOfFourDistinctPrimes(n):
    allFourPrimes = set(getPrimes(n))
    if len(allFourPrimes) != 4:
        return False
    mana = reduce(lambda x,y: x*y, allFourPrimes)
    if n % mana == 0 and ((n / mana) in allFourPrimes or n / mana == 1):
        return True
    return False


for i in itertools.count(2):
    isPrime(i)
    if isCompositeOfFourDistinctPrimes(i) and isCompositeOfFourDistinctPrimes(i+1) and isCompositeOfFourDistinctPrimes(i+2) and isCompositeOfFourDistinctPrimes(i+3):
        print i
        break

