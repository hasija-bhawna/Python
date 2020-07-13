#compute pay with a function

h = input('Enter the number of hours:')
hours = float(h)

r = input('Enter the rate per hour:')
rate = float(r)

def computepay(hours, rate):
    if hours <= 40:
        pay = hours*rate
    else:
        extra_hours = (hours-40)
        new_rate = (1.5*rate)
        pay = (40*rate) + (new_rate*extra_hours)

    return pay

Pay = computepay(hours,rate)
print('The pay is:', Pay)
