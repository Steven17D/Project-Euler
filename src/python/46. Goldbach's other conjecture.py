""" #46 Goldbach's other conjecture"""

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

def isGoldbach(n):
    if n == 5777:
        pass
    if isPrime(n):
        return True
    else:
        for p in isPrime.primes:
            twiceSquare = n - p
            Square = twiceSquare / 2
            if (int(Square**0.5)) ** 2 == Square:
                return True
        return False

n = 3
while isGoldbach(n):
    n += 2
print n

