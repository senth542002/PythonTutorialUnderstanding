'''
Created on 18-Jan-2018

@author: senthilkumar
'''
from math import sqrt
from pprint import pprint as pp

if __name__ == '__main__':
    pass

def is_prime(x):
    if(x < 2):
        return False
    for i in range(2, int(sqrt(x))+1):
        if x % i ==0:
            return False
    return True


print([x for x in range(101) if is_prime(x)])

prime_square_divisors = {x*x : (1, x, x*x) for x in range(101) if is_prime(x) }
print(pp(prime_square_divisors))