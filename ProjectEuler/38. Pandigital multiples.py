""" #38 Pandigital multiples"""

from eulerlib import is_pandigital

def isPandigital(n):
    return is_pandigital(n,1,len(str(n)))

for n in range(9487, 9213, -1):
        p = str(n*1) + str(n*2)
        if isPandigital(int(p)):
            print p
            break

