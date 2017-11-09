""" #39 Integer right triangles"""

from math import sqrt

def numOfSolutions(p):
    solutions = []
    for a in range(1,p):
        for b in range(1,p):
            c = sqrt(a*a + b*b)
            if a + b + c == p:
                ans = sorted([a, b, c])
                try:
                    solutions.index(ans)
                except ValueError:
                    solutions.append(ans)
    return len(solutions)

maxP = [0,0]

for p in range(1,1000):
    if numOfSolutions(p) > maxP[1]:
        maxP[1] = numOfSolutions(p)
        maxP[0] = p

print maxP

