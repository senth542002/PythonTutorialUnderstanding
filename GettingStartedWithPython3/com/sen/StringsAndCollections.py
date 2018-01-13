'''
Created on Jan 11, 2018

@author: VSENTH17
'''
from builtins import str

if __name__ == '__main__':
    pass

print('"Yes" it is a "String"') #"Yes" it is a "String"

print("first" "second")

#multi line strings
multilineStringUsingDoubleQuotes = """ This is
a multiline
String"""
print("multilineStringUsingDoubleQuotes:"+multilineStringUsingDoubleQuotes)

multilineStringUsingSingleQuotes = ''' This is
a multiline
String'''
print("multilineStringUsingSingleQuotes:"+multilineStringUsingSingleQuotes)

multilineStringUsingControlCharacters = 'This is \na multiline \nString' 
print("multilineStringUsingControlCharacters"+multilineStringUsingControlCharacters)

path2 = r'C:\Users\VSENTH17\Desktop\wsHandlers\com\ford\it\ws\handlers\cookie\jaxws'
print("path2:"+path2)

#Strings
a = str('1bc')
print(a)

a = 'oslo'
print(a.capitalize())

#Bytes prefix b

print(b'some bytes')

norsk = "1234244 *&^&*^ KJHJH )(*&()* ~~~~~~~~~~}}}}}}}"
data = norsk.encode(encoding='utf_8', errors='strict')
print(data)

norwegian = data.decode("utf-8")
print(norwegian)


##Lists

a = [1, 9, 8]
print(a)

c = ["apple","orange","pears"]
c[1] = 8
print(c)


b = []
b.append(1.618)
b.append(1.414)
print(b)

d = list("characters")
print(d)

animals = ['bear',
     'girafee',
     'elephant',
     'caterpillar',]
print(animals)

## DIctionaries

fictionary_entry1 = {'alice' : "123-123-123", 'bob': "323-323-323"}
print(fictionary_entry1)


##For loops
cities = ["London","New York","Paris","Oslo","Helsinki"]
for city in cities:
    print(city)
    
for key in fictionary_entry1:
    print(key, fictionary_entry1[key])
    


## Puting it all together

from urllib.request import urlopen
with urlopen('http://public.oed.com/how-to-use-the-oed/what-is-the-oed-online/') as story:
    story_words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        for line_word in line_words:
            story_words.append(line_word)
            
    print(story_words)

