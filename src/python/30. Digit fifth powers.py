""" #30 Digit fifth powers"""

sum = 0

def sumOfDigits(d):
    sum = 0
    for c in str(d):
        sum += int(c)**5
    return sum

for d in range(2,5*9**5):
    if sumOfDigits(d) == d:
        sum += d

print sum

