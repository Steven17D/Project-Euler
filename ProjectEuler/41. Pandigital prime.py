""" #41 Pandigital prime"""

from eulerlib import primes
from eulerlib import is_pandigital

def isPandigital(n):
    return is_pandigital(n,1,len(str(n)))

ps =primes(987654322)
ps.reverse()
for p in ps:
    if isPandigital(p):
        print p
        break

