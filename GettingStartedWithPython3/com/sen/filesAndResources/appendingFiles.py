'''
Created on 28-Jan-2018

@author: senthilkumar
'''

if __name__ == '__main__':
    pass

h = open('wasteland.txt', mode='at')
h.writelines(
    ['Son of man,\n',
    'You cannot say, or guess, ',
    'for you know only,\n',
    'A heap of broken images, ',
    'where the sun beats\n']
    )
h.close()