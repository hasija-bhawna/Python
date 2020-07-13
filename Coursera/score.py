#score
sco = input("Enter a score between 0.0 and 1.0:")
score = float(sco)
if score > 1.0 :
    print('Enter a value between 0.1 and 1.0')
    quit()

elif score >= 0.9 :
    print('A')

elif score >= 0.8 :
    print('B')

elif score >= 0.7 :
    print('C')

else :
    score < 0.6
    print('F')
