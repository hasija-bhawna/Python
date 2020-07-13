#function def for leap year and month

import re

try:
    year = int(input('Enter the year:'))
    month = int(input('Enter the month:'))
    #monthdays(month)
except:
    print('Invalid input. Enter a numeric')


def leapyear(y):
    if (y%4 == 0) or (y%100 != 0) and (y%400 == 0):
        print(y, 'is a leap year!')
    else:
        print(y, 'is not a leap year!')
    #return y

def monthdays(m):
    if (m == 1 or m == 3 or m == 5 or m == 7 or m ==8 or m == 10 or m == 12):
        print('The month has 31 days')
    elif (m == 4 or m == 6 or m == 9 or m == 11):
        print('The month has 30 days')
    elif (m == 2):
        output = leapyear(year)
        value = re.search("not", outputb )
        print(value)
        if value == :
            print('The month has 28 days')
        else:
            print('The month has 29 days')
    #return m

leapyear(year)
monthdays(month)
