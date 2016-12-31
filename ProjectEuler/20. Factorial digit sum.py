""" #20 Factorial digit sum"""

def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

print sum(map(int,str(factorial(100))))

