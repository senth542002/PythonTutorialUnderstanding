'''
Created on Jan 15, 2018

@author: VSENTH17
'''

if __name__ == '__main__':
    pass

print(len("llanfairpwllgyll"))
print("new"+"found"+"land")

s = "new"
s += "found"
s += "land" 
print(s)

colors = ";".join(['#45ff23', '#2321fa','#1298a3','#a32312'])
print(colors)
print(colors.split(';'))
print(''.join(['high','way','man']))

#partision
print("unforgetable".partition("forget"))

departure, separator, arrival = "London:Edinburgh".partition(':')
print(departure)

origin, _, destination = "Seattle-Boston".partition('-')
print(origin)
print(type(origin))

print("The age of {0} is  {1}".format('jim',21))

print("The age of {0} is {1}. {0}'s birthday is on {2}".format('Fred',24,'October 31'))

print("Reticilating spline {} of {}.".format(4,23))
print("Current position {lattitude} {longitude}".format(longitude="30S", lattitude="60N"))

'Galactic position x=65.2 y=23.1 z=82.2'

import math

print("Math constants: pi={m.pi}, e={m.e}".format(m=math))
print("Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))




