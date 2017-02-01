""" #583 Heron Envelopes"""
#Solution is too slow. checkout the C++ solution.
from math import sqrt
from math import cos
from math import pi as PI
from math import acos
def isInt(n):
    return n - int(n) == 0

def diagonal(a, b):
    return sqrt(a**2 + b**2)

def S(maxP):
    s = 0
    for base in xrange(1, maxP/2):
        halfBase = base/2.0

        for side in xrange(1, maxP/2):
            if not isInt(diagonal(base,side)): continue #check the DA, BE diagonals
            
            for flapHight in xrange(1, side):
                CD = diagonal(halfBase,flapHight)
                if not isInt(CD): continue          #if CD, BC are not integers try next roof
                else: CD = int(CD)
                perimeter = base + side + CD + CD + side
                if perimeter > maxP: break              #if the perimeter too big stop trying roofs
                CE = diagonal(side+flapHight,halfBase)
                if isInt(CE):
                    print base, side, CD
                    s += perimeter

    return s

print S(10**7)


"""              C
                / \
             /       \
          /             \      <-- the flap
       /                   \
   B /_ _ _ _ _ _ _ _ _ _ _ _ \ D
    |                          |
    |                          |
    |                          |    <-- the side
    |                          |
    |                          |
   A|__________________________|E   <-- the base

"""