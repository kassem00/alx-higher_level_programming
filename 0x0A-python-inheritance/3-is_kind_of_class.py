#!/usr/bin/python3
'''Exact same object'''


def is_kind_of_class(obj, a_class):
    """
    function that returns True if the
    object is exactly an instance of the specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
