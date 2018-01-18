'''
Created on Jan 16, 2018

@author: VSENTH17
'''

from pprint import pprint as pp

if __name__ == '__main__':
    pass

urls = {'Google' : 'http://google.com',
        'Pluralsight' : 'http://pluralsight.com',
        'Sixty North' : 'http://sixty-north.com',
        'Microsoft' : 'http://microsoft.com'
        }

print(urls['Pluralsight'])

names_and_ages = [('Alice',32), ('Bob', 48),('Charlie', 28)]
d = dict(names_and_ages)
print(d)

phonetic = dict(a ='alfa', b ='bravo', c = 'charlie', d = 'delta', e = 'echo', f = 'foxrot')
print(phonetic)


d = dict( goldenrod=0xDAA520, indigo=0x4B0082, seashell=0xFFF5EE)
print(d)

e = d.copy()
print(e)

f = dict(d)
print(f)

g = dict(wheat=0xF5DEB3, kakhi=0xF0E68C, crimson=0xDC143C)
f.update(g)
print(f)

stocks = {'GOOG': 891, 'APPL' : 416, 'IBM' : 194}
stocks.update({'GOOG' : 894, 'YHOO': 25})
print(stocks)


colors = dict(aquamarine='#7444D4', burlywood='#DEB887', chartreuse='#7FFF00', cornflower='#6495ED',firebrick='#B22222',
              honeydew='#F0FFF0', maroon='#B03060', sienna='#A0522D')

for color in colors:
    print("{Key} => {value}".format( Key= color, value = colors[color]))

for value in colors.values():
    print(value)
    
for key in colors.keys():
    print(key)
    
for key, value in colors.items():
    print("{Key} => {value}".format( Key= key, value = value))    

symbols = dict(usd='\u0024', gbp = '\u00a3', nzd= '\u0024')
print(symbols)

print('usd' in symbols)
print('\u00a3' in symbols)

m = {'H': [1, 2, 3],
     'He': [3, 4],
     'Li': [6,7],
     'Be': [7, 8, 9],
     'B': [10, 11],
     'C': [11,12,13,124]}
print(m)

m['H'] += {4, 5, 6}
print(m)

m['N'] = {13, 14, 15}
print(m)
pp(m)




