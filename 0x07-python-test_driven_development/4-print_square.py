#!/usr/bin/python3
'''a function that adds 2 integers.'''


def print_square(size):
    ''' function that prints a square with the character # '''
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(size):
            print("#", end="")
        print("")
