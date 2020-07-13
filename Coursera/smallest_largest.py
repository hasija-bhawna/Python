#smallest and largest
smallest = None
largest = -1

while True:
    n = input('Enter a number:')

    if n == 'done':
        break

    try:
        num = float(n)
    except:
        print('Invalid input')
        continue

    #find the largest number
    if num > largest:
        largest = num

    #find the smallest
    if smallest is None :
        smallest = num
    elif num < smallest :
        smallest = num

print('Maximum is', int(largest))
print('Minimum is', int(smallest))
