'''

""" #1 Multiples of 3 and 5"""

print sum(filter(lambda x: x%3 == 0 or x%5==0,range(0,1000)))

""" #2 Even Fibonacci numbers"""

fibNumbers = [1,2]
LIMIT = 4000000

while fibNumbers[-1]+fibNumbers[-2] < LIMIT:
	fibNumbers.append(fibNumbers[-1]+fibNumbers[-2])

evenValuedFibs = filter(lambda x: x%2==0,fibNumbers)
result = sum(evenValuedFibs)
print result

""" #3 Largest prime factor"""

number = 600851475143
dividers = []
divider = 2
while divider <= number:
	if number%divider == 0:
		number = number / divider
		dividers.append(divider)
	divider = divider + 1

print dividers[-1]

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

""" #5 Smallest multiple"""

#1-10 => 2520 => divisible by 2, 3, 4, 5, 6, 7, 8, 9, 10, 12(2*6), 14(2*7), 15(3*5), 16(4*4), 18(9*2), 20(10*2)
#primes in 10-20 => 11, 13, 17, 19

def isDivisivle(num):
	for div in range(2,20):
		if num%div != 0:
			return False
	return True

print 2520*11*13*17*19*2, isDivisivle(2520*11*13*17*19*2)

""" #6 Sum square difference"""

limit = 100
squareOfSum = sum(range(limit+1))**2
sumOfSquares = sum(map(lambda x: x**2,range(limit+1)))
print squareOfSum - sumOfSquares

""" #7 1001st prime"""

counter = 0
num = 1

def isPrime(n):
	for i in range(2,n):
		if n%i==0:
			return False
	return True

while counter != 10001:
	num = num + 1
	if isPrime(num):
		counter += 1

print num

""" #8 Largest product in a series"""
data = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
datas = []

for i in range(len(data)-12):
	datas.append(data[i:i+13])

datas = map(lambda num: reduce(lambda x,y: long(x)*long(y),num),datas)
print max(datas)

""" #9 Special Pythagorean triplet"""

import math
# b = 1000 * (a - 500) / (a - 1000)

for a in range(1,1000):
	for b in range(1,1000):
		if math.sqrt(a**2 + b**2)%1 == 0 and a+b+math.sqrt(a**2 + b**2) == 1000:
			print a,b,math.sqrt(a**2 + b**2) , " = " , a*b*math.sqrt(a**2 + b**2)


""" #10 Summation of primes"""

def isPrime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True

primes = []

for n in range(2,2000000):
	if isPrime(n):
		primes.append(n)

print sum(primes)

""" #11 Largest product in a grid"""
import sys

data = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

data = map(lambda x: x.split(' '),data.split('\n'))
data = map(lambda subList: map(int,subList),data)

def upSum(x, y):
    return data[x][y]*data[x][y+1]*data[x][y+2]*data[x][y+3]
def downSum(x, y):
    return data[x][y]*data[x][y-1]*data[x][y-2]*data[x][y-3]
def lSum(x, y):
    return data[x][y]*data[x-1][y]*data[x-2][y]*data[x-3][y]
def rSum(x, y):
    return data[x][y]*data[x+1][y]*data[x+2][y]*data[x+3][y]
def rupSum(x, y):
    return data[x][y]*data[x+1][y+1]*data[x+2][y+2]*data[x+3][y+3]
def lupSum(x, y):
    return data[x][y]*data[x-1][y+1]*data[x-2][y+2]*data[x-3][y+3]
def rdownSum(x, y):
    return data[x][y]*data[x+1][y-1]*data[x+2][y-2]*data[x+3][y-3]
def ldownSum(x, y):
    return data[x][y]*data[x-1][y-1]*data[x-2][y-2]*data[x-3][y-3]

def greatestProduct(x,y):
    up, down, l, r, rup, lup, rdown, ldown = [1]*8
    results = []
    if y < 3:
        down, ldown, rdown = [0]*3
    elif y > 16:
        up, lup, rup = [0]*3
    if x<3: 
        l, lup, ldown = [0]*3
    elif x>16:
        r, rup, rdown = [0]*3

    if up == 1:
        results.append(upSum(x,y))
    if down == 1:
        results.append(downSum(x,y))
    if l == 1:
        results.append(lSum(x,y))
    if r == 1:
        results.append(rSum(x,y))
    if rup == 1:
        results.append(rupSum(x,y))
    if lup == 1:
        results.append(lupSum(x,y))
    if rdown == 1:
        results.append(rdownSum(x,y))
    if ldown == 1:
        results.append(ldownSum(x,y))

    return max(results)

maxs = []

for x in range(20):
    for y in range(20):
        try:
            maxs.append(greatestProduct(x,y))
        except:
            print x,y
print max(maxs)

""" #12 Highly divisible triangular number"""

primes = []

def findPrimes(num):
    for div in range(2,num+1):
        if num%div == 0:
            primes.append(div)
            findPrimes(num/div)
            break

def numOfDivisors(num):
    findPrimes(num)
    total = 1
    while len(primes) != 0:
        power = primes.count(primes[0])
        for v in range(power):
            primes.remove(primes[0])
        total *= power+1
    return total


x = 1
while True:
    n = (x*(x+1))/2
    divs = numOfDivisors(n)
    print x, n, divs
    if divs >= 500:
        break
    x += 1

""" #13 Large sum"""

data = """37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690"""

print str(sum(map(long,data.split('\n'))))[:10]

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

""" #15 Lattice paths"""

#40 nCr 20

""" #16 Power digit sum"""

print sum(map(int,str(2**1000)))

""" #17 Number letter counts"""

def int_to_en(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'ninteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninty' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + '-' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred and ' + int_to_en(num % 100)

    if (num < m):
        if num % k == 0: return int_to_en(num // k) + ' thousand'
        else: return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)

    if (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' million'
        else: return int_to_en(num // m) + ' million, ' + int_to_en(num % m)

    if (num < t):
        if (num % b) == 0: return int_to_en(num // b) + ' billion'
        else: return int_to_en(num // b) + ' billion, ' + int_to_en(num % b)

    if (num % t == 0): return int_to_en(num // t) + ' trillion'
    else: return int_to_en(num // t) + ' trillion, ' + int_to_en(num % t)

    raise AssertionError('num is too large: %s' % str(num))

def num2Text(num):
    return int_to_en(num).replace(" ", "").replace("-","")

counter = 0

for num in range(1,1001):
    print num, '\t', num2Text(num)
    counter += len(num2Text(num))
print counter  #21124 little of

""" #18 Maximum path sum I"""

data =   """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

data = data.split('\n')
data = map(lambda x: x.split(' '), data)

maxSum = 0
path = 0b000000000000000
while path <= 0b111111111111111:
    sum = 0
    x = 0
    y = 0
    for d in data:
        sum += int(d[x])
        print int(d[x]),
        if str(format(path, '#017b'))[::-1][y] == '1':
            x += 1
        y += 1
    path += 1
    print sum
    if sum > maxSum:
        maxSum = sum

print maxSum

""" #19 Counting Sundays"""

# 9, 4, 6, 11 => 30 days
# 1, 3, 5, 7, 8, 10, 12 => 31 days
# 2 ~ 28.25 days

calendar = []

# Append empty lists in first two indexes.
map(lambda x: calendar.append([None, None, None, None, None, None, None]), range(5271))

leapYear = False
year = 1899
month = 12
date = 31
dayOfTheWeek = 1

def incDate():
    global date
    global month
    global year
    global leapYear
    if date == 31:
        date = 1
        if month == 12:
            month = 1
            year += 1
            if year%4 == 0:
                if year%100 == 0: #centery
                    if year%400 ==0:
                        leapYear = True
                    else:
                        leapYear = False
                else:
                    leapYear = True
            else:
                leapYear = False
        else:
            month += 1
    elif date == 30 and (month == 9 or month == 4 or month == 6 or month == 11):
        date = 1
        month += 1
    elif ((date == 28 and not leapYear) or (date == 29 and leapYear)) and month == 2: #end of February
        date = 1
        month += 1
    else: #middle of the month
        date += 1


for w in calendar:
    for d in range(len(w)):
        w[d] = (date,month,year)
        incDate()

calendar = calendar[52:] #from 30/12/1900

counter = 0
for w in calendar:
    if w[0][0] == 1:
        counter += 1
print counter

""" #20 Factorial digit sum"""

def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

print sum(map(int,str(factorial(100))))

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

""" #22 Names scores"""

data = sorted(map(lambda x: x.replace('"',"").replace('"',""), open("p022_names.txt","r").read().split(',')))
totalScore = 0

def nameScore(name):
    score = 0
    for char in name:
        score += ord(char) - ord('A') + 1
    return score

for n in range(len(data)):
    totalScore += (n+1) * nameScore(data[n])

print totalScore

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

""" #24 Lexicographic permutations"""

group = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def next_permutation(arr):
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return True


for i in range(1,3628800+1):
    if i == 1000000:
        print group
        break
    next_permutation(group)

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

""" #26 Reciprocal cycles"""
def isPrime(a):
    return not ( a < 2 or any(a % i == 0 for i in range(2, int(a ** 0.5) + 1)))
def phi(n):
    y = n
    for i in range(2,n+1):
        if isPrime(i) and n % i  == 0 :
            y -= y/i
        else:
            continue
    return int(y)

maximum = [0,0]
for i in range(1,1000):
    p = phi(i)
    if p > maximum[1]:
        maximum = [i,phi(i)]

print maximum #983

""" #27 Quadratic primes"""

from eulerlib import is_prime

limitA = 1000
limitB = 1000

def consecutivePrimes(a,b):
    eq = lambda n: n**2 + a*n + b
    counter = 0
    #print eq(counter)
    while is_prime(eq(counter)):
        counter += 1
    return counter

stats = {'product': 0, 'a': None, 'b': None}

for a in range(-limitA,limitA+1):
    for b in range(-limitB,limitB+1):
        product = consecutivePrimes(a,b)
        if product > stats['product']:
            stats['product'] = product
            stats['a'] = a
            stats['b'] = b

print stats, '\nAnswer =', stats['a'] * stats['b']

""" #28 Number spiral diagonals"""

import numpy

size = 1001
Nx=size; Ny=size
matrix= numpy.zeros((Nx,Ny)).tolist()
x, y = size/2, size/2
v = 'r'

def update():
    global x, y, v
    if v == 'r':
        if matrix[x][y+1] != 0:
            x += 1
        else:
            y += 1
            v = 'd'
    elif v == 'd':
        if matrix[x-1][y] != 0:
            y += 1
        else:
            x -= 1
            v = 'l'
    elif v == 'l':
        if matrix[x][y-1] != 0:
            x -= 1
        else:
            y -= 1
            v = 'u'
    elif v == 'u':
        if matrix[x+1][y] != 0:
            y -= 1
        else:
            x += 1
            v = 'r'

for d in range(1,size**2+1):
    matrix[x][y] = d
    update()

sum = 0

for i in range(size):
    sum += matrix[i][i] + matrix[i][size-i -1]

print sum - 1

""" #29 Distinct powers"""

limit = 100

result = set()

for a in range(2,limit+1):
    for b in range(2,limit+1):
        result.add(a**b)

print len(result)

""" #30 Digit fifth powers"""

sum = 0

def sumOfDigits(d):
    sum = 0
    for c in str(d):
        sum += int(c)**5
    return sum

for d in range(2,5*9**5):
    if sumOfDigits(d) == d:
        sum += d

print sum

""" #31 Coin sums"""

target = 200
ways = 0

for a in range(200,-1,-200):
    for b in range(a,-1,-100):
        for c in range(b,-1,-50):
            for d in range(c,-1,-20):
                for e in range(d,-1,-10):
                    for f in range(e,-1,-5):
                        for g in range(f,-1,-2):
                            ways += 1

print ways

""" #32 Pandigital products"""

from eulerlib import is_pandigital

numbers = set()
for d in range(2,80):
    start = 1234 if d < 10 else 123
    for j in range(start,10000//d):
        if is_pandigital(str(d)+str(j)+str(d*j),1,len(str(d)+str(j)+str(d*j))):
            numbers.add(d*j)

print sum(numbers)

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

""" #34 Digit factorials"""
from math import factorial

def isCurious(num):
    numArr = map(int,str(num))
    sum = 0
    for n in numArr:
        sum += factorial(n)
    return sum == num

d = 3
results = []

while d < 1000000:
    if isCurious(d):
        results.append(d)
    d += 1

print sum(results)

""" #35 Circular primes"""

from eulerlib import is_prime

counter = 0  
primeList = []

def rotations(n):
    answer = []
    rotation = str(n)
    while not rotation in answer:
        answer.append(rotation)
        rotation = rotation[1:] + rotation[0]
    return map(int,answer)

def isCircular(n):
    rotList = rotations(n)
    for num in rotList:
        if not is_prime(num):
            return False
    return True

for d in range(2,1000000):
    if isCircular(d):
        counter += 1

print counter

""" #36 Double-base palindrome"""

from eulerlib import is_palindrome

sum = 0

for d in range(1000000):
    if is_palindrome(d,10) and is_palindrome(d,2):
        sum += d

print sum

""" #37 Truncatable primes"""

from eulerlib import is_prime

def isTrancatable(num):
    numS = str(num)
    digits = []
    for i in range(len(numS)):
        digits.append(int(numS[i:]))
        digits.append(int(numS[:len(numS) -i]))
    digits = set(digits)
    for d in digits:
        if not is_prime(d):
            return False
    return True

truncatablePrimes = []
d = 8

while len(truncatablePrimes) != 11:
    if isTrancatable(d):
        truncatablePrimes.append(d)
    d += 1

print sum(truncatablePrimes)

""" #38 Pandigital multiples"""

from eulerlib import is_pandigital

def isPandigital(n):
    return is_pandigital(n,1,len(str(n)))

for n in range(9487, 9213, -1):
        p = str(n*1) + str(n*2)
        if isPandigital(int(p)):
            print p
            break

""" #39 Integer right triangles"""

from math import sqrt

def numOfSolutions(p):
    solutions = []
    for a in range(1,p):
        for b in range(1,p):
            c = sqrt(a*a + b*b)
            if a + b + c == p:
                ans = sorted([a, b, c])
                try:
                    solutions.index(ans)
                except ValueError:
                    solutions.append(ans)
    return len(solutions)

maxP = [0,0]

for p in range(1,1000):
    if numOfSolutions(p) > maxP[1]:
        maxP[1] = numOfSolutions(p)
        maxP[0] = p

print maxP

""" #40 Champernowne's constant"""

number = ""
n = 1

while len(number) < 1000001:
    number += str(n)
    n += 1

print int(number[1-1]) * int(number[10-1]) * int(number[100-1]) * int(number[1000-1]) * int(number[10000-1]) * int(number[100000-1]) * int(number[1000000-1])

""" #41 Pandigital prime"""

from eulerlib import primes
from eulerlib import is_pandigital

def isPandigital(n):
    return is_pandigital(n,1,len(str(n)))

ps =primes(987654322)
ps.reverse()
for p in ps:
    if isPandigital(p):
        print p
        break

""" #42 Coded triangle numbers"""

data = sorted(map(lambda x: x.replace('"',"").replace('"',""), open("p042_words.txt","r").read().split(',')))

def wordToValue(word):
    word = word.lower()
    sum = 0
    for char in word:
        sum += ord(char) - ord('a') + 1
    return sum

def isTriangleWord(word):
    value = wordToValue(word)
    n = 1.0
    while value >= 0.5 * n * (n + 1):
        if value == 0.5 * n * (n + 1):
            return True
        n += 1.0
    return False

counter = 0

for word in data:
    if isTriangleWord(word):
        counter += 1

print counter

""" #43 Sub-string divisibility"""

from itertools import permutations

LEN = 10

def isRare(number):
    n = str(number)
    if int(n[1:4])%2==0 and int(n[2:5])%3==0 and int(n[3:6])%5==0 and int(n[4:7])%7==0 and int(n[5:8])%11==0 and int(n[6:9])%13==0 and int(n[7:10])%17==0:
        return True
    return False

pands = list(permutations(range(LEN)))
pands = map(lambda x: int(''.join(map(str,x))),pands)
pands = filter(lambda x: x > 10**(LEN-1),pands)
pands = filter(lambda x: isRare(x),pands)

print pands
print sum(pands)

""" #44 Pentagon numbers"""

pentagons = {}

def Max(l):
    if l == []:
        return 0
    else:
        return max(l)

def isPentagonal(penNum):
    global pentagons
    if penNum in pentagons.values():
        return True
    while not(penNum in pentagons.values()) and penNum >= Max(pentagons.values()):
        lastN = len(pentagons)
        pentagonAt(lastN + 1)
        if pentagons[lastN+1] == penNum:
            return True

    return False

def pentagonAt(n):
    global pentagons

    if pentagons.has_key(n):
        return pentagons[n]
    else:
        res = n*(3*n-1)/2
        pentagons[n] = res
        return res

for a in xrange(1,10000):
    for b in xrange(1,a):
        if isPentagonal(pentagonAt(a) + pentagonAt(b)) and isPentagonal(pentagonAt(a) - pentagonAt(b)):
            print pentagonAt(a) - pentagonAt(b)
            break

""" #45 Triangular, pentagonal, and hexagonal"""

P = set()
T = set()
H = set()

def p(n):
    return n* (n + 1)/2

def t(n):
    return n* (3*n - 1)/2

def h(n):
    return n* (2*n - 1)

for i in range(999999):
    P.add(p(i))
    T.add(t(i))
    H.add(h(i))
    if len(P.intersection(T.intersection(H))) > 3:
        print P.intersection(T.intersection(H))
        break

'''""" #46 Goldbach's other conjecture"""

def isPrime(n):
    if not hasattr(isPrime,"primes"):
        isPrime.primes = []
    if n in isPrime.primes:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    isPrime.primes.append(n)
    return True

def isGoldbach(n):
    if n == 5777:
        pass
    if isPrime(n):
        return True
    else:
        for p in isPrime.primes:
            twiceSquare = n - p
            Square = twiceSquare / 2
            if (int(Square**0.5)) ** 2 == Square:
                return True
        return False

n = 3
while isGoldbach(n):
    n += 2
print n