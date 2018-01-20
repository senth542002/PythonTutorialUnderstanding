'''
Created on 20-Jan-2018

@author: senthilkumar
'''
from com.sen.classes.airtravel3 import Flight, Aircraft

if __name__ == '__main__':
    pass

print(range(1, 10), 
                 "ABCDEFGHIJK"[:6])

aircraft = Aircraft("G-EUPT","Airbus A319",num_rows=22, num_seats_per_row=6)
print("Registration Number: "+aircraft.registration())
print("Aircraft Model: "+aircraft.model())
print("Seating Plan",aircraft.seating_plan())

#Law of dementor - Talk to only your friends
flight = Flight("BA747", Aircraft("G-EUPT","Airbus A319",num_rows=22, num_seats_per_row=6))
print(flight.aircraft_model())