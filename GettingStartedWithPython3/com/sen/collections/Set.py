'''
Created on Jan 16, 2018

@author: VSENTH17
'''

if __name__ == '__main__':
    pass

p = {6,28, 467, 8128, 33440336}
print(p)
print(type(p))

d ={}
print(type(d))

e = set()
print(e)

s = set([2, 4, 16, 64, 128, 4096])
print(s)

t = [1, 4, 2, 1, 7, 9, 9]
print(set(t))

for x in {1, 2, 3, 4, 5, 6, 7}:
    print(x)
    
q = {2, 9, 6, 4}
print(9 in q)
print(6 not in q)

k = {81, 108}
k.add(21)
print(k)

k.add(81)
print(k)

k.update([81, 24, 67])
print(k)


k.remove(81)
print(k)

k.discard(24)
print(k)

j = k.copy()
print(j)
m = set(k)
print(m)

#Set operations

blue_eyes = {'olivia', 'harry', 'lily', 'jack','amelia'}
blond_hair = {'harry', 'jack', 'amelia','mia','joshua'}
smell_hcn = {'harry','amelia'}
taste_ptc = {'harry','lily','amelia','lola'}
o_blood = {'mia','joshua','lily','olivia'}
b_blood = {'amelia','jack'}
a_blood = {'harry'}
ab_blood = {'joshua','lola'}

print(blue_eyes.union(blond_hair))
print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))
print(blue_eyes.intersection(blond_hair))
print(blond_hair.difference(blue_eyes))
print(blond_hair.symmetric_difference(blue_eyes))

print(smell_hcn.issubset(blond_hair))
print(taste_ptc.issuperset(smell_hcn))
print(a_blood.isdisjoint(o_blood))
