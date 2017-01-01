""" #1 Multiples of 3 and 5"""

print sum(filter(lambda x: x%3 == 0 or x%5==0,range(0,1000)))

