'''
Created on 01-Jan-2018

@author: senthilkumar
'''

if __name__ == '__main__':
    pass

double = lambda x: x * 2

print(double(5))

sumation = lambda x, y : x + y

print(sumation(2,3))

my_list = [1,2,3,4,5,6,7,8,9,10]

filtered_list = list(filter(lambda x: (x*2 > 10), my_list))
print(filtered_list)

mapped_list = list(map(lambda x: x*2, my_list))
print(mapped_list)

reduced_list = reduce(lambda x,y: x+y, my_list)
print(reduced_list)
