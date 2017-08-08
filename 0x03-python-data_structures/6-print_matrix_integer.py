#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    ''' print a matrix aka 2d array of integers
    '''
    if matrix is not None:
        for inner in matrix:
            for i, n in enumerate(inner):
                if i < len(inner) - 1:
                    print("{:d} ".format(n), end='')
                else:
                    print("{:d}".format(n))
