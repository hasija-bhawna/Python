#grade as per the score

try:
    score = float(input('Enter a score between 0.0 and 1.0:'))
except:
    print('Enter a valid score')
    quit()

if score > 1.0:
    print('Bad score')
elif score >= 0.9:
    print('Grade is A')
elif score >= 0.8:
    print('Grade is B')
elif score >= 0.7:
    print('Grade is C')
elif score >= 0.6:
    print('Grade is D')
elif score < 0.6:
    print('FAIL')
