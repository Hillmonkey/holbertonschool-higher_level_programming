#!/usr/bin/python3
''' module: 2-read_lines
'''


def read_lines(filename="", nb_lines=0):
    ''' function: read_lines
    readi, send to stdout specified number of lines of file.  If nb_lines <= 0
    or nb_lines > number of lines in file, then read all lines
    '''
    if filename == "" or type(filename) != str:
        return
    if type(nb_lines) != int:
        return
    counter = 0
    with open(filename, "r") as f:
        for line in f:
            counter += 1
            if nb_lines <= 0 or (counter <= nb_lines and nb_lines > 0):
                print(line, end='')
            else:
                break
