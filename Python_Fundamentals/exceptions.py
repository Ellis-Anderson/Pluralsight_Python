#!/usr/bin/env python3

import sys
from math import log

def string_log(s):
    v = convert(s)
    return log(v)


def convert(s):
    try:
        return int(s)
    except (TypeError, ValueError) as e:
        print("Conversion Error: {}"\
             .format(str(e)),
             file=sys.stderr)
        raise
    
        """
        You could also use pass for exception handling.
        This is useful if you don't want anything to
        happen in your except block.
        """
        
if __name__ == '__main__':
    convert(sys.argv[1])        