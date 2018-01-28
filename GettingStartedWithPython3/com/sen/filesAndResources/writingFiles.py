'''
Created on 28-Jan-2018

@author: senthilkumar
'''
import io
from encodings.utf_8 import encode
from idlelib.IOBinding import encoding
if __name__ == '__main__':
    pass

f = open('wasteland.txt', mode='wt')
f.write('What are the roots that clutch, ')
f.write('what branches grow\n')
f.write('Out of this stony rubbish? ')
f.close()

