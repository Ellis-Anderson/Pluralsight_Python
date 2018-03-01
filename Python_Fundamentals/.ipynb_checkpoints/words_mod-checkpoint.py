#!/usr/bin/env python3
""" 
Retrieve and print words from a URL

Usage:

    python3 words_mod.py <url>
"""


from urllib.request import urlopen
import sys

def fetch_words(url):
    
    """
    This function gets words from the url within urlopen()
    It supports both REPL and terminal execution.
    It can be imported and executed in the REPL,
    or it can be executed in the terminal thanks to the final if statement
    
    Args:
        url: The URL of a UTF-8 document.
        
    Returns:
        A list of strings containing the words from the document.
    """
    
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words
 

def print_items(items):
    
    """
    prints any iterable set of values line by line. 
    
    Args:
        items: a list of iterable items to be printed
    """
    
    for item in items:
        print(item)
     
    
def main(url):
    
    """
    Using a URL, this function gets words from that URL using fetch_words()
    then passes them to print_items to be printed line by line. 
    The URL is either supplied by the user (REPL) or through arg-v (script execution)
    
    Args:
        url: A URL supplied at either the command-line or the REPL
        linking to a UTF-8 document. 
    """
    
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
    
    """
    sys.argv[1] is supplied here instead of in the main function. 
    This allows us to use the REPL - where the if block is not evaluated
    and we can call the function with a URL, 
    or at the command-line with a user supplied argv argument.
    """