# score and grades with function

sc = input('Enter a score  between 0.1 and 0.9:')

try:
    score = float(sc)
    if score >= 1.0:
        print('bad Score')
except:
    print('Bad score!')
    quit()

def computegrade(score):
    if (score > 0.9):
        grade = "A"
    elif (score > 0.8):
        grade = "B"
    elif (score > 0.7):
        grade = "C"
    elif (score > 0.6):
        grade = "D"
    elif (score <= 0.6):
        grade = "F"

    return grade

grade = computegrade(score)
print(grade)
