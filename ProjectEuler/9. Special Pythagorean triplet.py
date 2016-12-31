""" #9 Special Pythagorean triplet"""

import math
# b = 1000 * (a - 500) / (a - 1000)

for a in range(1,1000):
	for b in range(1,1000):
		if math.sqrt(a**2 + b**2)%1 == 0 and a+b+math.sqrt(a**2 + b**2) == 1000:
			print a,b,math.sqrt(a**2 + b**2) , " = " , a*b*math.sqrt(a**2 + b**2)


