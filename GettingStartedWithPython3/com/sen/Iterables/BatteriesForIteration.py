'''
Created on 18-Jan-2018

@author: senthilkumar
'''
from itertools import islice, count
from com.sen.Iterables.FilteringPredicates import is_prime
from itertools import chain
from com.sen.Iterables.LazinessAndTheInfinite import lucas

if __name__ == '__main__':
    pass
#islice(all_primes, 1000)

thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
print(list(thousand_primes))
print(sum(islice((x for x in count() if is_prime(x)), 1000)))


print(any([False, False, True]))
print(all([False, False, True]))
print(any(is_prime(x) for x in range(1328, 1361)))
print(all(name == name.title() for name in ['London', 'New York','Sydney']))
print(all(name == name.title() for name in ['london', 'New York','Sydney']))



sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]

for item in zip(sunday, monday):
    print(item)
    
for sun, mon in zip(sunday, monday):
    print("average =",(sun+mon)/2)
    
tuesday = [2, 3, 3, 7, 6, 8, 11, 23, 5, 7, 8, 9]
for temp in zip(sunday, monday, tuesday):
    print("min={:4.1f}, max={:4.1f}, average={:4.1f}".format(min(temp), max(temp), sum(temp)/len(temp)))
    
temperatues = chain(sunday, monday, tuesday)
print(all(t > 0 for t in temperatues ))

for x in (p for p in lucas() if is_prime(p)):
    print(x)
