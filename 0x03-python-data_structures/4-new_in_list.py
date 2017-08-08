#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    ''' replace element in list
    '''

    new = []
    for el in my_list:
        new.append(el)
    if idx in range(len(new)):
        new[idx] = element
    return new
