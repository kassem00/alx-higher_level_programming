#!/usr/bin/python3
'''0. Read file'''


def read_file(filename=""):
    with open(filename, encoding="utf-8") as op_file:
        print(op_file.read())