#!/usr/bin/python3
'print(__import__("my_module").my_function.__doc__)'


class Square:
    'print(__import__("my_module").my_function.__doc__)'
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
                print("size must be an integer")
                return TypeError
        if size < 0:
            print("TypeError")
            return ValueError
