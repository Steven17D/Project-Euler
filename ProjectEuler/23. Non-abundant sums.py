""" #23 Non-abundant sums"""

from eulerlib import Divisors

def isAbundant(num):
    divs = Divisors().divisors(num)
    return (sum(divs[:-1])>num)

def writtenAsTheSumOfTwoAbundantNumbers(num):
    for n1 in range(1,num/2 + 1):
        if isAbundant(n1) and isAbundant(num - n1):
            return True
    return False

counter = 0

for n in range(1,28124):
    if not writtenAsTheSumOfTwoAbundantNumbers(n):
        counter += n

print counter

