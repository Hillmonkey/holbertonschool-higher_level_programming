#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list == []:
        return 0
    top = 0
    bottom = 0
    for el in my_list:
        top += (el[0] * el[1])
        bottom += el[1]
    return top / bottom
