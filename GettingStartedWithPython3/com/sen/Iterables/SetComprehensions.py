'''
Created on 18-Jan-2018

@author: senthilkumar
'''
from math import factorial

if __name__ == '__main__':
    pass
words = "Why somtimes I have belived as many as six impossible things before breakfast".split()
print(words)

print({ len(word) for word in words})
print({len(str(factorial(x))) for x in range(20)})