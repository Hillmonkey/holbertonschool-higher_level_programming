#!/usr/bin/python3


def element_at(my_list, idx):
    ''' retrieves element from a list
    '''

    if idx in range(len(my_list)):
        return my_list[idx]
    else:
        return None
