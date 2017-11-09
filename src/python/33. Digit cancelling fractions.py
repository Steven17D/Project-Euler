""" #33 Digit cancelling fractions"""

product = 1

for numerator in range(11,100):
    start = numerator + 1
    for denominator in range(start,100):
        n1 = map(int, str(numerator))
        n2 = map(int, str(denominator))
        x = set(n1).intersection(n2)
        if len(set(n1).intersection(n2)) != 0:
            common = list(set(n1).intersection(n2))[0]
            n1.remove(common)
            n2.remove(common)
            if n2[0] == 0:
                continue
            if float(numerator)/ denominator == float(n1[0])/n2[0] and denominator%10 != 0:
                product *= float(n1[0])/n2[0]
                print numerator, "/", denominator, "=", n1[0], "/", n2[0]

print product**-1

