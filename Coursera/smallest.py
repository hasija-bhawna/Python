#smallest
smallest = None
print('Before!')

for number in [26, 23, 81, 25, 20, 7, 89, 94, 4, 1, 92, 11] :
    print('Number is:', number)
    if smallest is None :
        smallest = number
        print('Smallest is:', number)
    elif number < smallest :
        smallest = number
        print(number, smallest)

print('Smallest is:', smallest)
