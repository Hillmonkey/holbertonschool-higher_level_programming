#!/usr/bin/python3


def print_sorted_dictionary(my_dict):

    if my_dict is None or len(my_dict) == 0:
        return
    for k in sorted(my_dict.keys()):
        print("{}: {}".format(k, my_dict[k]))
