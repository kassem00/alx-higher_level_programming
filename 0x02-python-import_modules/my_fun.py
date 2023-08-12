#!/usr/bin/python3
# my_fun.py

if __name__ == "__main__":
    """loop througe argument"""
    import sys


def fun():
    """loop througe argument"""
    for i in range(len(sys.argv)):
        if i > 0:
            print(i, sys.argv[i])
