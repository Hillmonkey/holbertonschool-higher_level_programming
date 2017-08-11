#!/usr/bin/python3


def multiply_by_2(my_dict):
    if my_dict is None or len(my_dict) == 0:
        return {}
    new_dict = {}
    for k, v in my_dict.items():
        new_dict[k] = v * 2
    return new_dict
