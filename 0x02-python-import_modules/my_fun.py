#!/usr/bin/python3
# my_fun.py
import sys


def fun():
    """loop through arguments"""
    for i in range(len(sys.argv)):
        if i > 0:
            print(f"{i}: {sys.argv[i]}")
