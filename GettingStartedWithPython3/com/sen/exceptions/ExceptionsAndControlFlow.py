'''
Created on Jan 16, 2018

@author: VSENTH17
'''
from com.sen.exceptions.exceptional import convert, convert_with_exception_handling,\
    convert_with_exception_handling_raise
from com.sen.exceptions.string_log import string_log
from com.sen.exceptions import roots

if __name__ == '__main__':
    pass

print(convert("33"))
#print(convert("hedgehog"))


print(convert_with_exception_handling("33"))
print(convert_with_exception_handling("hedgehog"))

print(convert_with_exception_handling([4, 5, 6]))

#print(string_log("ouch"))
print(string_log("256"))

print(roots.main())

print(convert_with_exception_handling_raise("abcd"))