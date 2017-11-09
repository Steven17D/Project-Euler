""" #10 Summation of primes"""

def isPrime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True

primes = []

for n in range(2,2000000):
	if isPrime(n):
		primes.append(n)

print sum(primes)

