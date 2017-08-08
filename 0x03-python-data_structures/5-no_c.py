#!/usr/bin/python3


def no_c(my_string):
    ''' create new string that is a version of my_string
        but, with C and c removed '''

    if my_string is None:
        return (my_string)
    new_str = ""
    for ch in my_string:
        if ch != "c" and ch != "C":
            new_str += ch
    return new_str
