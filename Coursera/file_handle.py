#file handling

fname = input('Enter a file name:')
fhand = open(fname)
#rea = fhand.read()
count = 0
for line in fhand:
    ln = line.rstrip()
    #print(line)
    #if line.startswith('a') :
    #    print(line)
    #    count = count + 1
    print(ln.upper())

print('Number of lines in the file:', count)
