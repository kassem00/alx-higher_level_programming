#!/usr/bin/python3
'''Only sub class of'''


def inherits_from(obj, a_class):
    """
    function that returns True if the
    if the object is an instance of a
    class that inherited (directly or indirectly)
    from the specified class
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
