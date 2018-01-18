'''
Created on Jan 16, 2018

@author: VSENTH17
'''
import sys
def convert(s):
    '''convert to an Integer. '''
    x = int(s)
    return x

def convert_with_exception_handling(s):
    ''' Convert to an integer.'''
    try:
        x = int(s)
        return x
    except(ValueError, TypeError) as e:
        print("Conversion error:{}"\
              .format(str(e), file=sys.stderr))
        return -1

def convert_with_exception_handling_raise(s):
    ''' Convert to an integer.'''
    try:
        return int(s)
    except(ValueError, TypeError) as e:
        print("Conversion error:{}"\
              .format(str(e), file=sys.stderr))
        raise
    finally:
        print("Inside finally block to execute mandatory processes")

