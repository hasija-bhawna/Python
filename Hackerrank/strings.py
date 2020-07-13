# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
str_lst = []

for str in range(0, n):
    str = input()
    str_lst.append(str)
    #print(str_lst)

for strings in str_lst:
    #print(strings)
    my_even = strings[::2]
    my_odd = strings[1::2]
    print(my_even + ' ' + my_odd)
