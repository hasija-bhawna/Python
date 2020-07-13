#count_the_items in a loop
num = 0
total = 0
print('No of items before:', num)
print('Total of items before:', total)
for count in [1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 9, 9, 0, 5, 4, 3, 3, 3, 2, 2]:
    num = num + 1
    #print(num, count)
    total = total + count

print('No of items after:', num)
print('Total sum of numbers after:', total)
