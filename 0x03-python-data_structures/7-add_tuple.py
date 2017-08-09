#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    ''' returns tuple with two sums
    '''
    new_list = [0, 0]
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    if len(tuple_b) == 0:
        tuple_b = (0, 0)

    if len(tuple_a) == 1:
        tuple_a = tuple_a + (0,)
    if len(tuple_b) == 1:
        tuple_b = tuple_b + (0,)

    for i in range(2):
        new_list[i] = tuple_a[i] + tuple_b[i]
    return tuple(new_list)
