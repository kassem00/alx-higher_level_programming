#!/usr/bin/python3

def print_last_digit(number):
    if isinstance(number, int):
        num_s = str(number)
        x = num_s[-1]
        print("{}".format(x), end="")
        return int(x)
    else:
        print("Traceback (most recent call last):")
