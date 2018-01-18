'''
Created on 18-Jan-2018

@author: senthilkumar
'''

if __name__ == '__main__':
    pass

#Iterable and Iterator protocols

iterable = ['Spring','Summer','Autumn','Winter']
iterator = iter(iterable)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))

def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterator is empty")

print(first(['1st','2nd','3rd']))
print(first({'1st','2nd','3rd'}))
first(set())