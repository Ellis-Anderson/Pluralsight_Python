from urllib.request import urlopen

def fetch_words():
    
    """
    This function gets words from the url within urlopen()
    It supports both REPL and terminal execution.
    It can be imported and executed in the REPL,
    or it can be executed in the terminal thanks to the final if statement
    """
    
    with urlopen("http://sixty-north.com/c/t.txt") as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    for word in story_words:
        print(word)

if __name__ == '__main__':
    fetch_words()