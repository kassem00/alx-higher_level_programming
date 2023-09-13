#!/usr/bin/python3
'''1. write file'''
import json


def save_to_json_file(my_obj, filename):
    '''
    function that writes an Object to a text file
    using a JSON representation:
    '''
    with open(filename, "w") as op_file:
        json.dump(my_obj, op_file)
