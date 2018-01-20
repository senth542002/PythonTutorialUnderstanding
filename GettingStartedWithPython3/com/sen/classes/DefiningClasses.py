'''
Created on 20-Jan-2018

@author: senthilkumar
'''

from com.sen.classes.airtravel import Flight
from com.sen.classes.airtravel2 import Flight as Flight2


if __name__ == '__main__':
    pass

print(type(Flight))
flight = Flight("SN060")
print(type(flight))

print('Flight Number:'+flight.number())

#String slicing
print("SN060"[:2])
print("SN060"[2:])
#flight2 = Flight2("000")#Invalid Airline Code
#flight2 = Flight2("sn060")#Invalid Airline Code
#flight2 = Flight2("SNabcd")#Invalid route number
#flight2 = Flight2("SN12345")#Invalid route number 
flight2 = Flight2("SN1234")
print("Flight Number:"+flight2.number())
print("Airline:"+flight2.airline())
