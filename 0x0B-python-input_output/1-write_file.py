#!/usr/bin/python3
'''1. write file'''


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8) and returns
    the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as op_file:
        op_file.write(text)
        op_file.close()
    return len(text)
