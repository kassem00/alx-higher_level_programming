#!/usr/bin/python3
'print(__import__("my_module").my_function.__doc__)'


class Square:
    'print(__import__("my_module").my_function.__doc__)'
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
