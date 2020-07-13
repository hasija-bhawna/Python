import sympy
#range function
#for i in range(10):
#    print(i)

#fibonacci series
a,b = 0,1
while (a<10):
    print(a)
    a,b = b,a+b

# odd-even number
for i in range(2,10):
    if (i % 2 == 0):
        print(i, 'is an even number')
    else:
        print(i, 'is a odd number')
        #continue:

#prime number
for i in range(1,10):
    if sympy.isprime(i):
        print(i, 'is prime')
    else:
        print(i, 'is not Prime')
