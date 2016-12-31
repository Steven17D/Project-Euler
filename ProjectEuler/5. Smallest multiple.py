""" #5 Smallest multiple"""

#1-10 => 2520 => divisible by 2, 3, 4, 5, 6, 7, 8, 9, 10, 12(2*6), 14(2*7), 15(3*5), 16(4*4), 18(9*2), 20(10*2)
#primes in 10-20 => 11, 13, 17, 19

def isDivisivle(num):
	for div in range(2,20):
		if num%div != 0:
			return False
	return True

print 2520*11*13*17*19*2, isDivisivle(2520*11*13*17*19*2)

