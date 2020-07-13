#PayCompute

h = input('Enter the number of hours:')
try:
    hours = float(h)
except:
    print('Error: Enter numeric input')
    quit()

r = input('Enter the rate per hour:')
try:
    rate = float(r)
except:
    print('Error: Enter numeric value')
    quit()

if hours > 40:
    extra_hours = hours-40
    #print (extra_hours)
    new_rate = 1.5*rate
    #print (new_rate)
    pay = (extra_hours*new_rate)+(40*rate)

else:
    pay = hours*rate

print('Pay is:', pay)
