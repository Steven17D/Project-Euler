""" #43 Sub-string divisibility"""

from itertools import permutations

LEN = 10

def isRare(number):
    n = str(number)
    if int(n[1:4])%2==0 and int(n[2:5])%3==0 and int(n[3:6])%5==0 and int(n[4:7])%7==0 and int(n[5:8])%11==0 and int(n[6:9])%13==0 and int(n[7:10])%17==0:
        return True
    return False

pands = list(permutations(range(LEN)))
pands = map(lambda x: int(''.join(map(str,x))),pands)
pands = filter(lambda x: x > 10**(LEN-1),pands)
pands = filter(lambda x: isRare(x),pands)

print pands
print sum(pands)

