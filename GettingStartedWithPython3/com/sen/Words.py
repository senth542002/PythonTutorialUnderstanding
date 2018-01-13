'''
Created on Jan 12, 2018

@author: VSENTH17
'''

from urllib.request import urlopen

def fetch_words(self):
    with urlopen('http://public.oed.com/how-to-use-the-oed/what-is-the-oed-online/') as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf-8").split()
            for line_word in line_words:
                story_words.append(line_word)
     
    for word in story_words:
        print(word) 
        
if(__name__ == '__main__'):
    fetch_words("")      
             
