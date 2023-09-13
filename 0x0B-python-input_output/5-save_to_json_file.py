#!/usr/bin/python3
'''1. write file'''
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as op_file:
        json.dump(my_opj, f)
