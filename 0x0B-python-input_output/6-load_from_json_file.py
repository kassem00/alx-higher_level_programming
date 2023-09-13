#!/usr/bin/python3
'''1. write file'''
import json

def load_from_json_file(filename):
    '''
    function that writes an Object to a text file
    using a JSON representation:
    '''
    with open(filename) as op_file:
        return json.load(op_file)
