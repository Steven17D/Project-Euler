""" #3 Largest prime factor"""

number = 600851475143
dividers = []
divider = 2
while divider <= number:
	if number%divider == 0:
		number = number / divider
		dividers.append(divider)
	divider = divider + 1

print dividers[-1]

