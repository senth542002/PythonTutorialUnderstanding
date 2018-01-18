'''
Created on 18-Jan-2018

@author: senthilkumar
'''

if __name__ == '__main__':
    pass

def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b

for x in lucas():
    print(x)