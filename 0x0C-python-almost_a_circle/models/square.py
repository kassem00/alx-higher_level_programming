#!/usr/bin/python3
''' square class module '''
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class module """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new square opject.

        Args:
            size (int): size of new square opject.
            x (int): Coordinat attribute.
            y (int): Coordinat attribute.
            id (int): id of new square opject.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size>"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """property of height"""
        return self.width

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value
        """setter of height"""

    def update(self, *args, **kwargs):
        """
        Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            if len(args) > 0:
                self.id = args[0] if args[0] is not None else self.id
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        elif kwargs:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)
