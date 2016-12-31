""" #14 Longest Collatz sequence"""

startingNumber = 1
max = [0,0]
while startingNumber<1000000:
    n = startingNumber
    counter = 0
    while n != 1:
        if n%2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        counter += 1
    if counter > max[1]:
        max[1] = counter
        max[0] = startingNumber
    startingNumber += 1
print max

