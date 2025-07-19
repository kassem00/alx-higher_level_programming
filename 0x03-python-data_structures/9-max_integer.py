#!/usr/bin/python3


def max_integer(my_list=[]):
    """
    max integer in list
    """
    if my_list:
        my_list.sort()
        return my_list[-1]
    return None
