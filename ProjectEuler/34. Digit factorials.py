""" #34 Digit factorials"""
from math import factorial

def isCurious(num):
    numArr = map(int,str(num))
    sum = 0
    for n in numArr:
        sum += factorial(n)
    return sum == num

d = 3
results = []

while d < 1000000:
    if isCurious(d):
        results.append(d)
    d += 1

print sum(results)

