#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length = len(my_list) - 1
    if (idx < 0) or (idx > length):
        return my_list
    new = my_list
    new[idx] = element
    return new
