""" #37 Truncatable primes"""

from eulerlib import is_prime

def isTrancatable(num):
    numS = str(num)
    digits = []
    for i in range(len(numS)):
        digits.append(int(numS[i:]))
        digits.append(int(numS[:len(numS) -i]))
    digits = set(digits)
    for d in digits:
        if not is_prime(d):
            return False
    return True

truncatablePrimes = []
d = 8

while len(truncatablePrimes) != 11:
    if isTrancatable(d):
        truncatablePrimes.append(d)
    d += 1

print sum(truncatablePrimes)

