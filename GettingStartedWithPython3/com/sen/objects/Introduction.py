'''
Created on Jan 15, 2018

@author: VSENTH17
'''

if __name__ == '__main__':
    pass

a = [1, 10, 15]
b = a
b[2] = 25

print(a==b)
print(a is b)

print(id(a))
print(id(b))


p = [4, 7, 11]
q = [4, 7, 11]

print(p==q)
print(id(p))
print(id(q))
print(p is q)