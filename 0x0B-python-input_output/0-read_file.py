#!/usr/bin/python3
'''0. Read file'''


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename,'r', encoding="utf-8") as op_file:
        print(op_file.read())
