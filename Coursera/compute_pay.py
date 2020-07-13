#computepay()
hrs = input("Enter the hours:")
hours = float(hrs)
r = input("Enter the rate:")
rate = float(r)

def computepay(h,r) :
    if hours <= 40 :
        pay = h*r
    else :
        normal = h*r
        extra = (h-40) * (r*0.5)
        pay = normal + extra

    return pay

grosspay = computepay(hours,rate)
print (grosspay)
