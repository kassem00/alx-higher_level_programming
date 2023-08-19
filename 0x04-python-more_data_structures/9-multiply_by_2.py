#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    return ({a: a_dictionary[k] * 2 for a in a_dictionary})
