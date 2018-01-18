'''
Created on Jan 15, 2018

@author: VSENTH17
'''

if __name__ == '__main__':
    pass

t = ("Norway", 4.9, 3 )
print(t)

print(t[0])
print(len(t))
print(t + (3381186.0 , 265e9))
print(t * 3)

a = ((22, 284),(1184, 1210),(5020,4050))
print(a[2])
print(a[2][1])

h = (391,)
print(h)
e = ()
print(e)
print(type(e))

def minmax(items):
    return min(items),max(items)

print(minmax([83, 33, 84, 32, 85, 21, 86]))

lower, upper = minmax([83, 33, 84, 32, 85, 21, 86])
print(lower)
print(upper)

(a, (b, (c,d))) = (4, (3,(2,1)))
print(a)
print(b)
print(c)
print(d)

a = 'Jelly'
b = 'Beans'
a, b = b,a

print(a)
print(b)

#Creating Tuple form an existing collection object

print(tuple([561, 1105, 1729, 2465]))
print(tuple("Carmichael"))

print(5 in (3, 4, 5, 6, 7))
print(5 not in (3, 4, 5, 6, 7))

