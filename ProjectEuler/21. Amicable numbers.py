""" #21 Amicable numbers"""

def sumOfDivs(n):
    divs = []
    for i in range(1,n/2 + 1):
        if n%i==0:
            divs.append(i)
    return sum(divs)

counter = 0

for i in range(1,10001):
    if i == sumOfDivs(sumOfDivs(i)) and sumOfDivs(i) != i:
        counter += i

print counter

