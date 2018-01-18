'''
Created on 18-Jan-2018

@author: senthilkumar
'''
from pprint import pprint as pp

if __name__ == '__main__':
    pass

country_to_capital = {'United Kingdom' : 'London',
                      'Brazil':'Brazilia',
                      'Morocco':'Rabat',
                      'Sweden':'Stockholm'}

print({capital : country for country, capital in country_to_capital.items()})
print(pp({capital : country for country, capital in country_to_capital.items()}))

words = ["hi", "hello","foxrot","hotel"]
print({x[0] : x for x in words})
