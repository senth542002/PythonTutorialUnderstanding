'''
Created on 30-Dec-2017

@author: senthilkumar
'''

class Summation(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    def sum(self, a, b):
        self.contents = a + b
        return self.contents
    
    def hello(self):
        name = str(raw_input("Enter your name: "))
        if name:
            print("Hello "+name)
        else:
            print("Hello World")
        return name
    

