#input example

#n = input('Enter your name:\n')
#Sname = string(n)
#age = input('Enter your age:')
#class_name = input('Enter your class:')
#print ('Hello', n)
h = input('Enter the hours:')
try:
    hours = float(h)
except:
    print('Enter a valid number')
    quit()

r = input('Enter the rate:')
try:
    rate = float(r)
except:
    print('Enter a valid number')

pay = hours*rate
print('Pay is:', pay)

w = input('Enter the width:')
width = float(w)

h = input('Enter the height:')
height = float(h)

print('Quotient operator:', width//2)
print('Modulo operator:', width%2)
print('Division operator:', width/2.0)
print('Division operator:', height/3)
print('Expression evaluation:', 1 + 2 * 5)
