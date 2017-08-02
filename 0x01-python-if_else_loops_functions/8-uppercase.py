#!/usr/bin/python3


def islower(c):
    '''islower returns a boolean
    '''
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False


def uppercase(str):
    offset = ord('A') - ord('a')
    for c in str:
        if islower(c):
            newc = chr(ord(c) + offset)
        else:
            newc = c
        print("{:s}".format(newc), end='')
    print('')
