#!/usr/bin/python3
'''
This is the add_integer module
'''


def add_integer(a, b):

    """Add two integers.

    Keyword arguments:
    a -- first integer
    b -- second integer
    """

    # I guess that we should accept booleans as their int equivalents?!?
    # But I am only guessing because specs are vague!!!
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    c = a + b
    return c
