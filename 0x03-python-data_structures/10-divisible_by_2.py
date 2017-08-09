#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    ''' return a list of booleans corresponding to the truth value of
    my_list[i] is divisible by 2 for each element in my_list
    '''

    bool_list = []
    for i in my_list:
        if i % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list
