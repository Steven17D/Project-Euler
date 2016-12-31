""" #29 Distinct powers"""

limit = 100

result = set()

for a in range(2,limit+1):
    for b in range(2,limit+1):
        result.add(a**b)

print len(result)

