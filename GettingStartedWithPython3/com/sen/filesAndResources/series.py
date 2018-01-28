'''
Created on 28-Jan-2018

@author: senthilkumar
'''
import sys

def read_series1(filename):
    try:
        f = open(filename, mode='rt')
        series = []
        for line in f:
            a = int(line.strip())
            series.append(a)
    finally:
        f.close()
    return series

def read_series2(filename):
    try:
        f = open(filename, mode='rt')
        return [ int(line.strip()) for line in f]

    finally:
        f.close()

def read_series3(filename):
    with open(filename, mode='rt') as f:
        return [ int(line.strip()) for line in f]

def main(filename):
    series = read_series1(filename)
    print(series)

if __name__ == '__main__':
    main(sys.argv[1])