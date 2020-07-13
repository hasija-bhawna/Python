#leap year and how many days each month has

year = int(input('Enter a year:'))
month = int(input('Enter a month:'))

if (year%4 == 0) and (year%100 !=0) or (year%400 == 0):
    print('The year is a leap year!')
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        print ('The given month has 31 days')

    elif (month == 4 or month == 6 or month == 9 or month == 11):
        print('The given month has 30 days')

    elif (month == 2):
        print('The month has 29 days.')
    else:
        print('Invalid month')

else:
    print('The year is not a leap year!')
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        print ('The given month has 31 days')

    elif (month == 4 or month == 6 or month == 9 or month == 11):
        print('The given month has 30 days')

    elif (month == 2):
        print('The month has 28 days.')
    else:
        print('Invalid month')
