def reverse(text):
    return text[::-1]

def palindrome(text):
    text = text.lower().replace(" ", "")
    #text = ''.join(text)
    #print(text)
    return text == reverse(text)


inp = input('Enter the text:')

if palindrome(inp):
    print('Input string is a palindrome')
else:
    print('String is not a Palindrome')
#rev = palindrome(inp)
#print(rev)
