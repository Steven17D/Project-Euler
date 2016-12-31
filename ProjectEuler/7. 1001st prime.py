""" #7 1001st prime"""

counter = 0
num = 1

def isPrime(n):
	for i in range(2,n):
		if n%i==0:
			return False
	return True

while counter != 10001:
	num = num + 1
	if isPrime(num):
		counter += 1

print num

