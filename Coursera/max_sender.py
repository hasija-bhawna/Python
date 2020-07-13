#assignment no 9.4 find the maximum sender

counts = dict()
fname = input('Enter a file name:')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhand = open(fname)

for line in fhand:
    words = line.split()
    print(words)
