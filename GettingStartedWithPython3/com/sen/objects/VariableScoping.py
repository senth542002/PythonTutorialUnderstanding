'''
Created on Jan 15, 2018

@author: VSENTH17
'''
#from scope import *

if __name__ == '__main__':
    pass

count = 0

def set_count(c):
    count = c
    
def show_count():
    print("count=", count)
    
print(count)
set_count(2)
print(count)

def set_count_modified(c):
    global count
    count = c
    
set_count_modified(2)
print(count)