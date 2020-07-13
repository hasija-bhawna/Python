#DICTIONARIES

name1 = {'name':'rayhan',
        'age':'5',
        'class':'I',
        'fav_color':'red and blue'}

print(name1)
print('Name is:', name1['name'])
print('Age is:', name1['age'])
print('Class is:', name1['class'])
print('Color is:', name1['fav_color'])

#Change value of a key
name1['class'] = 'II'
print('New class is:', name1['class'])
print(name1)

#Add a key-value pair
name1['address'] = '1116 vasant Kunj'
print(name1)
name1['name'] = 'nysa'
print(name1)

del name1['address']
print(name1)
for key, value in name1.items():
    print('Key is:', key)
    #print('\n Value is:', value)
    #print(key, value)
