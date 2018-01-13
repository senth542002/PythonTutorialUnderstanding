'''
Created on Jan 12, 2018

@author: VSENTH17
'''

from urllib.request import urlopen
import sys

def fetch_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf-8").split()
            for line_word in line_words:
                story_words.append(line_word)
    return story_words 

def print_items(items):
    for item in items:
        print(item)

def main(url):
    words = fetch_words(url)
    print_items(words)
            
if(__name__ == '__main__'):
    main(sys.argv[1])   
             
