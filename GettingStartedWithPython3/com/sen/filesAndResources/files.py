'''
Created on 28-Jan-2018

@author: senthilkumar
'''
import sys
def main(fileName):
    f = open(fileName, mode='rt')
    for line in f:
        #print(line)
        sys.stdout.write(line)
    f.close()
    
if __name__ == '__main__':
    main(sys.argv[1])
    