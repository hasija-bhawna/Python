#string slicing

text = "X-DSPAM-Confidence:    0.8475"

str = text.find('0')
str1 = text.find('5',str)

data = text[str:str1+1]
print(type(data), data)
num = float(data)
print(num)
