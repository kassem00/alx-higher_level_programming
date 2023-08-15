#!/usr/bin/python3

def element_at(my_list, idx):
    length = len(my_list)
    if (idx < 0) or (idx > length):
        return None
    else:
        i = 0
        while(idx != i):
            i = i + 1
        return my_list[i]
