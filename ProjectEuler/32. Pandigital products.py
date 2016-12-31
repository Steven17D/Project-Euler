""" #32 Pandigital products"""

from eulerlib import is_pandigital

numbers = set()
for d in range(2,80):
    start = 1234 if d < 10 else 123
    for j in range(start,10000//d):
        if is_pandigital(str(d)+str(j)+str(d*j),1,len(str(d)+str(j)+str(d*j))):
            numbers.add(d*j)

print sum(numbers)

