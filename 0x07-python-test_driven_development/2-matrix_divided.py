#!/usr/bin/python3
'''
This is the matrix_divided module
'''


def matrix_divided(matrix, div):
    '''Divide every element of 2D array by a number

    Keyword argument:
    matrix -- A list of lists of numbers
    div -- the number to divide all the matrix array elements by ..
    '''

    #  ERROR MESSAGE DICT #
    err_msg = {}
    err_msg["Not_Matrix"] = (
            "matrix must be a matrix (list of lists) of integers/floats")
    err_msg["Not_Regular"] = (
            "Each row of the matrix must have the same size")
    err_msg["NaN"] = (
            "div must be a number")
    err_msg["ZeroDiv"] = (
            "division by zero")

    new_matrix = []

    #  TESTS #

    if div == 0:
        raise ZeroDivisionError(err_msg["ZeroDiv"])

    if not isinstance(div, (int, float)) or isinstance(div, (bool)):
        raise TypeError(err_msg["NaN"])
    if type(matrix) != list:
        raise TypeError(err_msg["Not_Matrix"])

    if len(matrix) > 0:
        yardstick = matrix[0]
    for el in matrix:
        if type(el) != list:
            raise TypeError(err_msg["Not_Matrix"])
        if len(el) != len(yardstick):
            raise TypeError(err_msg["Not_Regular"])
        for num in el:
            if not isinstance(num, (int, float)) or isinstance(num, (bool)):
                raise TypeError(err_msg["Not_Matrix"])

    # BUILD NEW MATRIX #

    for i, el in enumerate(matrix):
        new_matrix.append([])
        for num in el:
            #  append num/div rounded to two decimal places
            new_matrix[i].append((int((num / div) * 100 + 0.5)) / 100)
    if new_matrix == []:
        new_matrix = [[]]
    return new_matrix
