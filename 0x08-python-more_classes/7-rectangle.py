#!/usr/bin/python3

"""Rectangle class"""


class Rectangle:
    """rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle."""
        type(self).number_of_instances += 1
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

    def __str__(self):
        """Represents the rectangle with the # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectang = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectang.append(str(self.print_symbol))
            if i != self.__height - 1:
                rectang.append('\n')
        return ''.join(rectang)

    def __repr__(self):
        """representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

