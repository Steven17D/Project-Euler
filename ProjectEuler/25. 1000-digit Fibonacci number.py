""" #25 1000-digit Fibonacci number"""

f1 = 1
f2 = 2
index = 2

while f1 + f2< 10**1000:
    temp = f1
    f1 = f2
    f2 = temp + f2
    index += 1

print  index - 3

