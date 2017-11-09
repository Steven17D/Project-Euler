""" #26 Reciprocal cycles"""
def isPrime(a):
    return not ( a < 2 or any(a % i == 0 for i in range(2, int(a ** 0.5) + 1)))
def phi(n):
    y = n
    for i in range(2,n+1):
        if isPrime(i) and n % i  == 0 :
            y -= y/i
        else:
            continue
    return int(y)

maximum = [0,0]
for i in range(1,1000):
    p = phi(i)
    if p > maximum[1]:
        maximum = [i,phi(i)]

print maximum #983

