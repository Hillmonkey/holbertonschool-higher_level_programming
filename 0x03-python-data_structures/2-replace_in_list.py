#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    ''' replace element in list
    '''

    if idx in range(len(my_list)):
        my_list[idx] = element
    return my_list
