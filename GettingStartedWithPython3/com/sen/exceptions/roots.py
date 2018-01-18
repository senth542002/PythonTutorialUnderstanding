'''
Created on Jan 16, 2018

@author: VSENTH17
'''
import sys

def sqrt(x):
    ''' Computes square root.'''
    if x < 0:
        raise ValueError("Cannot compute square root of negative number {}".format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("This is never printed")
    except (ZeroDivisionError, ValueError) as e:
        print(e, file=sys.stderr)
    print("Program execution continues normally here.")
    
if __name__ == '__main__':
    main()    