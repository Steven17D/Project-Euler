""" #4 Largest palindrome product"""

polindroms = []
maxNum = 999*999
minNum = 100*100
def isPolindrom(num):
	num = str(num)
	for i in xrange(len(num)/2):
		if num[i] != num[(len(num)-1) - i]:
			return False
	return True

for n1 in range(999,100,-1):
	for n2 in range(999,100,-1):
		n = n1*n2
		if isPolindrom(n):
			polindroms.append(n)

polindroms.sort(reverse = True)
print polindroms[0]

