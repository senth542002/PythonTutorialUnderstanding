'''
Created on 20-Jan-2018

@author: senthilkumar
'''
from com.sen.classes.airtravel5 import make_flight
from pprint import pprint as pp
if __name__ == '__main__':
    pass

flight = make_flight()
pp(flight._seating)

flight.relocate_passenger("1C", "13C")
flight.relocate_passenger("1D", "13D")
pp(flight._seating)
print(flight.num_available_seats())