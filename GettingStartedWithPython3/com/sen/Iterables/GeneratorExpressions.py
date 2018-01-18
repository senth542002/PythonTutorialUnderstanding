'''
Created on 18-Jan-2018

@author: senthilkumar
'''
from com.sen.Iterables.FilteringPredicates import is_prime

if __name__ == '__main__':
    pass
million_squares = (x*x for x in range(1000000))
print(million_squares)

print(sum(x*x for x in range(1000000)))

print(sum(x*x for x in range(1000000) if is_prime(x)))