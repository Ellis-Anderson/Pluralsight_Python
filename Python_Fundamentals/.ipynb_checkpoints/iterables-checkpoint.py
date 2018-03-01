#!/usr/bin/env python3

def take(count, iterable):
    """
    Take items from the front of an iterable
    
    Args:
        count: the number of items to be taken
        iterable: the list from which items are taken
        
    Yields:
        At most, `count` number of `item`s from `iterable`
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)
        

def distinct(iterable):
    """
    Yield distinct items from an iterable
    
    Args:
        iterable: the overall list of items
    
    Yields:
        unique or distinct items from the iterable
    """
    
    seen = set()
    
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)
        
        
def run_distinct():
    items = [5, 5, 6, 6, 6, 1, 7, 7, 1, 5, 3, 2]
    for item in distinct(items):
        print(item)
        
        
def run_pipeline():
    items = [5, 5, 6, 6, 6, 1, 7, 7, 1, 5, 3, 2]
    for item in take(3, distinct(items)):
        print(item)
        
        
if __name__ == '__main__':
    run_take()
    print('\n')
    run_distinct()
    print('\n')
    run_pipeline()
