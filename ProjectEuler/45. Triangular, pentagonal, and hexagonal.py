""" #45 Triangular, pentagonal, and hexagonal"""

P = set()
T = set()
H = set()

def p(n):
    return n* (n + 1)/2

def t(n):
    return n* (3*n - 1)/2

def h(n):
    return n* (2*n - 1)

for i in range(999999):
    P.add(p(i))
    T.add(t(i))
    H.add(h(i))
    if len(P.intersection(T.intersection(H))) > 3:
        print P.intersection(T.intersection(H))
        break

