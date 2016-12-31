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

