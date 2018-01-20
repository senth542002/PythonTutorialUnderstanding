'''
Created on 20-Jan-2018

@author: senthilkumar
'''
from com.sen.classes.airtravel4 import *
from pprint import pprint as pp
if __name__ == '__main__':
    pass
flight = Flight("BA747", Aircraft("G-EUPT","Airbus A319",num_rows=22, num_seats_per_row=6))
flight.allocate_seat("12A", "Senthil Kumar")
flight.allocate_seat("15A", "Senthil Kumar")
#flight.allocate_seat("E27", "Senthil Kumar") # Invalid seat number
flight.allocate_seat("1C", "Arun Kumar")
flight.allocate_seat("1D", "Arun Kumar")
#flight.allocate_seat("DD", "Arun Kumar") # INvalid seat row D
pp(flight._seating)
