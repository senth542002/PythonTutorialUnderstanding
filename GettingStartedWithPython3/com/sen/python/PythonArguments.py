'''
Created on 30-Dec-2017

@author: senthilkumar
'''

if __name__ == '__main__':
    pass

#Python Default Arguments

def plus(a,b=2):
    return a+b;

print(plus(2,3))
print(plus(2))

#Python Required Arguments

def plus1(a,b):
    return a+b;

print(plus1(2, plus(2)))

#Python keyword Arguments

def plus2(a,b):
    return a+b;

print(plus2(a=4, b=6))
print(plus2(b=4, a=6))

#Python variable number of Arguments

def plus3(*args):
    return sum(args)

print(plus3(1,4,5))

def plus4(*args):
    total = 0
    for i in args:
        total += i
    return total

print(plus3(1,4,5))