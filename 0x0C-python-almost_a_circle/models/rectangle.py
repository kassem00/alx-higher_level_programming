#!/usr/bin/python3
''' Rectangle class module '''
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class

    Attributes:
        __nb_objects (int): number of opjects created.
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        """
        Initialize a new Rectangle opject.

        Args:
            width (int): width of new Rectangle opject.
            height (int): height of new Rectangle opject.
            x (int): Coordinat attribute.
            y (int): Coordinat attribute.
            id (int): id of new Rectangle opject.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """property of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """property of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """area """
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #."""
        if self.width == 0 or self.height == 0:
            print("")
        else:
            [print("") for z in range(self.y)]
            for i in range(self.height):
                print(" " * self.x, end = "")
                print("#" * self.width)

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/\
{self.height}"
                )

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
           **kwargs (dict): key/value pairs for attributes.
       """
        if args:
            if len(args) > 0:
                self.id = args[0] if args[0] is not None else self.id
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

        elif kwargs:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width)
            self.height = kwargs.get("height", self.height)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)
