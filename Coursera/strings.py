#strings

index = 0
string = input('Enter a string:')
length = len(string)
print('Length of string is:', length)

while index < length :
    letter = string[index]
    print(index, letter)
    index = index + 1
print('out of while loop')

index = 0
for letter in string :
    print(index, letter)
    index = index + 1
print('out of for loop')
