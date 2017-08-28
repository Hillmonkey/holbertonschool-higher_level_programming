#!/usr/bin/python3
'''
this is the 4-print_square module
'''


def print_square(size):
    ''' Print a square of pound signs, size x size

    Keyword argument:
    size -- The size of the square to print
    '''

    # ERROR MESSAGE DICT  #
    err_msg = {}
    err_msg["NaInt"] = "size must be an integer"
    err_msg["LTzero"] = "size must be >= 0"

    #  TESTS  #

    if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError(err_msg["NaInt"])
    if size < 0:
        raise ValueError(err_msg["LTzero"])

    #  PRINT SQUARE  #
    for i in range(size):
        # for j in range(size):
            # print("#", end='')
        print("#" * size, end='')
        print()
