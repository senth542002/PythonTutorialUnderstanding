'''
Created on Jan 16, 2018

@author: VSENTH17
'''
from com.sen.exceptions.exceptional import convert_with_exception_handling_raise
from math import log

def string_log(s):
    v = convert_with_exception_handling_raise(s)
    return log(v)
