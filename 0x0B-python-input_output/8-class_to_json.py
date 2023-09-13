#!/usr/bin/python3
'''8. Class to JSON'''
import json


def class_to_json(obj):
    '''function that returns the dictionary description'''
    return obj.__dict__
