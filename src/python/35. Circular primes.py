""" #35 Circular primes"""

from eulerlib import is_prime

counter = 0  
primeList = []

def rotations(n):
    answer = []
    rotation = str(n)
    while not rotation in answer:
        answer.append(rotation)
        rotation = rotation[1:] + rotation[0]
    return map(int,answer)

def isCircular(n):
    rotList = rotations(n)
    for num in rotList:
        if not is_prime(num):
            return False
    return True

for d in range(2,1000000):
    if isCircular(d):
        counter += 1

print counter

