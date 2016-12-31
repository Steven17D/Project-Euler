""" #12 Highly divisible triangular number"""

primes = []

def findPrimes(num):
    for div in range(2,num+1):
        if num%div == 0:
            primes.append(div)
            findPrimes(num/div)
            break

def numOfDivisors(num):
    findPrimes(num)
    total = 1
    while len(primes) != 0:
        power = primes.count(primes[0])
        for v in range(power):
            primes.remove(primes[0])
        total *= power+1
    return total


x = 1
while True:
    n = (x*(x+1))/2
    divs = numOfDivisors(n)
    print x, n, divs
    if divs >= 500:
        break
    x += 1

