""" #40 Champernowne's constant"""

number = ""
n = 1

while len(number) < 1000001:
    number += str(n)
    n += 1

print int(number[1-1]) * int(number[10-1]) * int(number[100-1]) * int(number[1000-1]) * int(number[10000-1]) * int(number[100000-1]) * int(number[1000000-1])

