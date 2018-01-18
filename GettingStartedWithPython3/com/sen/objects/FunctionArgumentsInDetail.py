'''
Created on Jan 15, 2018

@author: VSENTH17
'''
import time
if __name__ == '__main__':
    pass

def banner(message, border="-"):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Norwegian Blue")
banner("Norwegian Blue","*")
banner(border=".", message="Hello from Earth")


#print(time.ctime())

def showDefault(arg=time.ctime()):
    print(arg)

showDefault()
showDefault(arg=time.ctime())
print(time.ctime())

def add_spam(menu=[]):
    menu.append("spam")
    return menu

breakfast = ['bacon','eggs']
print(add_spam(breakfast))

lunch = ['baked beans']
print(add_spam(lunch))

print(add_spam())
print(add_spam())


def add_spamModified(menu=None):
    if menu is None:
        menu = []
    
    menu.append("spam")
    return menu

print(add_spamModified())
print(add_spamModified())