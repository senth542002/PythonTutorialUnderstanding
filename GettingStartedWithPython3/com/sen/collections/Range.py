'''
Created on Jan 15, 2018

@author: VSENTH17
'''

if __name__ == '__main__':
    pass

print(range(5))

for i in range(5):
    print(i)
print(range(1,5))
print(list(range(5, 10)))
print(list(range(5, 10,2)))

#unpythonic way of looping
s = [0, 1, 4, 6, 13]
for i in range(len(s)):
    print(i)
    
for v in s:
    print(v)
    
    
t = [6, 372, 8864, 148800, 2096886]
for p in enumerate(t):
    print(p)
    
for i, v in enumerate(t):
    print(v)
