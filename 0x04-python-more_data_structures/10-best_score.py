#!/usr/bin/python3


def best_score(my_dict):
    if my_dict is None or len(my_dict) == 0:
        return None
    maxKey = list(my_dict.keys())[0]
    for k in my_dict.keys():
        if my_dict[k] > my_dict[maxKey]:
            maxKey = k
    return maxKey
