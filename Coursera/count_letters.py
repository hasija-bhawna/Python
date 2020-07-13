#count number of letters in a string
count = 0
#n = 'ajjjsjhhhhaa@gjhgjjkhkjhkjk#aaaa'
n = input('Enter a string:')
c = input('Enter the letter that you need to count:')

for letter in n :
    if letter == c :
        count = count + 1

print('Number of', c, 'is:', count)

print(n[4:8])

lower = n.lower()
upper = n.upper()

print('Lower case is:', lower)
print('Upper case is:', upper)

str = n.find('@')
str1 = n.find('#',str)

data = n[str+1:str1]
print(data)
