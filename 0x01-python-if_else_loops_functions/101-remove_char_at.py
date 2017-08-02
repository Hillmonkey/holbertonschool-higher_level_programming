#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    elif n == 0:
        newstr = str[1:]
        return newstr
    elif n == len(str) - 1:
        newstr = str[:len(str) - 1]
        return newstr
    else:
        pre = str[:n]
        post = str[n+1: len(str)]
        newstr = pre + post
        return newstr
