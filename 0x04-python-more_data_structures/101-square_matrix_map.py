#!/usr/bin/python3
# https://stackoverflow.com/questions/30952526/nested-maps-in-python-3
def square_matrix_map(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
