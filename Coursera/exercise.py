#exercise on loop, sum, average, try, except

num = 0
total = 0
while True :
    n = input('Enter a number:')
    if n == 'done' :
        break
    try:
        number = float(n)
    except:
        print('Invalid Input')
        continue

    num = num + 1
    total = total + number

print('Total number of inputs:', num)
print('Sum of numbers:', total)
print('Average:', total/num)
