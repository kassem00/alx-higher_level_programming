#!/usr/bin/python3

def remove_char_at(str, n):
    """
    function that creates a copy of the string, removing the
    character at the position n
    """
    if n >= 0 and n < len(str):
        return str[:n] + str[n+1:]
    return str
