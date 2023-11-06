#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """function that returns a new dictionary with all values multiplied by 2"""
    new = a_dictionary.copy()
    for k in new.keys():
        new[k] *= 2
    return new
