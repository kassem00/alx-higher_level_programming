#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """rectangle."""
     def __init__(self, width=0, height=0):
        """Initialize a Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width
     @property
    def height(self):
        """set the height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        else:
            if value <0:
                raise ValueError("width must be >= 0")
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
