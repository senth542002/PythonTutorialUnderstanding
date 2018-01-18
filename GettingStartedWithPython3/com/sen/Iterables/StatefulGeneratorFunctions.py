'''
Created on 18-Jan-2018

@author: senthilkumar
'''

if __name__ == '__main__':
    pass

def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item
        
def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)
        
run_take()
print("-x-x-x-x-x-x-")





def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)


run_distinct()
print("-x-x-x-x-x-x-")


def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)
        
run_pipeline()
print("-x-x-x-x-x-x-")