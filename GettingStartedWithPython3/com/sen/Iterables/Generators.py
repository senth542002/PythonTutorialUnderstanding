'''
Created on 18-Jan-2018

@author: senthilkumar
'''

if __name__ == '__main__':
    pass

def gen123():
    yield 1
    yield 2
    yield 3
    
g = gen123()
print(g)
print(next(g))
print(next(g))
print(next(g))
#print(next(g))

for v in gen123():
    print(v)

def gen456():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")

g = gen456()
print(next(g))
print(next(g))
print(next(g))
print(next(g))

