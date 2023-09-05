#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """set the height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
