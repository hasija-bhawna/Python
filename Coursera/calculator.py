# calculator

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

operator = input('Enter a operator from + - * /:')
num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))

if (operator == "+"):
    print('Sum is:', add(num1, num2))

elif (operator == '-'):
    print('Difference is:', sub(num1, num2))

elif (operator == '*'):
    print('Multiplication is:', mul(num1, num2))

elif (operator == '/'):
    print('Division is:', div(num1, num2))

else:
    print('Invalid input!')
