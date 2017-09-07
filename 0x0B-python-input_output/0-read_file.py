#!/usr/bin/python3
''' module: 0-read_file
'''


def read_file(filename=""):
    ''' function: read_file
    '''
    if filename = "" or type(filename) != str:
        return
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')
