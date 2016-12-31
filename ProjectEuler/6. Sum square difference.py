""" #6 Sum square difference"""

limit = 100
squareOfSum = sum(range(limit+1))**2
sumOfSquares = sum(map(lambda x: x**2,range(limit+1)))
print squareOfSum - sumOfSquares

