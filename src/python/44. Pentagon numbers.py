""" #44 Pentagon numbers"""

pentagons = {}

def Max(l):
    if l == []:
        return 0
    else:
        return max(l)

def isPentagonal(penNum):
    global pentagons
    if penNum in pentagons.values():
        return True
    while not(penNum in pentagons.values()) and penNum >= Max(pentagons.values()):
        lastN = len(pentagons)
        pentagonAt(lastN + 1)
        if pentagons[lastN+1] == penNum:
            return True

    return False

def pentagonAt(n):
    global pentagons

    if pentagons.has_key(n):
        return pentagons[n]
    else:
        res = n*(3*n-1)/2
        pentagons[n] = res
        return res

for a in xrange(1,10000):
    for b in xrange(1,a):
        if isPentagonal(pentagonAt(a) + pentagonAt(b)) and isPentagonal(pentagonAt(a) - pentagonAt(b)):
            print pentagonAt(a) - pentagonAt(b)
            break

