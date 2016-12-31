""" #36 Double-base palindrome"""

from eulerlib import is_palindrome

sum = 0

for d in range(1000000):
    if is_palindrome(d,10) and is_palindrome(d,2):
        sum += d

print sum

