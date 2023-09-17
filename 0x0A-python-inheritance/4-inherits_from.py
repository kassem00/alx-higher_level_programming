#!/usr/bin/python3
'''Exact same object'''

def inherits_from(obj, a_class):
    """
    function that returns True if the
    object is exactly an instance of the specified class
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
