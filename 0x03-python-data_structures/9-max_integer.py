#!/usr/bin/python3


def max_integer(my_list=[]):
    ''' returns max integer
    '''

    if my_list is None or len(my_list) == []:
        return None
    max = my_list[0]
    for i in range(len(my_list)):
        max = my_list[i] if my_list[i] > max else max
    return max
