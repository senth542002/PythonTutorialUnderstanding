'''
Created on Jan 16, 2018

@author: VSENTH17
'''

if __name__ == '__main__':
    pass

s = "show how to index into sequences".split()
print(s)
print(s[4])
print(s[-5])
print(s[-1])
print(s[1:4])# slice the list based on start and end indexes
print(s[0:])
print(s[:]) # Full slice

full_slice = s[:]
print(full_slice == s)
print(full_slice is s)

u = s.copy()
print(u == s)
print(u is s)

v = list(s)
print(v == s)
print(v is s)

# Copies are shallow

a = [[1,2], [3,4]]
b = a[:]
print(a == b)
print(a is b)
print(a)
print(b)
a[0] = [8,9]
print(a)
print(b)
a[1].append(5)
print(a)
print(b)
print(b)

c = [21,37]
d = c * 4
print(d)

s = [[-1, +1]] * 5
print(s)
s[3].append(7)
print(s)

w = "the quick brown fox jumps over the lazy dog".split()

print(w.index('fox'))
#print(w.index('unicorn'))
print(w.count("the"))
print(37 in [1,2,3,49,37,85])
print(3 not in [1,2,3,49,37,85])

u = "Jackdaws love my big sphinx of quartz".split()
print(u)
del u[3] # To remove by index
print(u)
u.remove("Jackdaws") # To remove by value
print(u)

a = "I accidentally the whole universe".split()
print(a)
a.insert(2, "destroyed")
print(a)
print(' '.join(a))

#concatination of lists
m = [2,1,3]
n = [4,7,11]
k = m + n
print(k)
k += [18, 29, 47]
print(k)

k.extend([76, 129, 199])
print(k)


#reversing na dsorting

g = [1, 11, 21, 1211, 112111]
g.reverse()
print(g)

d = [5, 17, 41, 29, 71, 149, 3299, 7, 13, 67]
d.sort()
print(d)
d.sort(reverse=True)
print(d)

h = 'not perplexing do handwriting family where I illegibly know doctors'.split()
print(h)
h.sort(key=len, reverse=False)
print(h)
print(' '.join(h))

x = [4, 9, 2, 1]
y = sorted(x)
print(y)

p = [9, 3, 1, 0]
q = reversed(p)
print(q)
print(list(q))

