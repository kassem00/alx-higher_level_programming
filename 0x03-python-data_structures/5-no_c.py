#!/usr/bin/python3

def remove_c(my_string):
    """
    Remove all occurrences of the letter 'c'
    (both lowercase and uppercase) from a string.
    """
    copy = [char for char in my_string if char.lower() != 'c']
    return ''.join(copy)
