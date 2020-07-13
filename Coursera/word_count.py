#word count
counts = dict()
fname = input('Enter a file name:')
fhand = open(fname)

for line in fhand :
     #print('Line:', line)

     words = line.split()
     #print('Words:', words)

     for word in words:
         counts[word] = counts.get(word,0) + 1
         print('counts:', counts)
