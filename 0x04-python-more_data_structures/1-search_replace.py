#!/usr/bin/python3


def search_replace(my_list, search, replace):

    new = my_list[:]
    s_l = [search] * len(my_list)
    r_l = [replace] * len(my_list)
    return list(map(lambda x, y, z: z if x == y else x, new, s_l, r_l))
