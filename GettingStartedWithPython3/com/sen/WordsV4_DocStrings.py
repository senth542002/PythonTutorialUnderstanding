#! C:/Users/VSENTH17/AppData/Local/Programs/Python/Python36-32/python
'''
Retrieve and print words from a URL.

Usage:
    python WordsV4_DocStrings.py <URL>
Created on Jan 12, 2018

@author: VSENTH17
'''

from urllib.request import urlopen
import sys

def fetch_words(url):
    """Fetch a list of words from a URL.
    
    Args:
        url: The URL of a UTF-8 text document.
    
    Returns:
        A list of strings containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf-8").split()
            for line_word in line_words:
                story_words.append(line_word)
    return story_words 

def print_items(items):
    """Print items one per line.
    
    Args:
        An iterable series of printable items.
    """
    for item in items:
        print(item)

def main(url):
    """Print each word from a text document from a URL.
    
    Args:
        url: The URL of a UTF-8 document.
    """
    words = fetch_words(url)
    print_items(words)
            
if(__name__ == '__main__'):
    main(sys.argv[1])   
             
