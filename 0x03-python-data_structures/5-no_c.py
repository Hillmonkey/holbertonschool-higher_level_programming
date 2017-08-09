#!/usr/bin/python3


def no_c(my_string):
    ''' create new string that is a version of my_string
        but, with C and c removed '''

    if my_string is None:
        return (my_string)
    return "".join([ch if ch not in "Cc" else "" for ch in my_string])
