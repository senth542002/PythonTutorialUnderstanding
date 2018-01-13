'''
Created on Jan 10, 2018

@author: VSENTH17
'''
import math
from math import factorial as fac
from pip._vendor.requests.packages.urllib3 import response
from builtins import int
if __name__ == '__main__':
    pass


print(math.sqrt(81))
print(fac(5))

'''
number of ways of drawing 3 fruits from a 5 fruits
'''
n = 5
k = 3

number_of_ways1 = fac(n)/(fac(k) * fac(n-k))
print(number_of_ways1)
number_of_ways2 = fac(n)//(fac(k) * fac(n-k))
print(number_of_ways2)

print(2 * 32)
print(2 ** 32) 
print(fac(13))

print(fac(100))
print(len(str(fac(100))))

print(3e8)
print(type(3.125))

print(True)
print(False)

print(bool(0))
print(bool(-1))
print(bool(55))
print(bool(0.0))
print(bool(-1.717))
print(bool([]))
print(bool([1,2,3]))
print(bool(""))
print(bool("Spam"))

g = 20

print(g == 20)
print(g > 20)

print(g < 20)

if True:
    print("It's true!")

if False:
    print("It's true!")
    
if bool("Eggs"):
    print("Yes")

h =40

if h > 50:
    print("Greater than 50")
elif h < 20:
    print("Less than 20")
else:
    print("Between 20 and 50")
    
c = 5    
while c != 0:
    print(c)
    c -= 1

c =5
while bool(c):
    print(c)
    c -= 1

while True:
    response = input()
    if int(response) % 7 == 0:
        break


