'''
Created on 20-Jan-2018

@author: senthilkumar
'''
from com.sen.classes.airtravel7 import *
if __name__ == '__main__':
    pass

flight, boeingFlight = make_flights()

print(flight.aircraft_model())
print(boeingFlight.aircraft_model())
print(flight.num_available_seats())
print(boeingFlight.num_available_seats())