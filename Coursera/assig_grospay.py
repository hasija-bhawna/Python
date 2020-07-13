#grosspay_2
hrs = input("Enter the hours:")
hours = float(hrs)
r = input("Enter the rate:")
rate = float(r)

if hours <= 40 :
    grosspay = (hours*rate)
    print ('Gross pay is:',grosspay)

else :
    extra_hours = (hours - 40)
    print ('Number of extra hours:', extra_hours)
    rate_extra = (1.5*rate)*extra_hours
    print ('Pay for extra hours:',rate_extra)

    grosspaydouble = ((40*rate)+rate_extra)
    #print ('Gross pay is:',grosspaydouble)
    print (grosspaydouble)
