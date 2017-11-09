""" #27 Quadratic primes"""

from eulerlib import is_prime

limitA = 1000
limitB = 1000

def consecutivePrimes(a,b):
    eq = lambda n: n**2 + a*n + b
    counter = 0
    #print eq(counter)
    while is_prime(eq(counter)):
        counter += 1
    return counter

stats = {'product': 0, 'a': None, 'b': None}

for a in range(-limitA,limitA+1):
    for b in range(-limitB,limitB+1):
        product = consecutivePrimes(a,b)
        if product > stats['product']:
            stats['product'] = product
            stats['a'] = a
            stats['b'] = b

print stats, '\nAnswer =', stats['a'] * stats['b']

