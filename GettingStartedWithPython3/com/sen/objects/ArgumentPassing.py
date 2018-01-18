'''
Created on Jan 15, 2018

@author: VSENTH17
'''

if __name__ == '__main__':
    pass

m = [9, 15, 24]

def modify(k):
    k.append(39)
    print("k=",k)


modify(m)


f = [14, 23, 37]

def replace(g):
    g = f.copy()
    g.append(40)
    print("g=",g)
    print("f=",f)

replace(f)