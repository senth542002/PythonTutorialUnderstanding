'''
Created on 01-Jan-2018

@author: senthilkumar
Requires:
legs = legs so that the dog can walk
color =A color of the fur
'''

class Dog:
    def __init__(self, legs, color):
        self.legs = legs
        self.color = color
        
    def bark(self):
        bark = "bow! " * 2
        return bark;
        

if __name__ == '__main__':
    dog = Dog(4,"Brown")
    print(dog.bark())