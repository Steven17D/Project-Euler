""" #2 Even Fibonacci numbers"""

fibNumbers = [1,2]
LIMIT = 4000000

while fibNumbers[-1]+fibNumbers[-2] < LIMIT:
	fibNumbers.append(fibNumbers[-1]+fibNumbers[-2])

evenValuedFibs = filter(lambda x: x%2==0,fibNumbers)
result = sum(evenValuedFibs)
print result

