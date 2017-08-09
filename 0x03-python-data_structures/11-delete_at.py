#!/usr/bin/python3


def delete_at(my_list=[], idx=0):

    tmp_list = my_list
    for i, el in enumerate(tmp_list):
        if i == idx:
            del my_list[i]
    return my_list
