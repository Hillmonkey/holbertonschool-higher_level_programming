#!/usr/bin/python3


def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    elif n == 0:
        return str[1:]
    elif n == len(str) - 1:
        return str[:n]
    else:
        pre = str[:n]
        post = str[n+1:]
        return str[:n] + str[n+1:]
