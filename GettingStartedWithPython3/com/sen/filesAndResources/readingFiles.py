'''
Created on 28-Jan-2018

@author: senthilkumar
'''

if __name__ == '__main__':
    pass

g = open('wasteland.txt', mode='rt')
print(g.read(32))
print(g.read())
print(g.read())
g.seek(0)
print(g.readline())
print(g.readline())

g.seek(0)
print(g.readlines())
g.close()